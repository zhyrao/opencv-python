#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-08 15:56:50
# @Author  : Joe

import numpy as np
import cv2
from matplotlib import pyplot as plt

# Bilateral Filtering
#  dst = cv.bilateralFilter(src, d, sigmaColor, sigmaSpace[, dst[, borderType]])

# 双边滤波
# 我们可以看到，前面的几个滤波模糊方式会模糊图像的边缘。
# 但是在双边滤波上我们可以在去除噪声的情况下保住图像的边缘
# 速度慢

def nothing(x):
	print(x)

img = cv2.imread('lena.jpg')
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

rows, cols, chs = img.shape

print(rows, cols)

cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)

cv2.createTrackbar('dSize', 'image', 0, 255, nothing)
cv2.createTrackbar('sigmaColor','image', 0, 255, nothing)
cv2.createTrackbar('sigmaSpace', 'image', 0, 255, nothing)

while  True:
	d = cv2.getTrackbarPos('dSize','image')
	sc = cv2.getTrackbarPos('sigmaColor', 'image')
	ss = cv2.getTrackbarPos('sigmaSpace', 'image')

	blur_bilateral = cv2.bilateralFilter(img,d, sc, ss)

	cv2.imshow('image', blur_bilateral)
	cv2.imshow('Original', img)
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
        		break

cv2.destroyAllWindows()

# blur_gaussian = cv2.GaussianBlur(img, (5,5), 0)
# blur_average = cv2.blur(img, (5,5))
# blur_median = cv2.medianBlur(img, 3)
# blur_bilateral = cv2.bilateralFilter(img, 9, 75, 75)

# plt.subplot(231),plt.imshow(img),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(232),plt.imshow(blur_gaussian),plt.title('Gaussian Blurred')
# plt.xticks([]), plt.yticks([])
# plt.subplot(233),plt.imshow(blur_average),plt.title('Averaging Blurred')
# plt.xticks([]), plt.yticks([])
# plt.subplot(234),plt.imshow(blur_median),plt.title('Median Blurred')
# plt.xticks([]), plt.yticks([])
# plt.subplot(235),plt.imshow(blur_bilateral),plt.title('Bilateral  Blurred')
# plt.xticks([]), plt.yticks([])
# plt.show()	