#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-08 10:53:38
# @Author  : Joe

import numpy as np
import cv2
from matplotlib import pyplot as plt 

# Gaussian Filtering
# 高斯模糊
	# 在高斯模糊中，采用高斯内核 作为过滤器的相关系数。
	#  高斯滤波是将输入数组的每一个像素点与 高斯内核 卷积将卷积和当作输出像素值。

# cv2.GaussianBlur()
# dst = cv.GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]])
		# 我们需要指定 高斯内核  的宽和高（都必须是正值并且是奇数）
		# 同时也需要也需要指定在x,y方向上的偏差， sigmaX 和 sigmaY；
		# 如果只有sigmaX给出了，那么sigmaY就等于sigmaX
		# 如果都是0，那么他们会从 内核 的大小计算得出

# 高斯模糊是对于消除高斯噪声的一种非常有效的方式


img = cv2.imread('opencv.png')

blur = cv2.GaussianBlur(img, (5,5), 0)
blur2 = cv2.blur(img, (5,5))

plt.subplot(131),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(blur),plt.title('Gaussian Blurred')
plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(blur2),plt.title('Averaging Blurred')
plt.xticks([]), plt.yticks([])
plt.show()