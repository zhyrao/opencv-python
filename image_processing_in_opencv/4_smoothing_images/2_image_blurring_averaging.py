#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-08 10:39:29
# @Author  : Joe

import numpy as np
import cv2
from matplotlib import pyplot as plt 

#图像模糊(图像平滑)
	# 图像模糊(Image blurring/smoothing) 是通过将图像与一个 LPF核 进行卷积得到的结果
	# 通常对于去除图像中的噪点很有用。
	# 实际上，他是去除了图像中高频出线的内容（例如噪点、边缘线等）。（也有模糊技术不会将边缘去除的）

# OpenCV提供了主要4中不同类型的模糊技术

# 1. 平均模糊
	# 原理： 将图像与一个标准化的方形过滤器（kernel）进行卷积计算。
		      # 这里只是简单的把在方形范围内的像素值平均化以后赋值给方形中心点的像素值

# cv2.blur()
# dst = cv.blur(src, ksize[, dst[, anchor[, borderType]]])

# cv2.boxFilter()
# dst = cv.boxFilter(	src, ddepth, ksize[, dst[, anchor[, normalize[, borderType]]]]	)


img = cv2.imread('opencv.png')

blur = cv2.blur(img,(3,3))

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()