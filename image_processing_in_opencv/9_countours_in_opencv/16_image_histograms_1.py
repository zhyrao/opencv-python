#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-22
# @Author  : Joe

import numpy as np
import cv2
from matplotlib import pyplot as plt 

# link: 	#https://docs.opencv.org/3.0-beta/doc/py_tutorials/
		#py_imgproc/py_histograms/py_histogram_begins/py_histogram_begins.html
# Find \ Plot \  Analyze
# 查找 绘制 分析

# Goal 目标
	# 用OpenCV\Numpy接口函数找到直方图
	# 用OpenCV\Matplotlib绘制\显示直方图

# Theory 理论
	# 什么是直方图？ 可以认为直方图是一副图表或者图，它
	# 给出了关于一副图像的强度分布的总体概览。这个图中的
	# X轴代表了像素值，Y轴代表了图像中每个像素值的个数。

	# 这只是理解图像内容的另外一种方式。通过查看图像的
	# 直方图，对图像的对比、亮度、强度分布等等有一个直
	# 观的了解。现今大部分图像处理工具，都会提供这个直
	# 方图的功能。下面是一副从剑桥图像网站上的图片：

	# 可以看出这幅图像的直方图。（注意，直方图是由灰度
	# 图绘制的，不是彩色图）。左边区域显示了图像中的暗
	#  的像素的数量，右边区域显示了亮的数量。从这幅图中，
	# 可以明显看出，暗区域比亮区域多很多，而中间色调（
	# 像素值在中间，如127）非常少。

# Find Histogram 查找直方图
	# 现在我们对图像直方图有了一定的理解，那么我们来看
	# 看怎么找到这个图像的直方图。OpenCV和Numpy都提供
	# 了内置的接口函数。在使用这些函数之前，我们需要来
	# 理解一些直方图有关的名词术语。

	# BINS:区间
		# 上面的直方图显示了图像中的每个像素的像素值。
		# 例如从0到255，你需要256个值来显示在直方图上。
		# 如果不需要详细的显示每个像素值，而是需要显示
		# 一定区间的像素值呢？例如，需要找到像素在0-15，
		# 16-31...... 240-255. 那么只需要16个值来显示
		# 直方图。

		# 所以需要将整个直方图的值分为16份，每份加起来
		# 为总的数量。这每个份，就成为BIN。第一种情况
		# 下bins的数量为256，而第二种情况下，bins的数量
		# 为16个。在OpenCV文档中，BINS被称为histSize。

	# DIMS: 维度
		# 这是我们收集数据的参数的个数。在目前的情况中，
		# 我们只需要一个值，灰度图像的强度值，所以DIMS
		# 是1. （如果是从色彩图中收集数据有可能是3或者
		# 4）

	# RANGE: 范围
		# 需要测量的强度值的范围。通常是所有的强度范围。
		# 【0,255】

# 1.Histogram Calculation in OpenCV
	# 现在我们是用cv2.calcHist()函数来找到直方图，首先
	# 熟悉一下函数及其参数
	# cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
	# 1. images: 原图像的数据，类型为uint8或者float32. 需
			      #要用中括号括起来 [img]
	# 2.channels: 我们计算直方图的数据的通道下标。例如
				#如果是灰度图，那么就是[0]。如果是色
				#彩图，[0],[1],[2]分别表示了图像中的
				#blue,green,red（opencv为BGR）
	# 3.mask: 遮罩图。如果计算整个图像的直方图，那么这里
				#是None。如果需要找到一个特定区域的直方
				#图，那么就需要计算这个特定区域的遮罩图
				#并传入这个遮罩图。
	# 4.histSize: 这里是指区间的个数。如果是整个像素值范围
				#那么是[256]
	# 5.ranges: [0,256]

img = cv2.imread('tower.jpg',0)
hist = cv2.calcHist([img], [0], None, [256],[0,256])
	# 这里 hist是一个256 x 1大小的数据，每个值代表了图像中该像素值所有的个数

# 2.Histogram Calculation in Numpy
	# Numpy提供了函数 np.histogram()。
hist, bins = np.histogram(img.ravel(), 256,[0,256])
	# hist 跟opencv中的结果是一样的，但是bins会有257个
	# 因为在numpy中区间位0-0.99,1-1.99，2-2.99等，这样
	# 最终的范围是255-255.00.这样最终会加上256,。但是
	# 并不需要256.到255已经足够了。

# 注意，opencv的函数比np.histogram()运行速度要快（大概40倍）
# 所以尽量使用opencv的函数接口。



# Plotting Histograms 绘制直方图
	# 1. Matplotlib plotting 函数
	# 2. OpenCV drawing 函数

	# 1.Matplotlib
		# matplotlib 提供了绘制直方图的函数接口
		# matplotlib.pyplot.hist()
		# 这个函数直接计算了图像的直方图数据并且
		# 绘制。所以不需要用opencv或者numpy来计算。
#plt.hist(img.ravel(), 256,[0,256])
#plt.show()
	
	# 或者可以使用正常的绘制，比如是BGR分别绘制出来，
	# 这样情况下我们需要先找到直方图的数据。
# cv2.imshow('img', img)
# color = ('b','g','r')
# for i,col in enumerate(color):
# 	print(i, col)
# 	histr = cv2.calcHist([img],[i],None,[256],[0,256])
# 	plt.plot(histr, color = col)
# 	plt.xlim([0,256])

# plt.show()


# Application of Mask 遮罩的运用
# create a mask
mask = np.zeros(img.shape[:2], np.uint8)
mask[50:100, 50:150] = 255
masked_img = cv2.bitwise_and(img,img,mask = mask)

# Calculate histogram with mask and without mask
# Check third argument for mask
hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])

plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.imshow(mask,'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0,256])

plt.show()



#print(hist)
#cv2.imshow('hist', hist)

cv2.waitKey(0)
cv2.destroyAllWindows()
