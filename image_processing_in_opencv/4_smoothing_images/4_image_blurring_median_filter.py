#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-08 11:05:45
# @Author  : Joe

import numpy as np
import cv2
from matplotlib import pyplot as plt 

# Median Filtering
# 中位值模糊	
	# 在中位值模糊中，计算出内核范围内的像素值的中位值，
	# 然后将内核中心点的像素值赋值为这个中位值
	# 这个方法对于移除 salt-and-pepper 噪声特别有效
	# 值得注意的是，对于高斯模糊或者块模糊，模糊后的值也许在原
	# 图像中是不存在的（计算出来的），但是对于中位值模糊来说，
	# 模糊值就是图片中的某一个像素值（对于范围内的像素值只是做了统计）。
	# 这样消除噪声是非常快。
	# 内核的范围值必须是正奇数


img = cv2.imread('saltpepper.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

blur_gaussian = cv2.GaussianBlur(img, (5,5), 0)
blur_average = cv2.blur(img, (5,5))
blur_median = cv2.medianBlur(img, 5)

plt.subplot(221),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(blur_gaussian),plt.title('Gaussian Blurred')
plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(blur_average),plt.title('Averaging Blurred')
plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(blur_median),plt.title('Median Blurred')
plt.xticks([]), plt.yticks([])
plt.show()	