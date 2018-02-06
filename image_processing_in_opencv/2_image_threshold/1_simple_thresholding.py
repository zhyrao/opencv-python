#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-06 15:57:38
# @Author  : Joe

import numpy as np
import cv2
from matplotlib import pyplot as plt 

# Applies a fixed-level threshold to each array element.
# 对于每个数组元素使用一个固定的阈值来检测
# cv2.threshold(src, thresh, maxval, type[, dst]) → retval, dst
	# src: 源图像
	# threshold: 阈值
	# maxvalue: 大于阈值则赋值为maxvalue
	# type: 二值化类型

# 简单阈值检测法：
	# 如果一个像素的值大于阈值，那么就把这个像素赋值给另外一个特定的值（比如白色）；
	# 如果一个像素的值小于阈值，那么就把这个像素赋值给另外一个特定的值（比如黑色）；


img = cv2.imread('Gradient.jpg', 0) 	# 0: grayscale mode
ret, threshold1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, threshold2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, threshold3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, threshold4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, threshold5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original Image', 'BINARA', 'BINARA_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, threshold1,threshold2,threshold3,threshold4,threshold5]

for i in range(6):
	plt.subplot(2,3, i+1), plt.imshow(images[i], 'gray') # show multiple images
	plt.title(titles[i])
	plt.xticks([]),plt.yticks([])	# hide tick mark

plt.show()