#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-24
# @Author  : Joe

import numpy as np
import cv2
from matplotlib import pyplot  as plt 


# Goal 
	# 学习直方图反向投影

# Theory
	# 由 Michael J.Swain, Dana H.Ballard在他们的
	# 论文Indexing via color histograms中提出

	# 简单理解：通常在图像分割或者在图像中找到目标
	# 物体中应用。简单来说，它创建了一副和原图想一
	# 样大小的、单通道的数据，每个像素中存储了该像
	# 素属于目标物体的可能性。再简单点来说，输出的
	# 图像中，感兴趣物体的颜色比其他的颜色更白一些。
	# 直方图反向投影用于 camshift 算法等

	# 怎么使用：我们创建一副感兴趣图像的直方图。这个
	# 兴趣物体尽可能的填满整个感兴趣图像。对比灰度直
	# 方图，更倾向于使用色彩直方图是因为灰色图仅仅含
	# 有强度值而色彩直方图拥有更多的信息来定义这个感
	# 兴趣的物体。然后我们再将直方图反向投影到原图像，
	# 换句话说，我们计算目标图像中每个像素在感兴趣图
	# 像中的可能性。

# Numpy 算法
	# 1.首先我们计算源图像和目标图像的彩色直方图。
		# import cv2
		# import numpy as np
		# from matplotlib import pyplot as plt

		# #roi is the object or region of object we need to find
		# roi = cv2.imread('rose_red.png')
		# hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

		# #target is the image we search in
		# target = cv2.imread('rose.png')
		# hsvt = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)

		# # Find the histograms using calcHist. Can be done with np.histogram2d also
		# M = cv2.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256] )
		# I = cv2.calcHist([hsvt],[0, 1], None, [180, 256], [0, 180, 0, 256] )
	# 2.计算比值R = M/I。然后反向投影R，根据R这个调色板
		# 创建新图像，每一个像素代表这个点事目标的概率。
		# 例如，B(x,y)=R[h(x,y),s(x,y)，其中H为点(x,y)
		# 的色调（hue）值，s为点（x,y）的饱和度（saturation）。
		# 最后加入条件B(x,y)=min([B(x,y),1]

		# h,s,v = cv2.split(hsvt)
		# B = R[h.ravel(),s.ravel()]
		# B = np.minimum(B,1)
		# B = B.reshape(hsvt.shape[:2])
	# 3.应用圆盘卷积， B = D * B，在这里D是卷积核
		#disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
		# cv2.filter2D(B,-1,disc,B)
		# B = np.uint8(B)
		# cv2.normalize(B,B,0,255,cv2.NORM_MINMAX)

	# 4.输出图像中灰度最大的地方就是目标位置。
		#如果要找的是一个区域，可以使用一个阈值
		# 对图像二值化，这样能得到不错的结果。
		# ret,thresh = cv2.threshold(B,50,255,0)


# OpenCV 算法
	# OpenCV提供了一个内置的函数 cv2.calcBackProject(),
	# 参数基本与cv2.calcHist()一致。其中的一个参数是一个
	# 我们想要查找到的目标物体的直方图。当然，在使用目标直
	# 方图反向投赢钱应该进行归一化处理。返回结果是一个概率
	# 图像，然后进行圆盘形状卷积操作，再二值化。

roi = cv2.imread('target.jpg')
hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

target = cv2.imread('messi.jpg')
hsvt = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)

# calculating object histogram
roihist = cv2.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256] )

# normalize histogram and apply backprojection
cv2.normalize(roihist,roihist,0,255,cv2.NORM_MINMAX)
dst = cv2.calcBackProject([hsvt],[0,1],roihist,[0,180,0,256],1)

# Now convolute with circular disc
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
cv2.filter2D(dst,-1,disc,dst)

# threshold and binary AND
ret,thresh = cv2.threshold(dst,50,255,0)
thresh = cv2.merge((thresh,thresh,thresh))
res = cv2.bitwise_and(target,thresh)

#res = np.vstack((target,thresh,res))
#cv2.imwrite('res.jpg',res)

cv2.imshow('original', target)
cv2.imshow('thresh', thresh)
cv2.imshow('result', res)

cv2.waitKey(0)
cv2.destroyAllWindows()