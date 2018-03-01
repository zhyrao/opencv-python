#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-01
# @Author  : Joe

import numpy as np
import cv2
from matplotlib import pyplot as plt

# Why Laplacian is a High Pass Filter?
# 为什么拉普拉斯算子是高频滤波

# 类似的问题在论坛上被问到。问题是为什么拉普拉斯算子、
# Sobel算子等等是高频滤波。对于他们的第一个解释就是
# 通过傅里叶变换。

# simple averaging filter without scaling parameter
mean_filter = np.ones((3,3))

# creating an gaussian filter
x = cv2.getGaussianKernel(5,10)
gaussian = x*x.T

# different edge detection filters 
# scharr in x-direction
scharr = np.array([
	[-3,0,3],
	[-10,0,10],
	[-3,0,3]])

# sobel in x direction
sobel_x = np.array([
	[-1,0,1],
	[-2,0,2],
	[-1,0,1]])

# sobel in y direction
sobel_y = np.array([
	[-1,-2,-1],
	[0,0,0],
	[1,2,1]])

# laplacian
laplacian = np.array([
	[0,1,0],
	[1,-4,1],
	[0,1,0]])

filters = [mean_filter, gaussian, laplacian, sobel_x,sobel_y,scharr]
filter_name = ['mean_filter', 'gaussian','laplacian', 'sobel_x', \
                'sobel_y', 'scharr_x']
fft_filters = [np.fft.fft2(x) for x in filters]
fft_shift = [np.fft.fftshift(y) for y in fft_filters]
mag_spectrum = [np.log(np.abs(z)+1) for z in fft_shift]

for i in range(6):
	plt.subplot(2,3,i+1),plt.imshow(mag_spectrum[i],cmap = 'gray')
	plt.title(filter_name[i]), plt.xticks([]), plt.yticks([])

plt.show()