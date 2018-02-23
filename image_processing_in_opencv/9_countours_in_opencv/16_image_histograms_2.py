#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-23
# @Author  : Joe

import numpy as np
import cv2
from matplotlib import pyplot as plt 

# Histogram Equalization 直方图均衡化

# Goal 目标
	# 在本节中，我们将学习直方图均衡化的思想并且用它来提高图像的对比度。

# Theory 理论
	# 想象一下，如果一幅图像的所有的像素值都限定在某些特定的区间范围之内。
	# 例如，比较亮的图像中所有的像素值都属于很高的值的范围内（[0-255]都
	# 分布在127以上）。但是一副好的图像中的像素值的取值范围是在整个范围
	# 空间内的([0-255])。所以需要将直方图进行拉伸使其范围为整个值域范围
	# https://opencv-python-tutroals.readthedocs.io/en/latest/_images/histogram_equalization.png
	# 这个过程称为直方图均衡化。通常使用这个方法来对图像进行对比度的提升。

	# http://en.wikipedia.org/wiki/Histogram_equalization
	# 上面这个链接是wiki对直方图均衡化的详细解释。
	# 在这里我们只是使用这个方法。

# 1. Numpy 使用
	# 从直方图中可以看出基本都在较亮的区域内(大约[110-210])
	# 我们需要整个频谱。为了得到完全的值域范围，我们需要将
	# 输入的数据（图像）映射到整个值域范围内([0-255])。
img = cv2.imread('wiki.jpg',0)

hist,bins = np.histogram(img.flatten(),256,[0,256])

cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()

# cdf_m = np.ma.masked_equal(cdf,0)
# cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
# cdf = np.ma.filled(cdf_m,0).astype('uint8')

# img2 = cdf[img]
# hist,bins = np.histogram(img2.flatten(),256,[0,256])

# cdf = hist.cumsum()
# cdf_normalized = cdf * hist.max()/ cdf.max()

plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()