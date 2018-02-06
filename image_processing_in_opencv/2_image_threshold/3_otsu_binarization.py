#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-06 23:01:46
# @Author  : Joe
# @Version : 

import numpy as np
import cv2
from matplotlib import pyplot as plt 

# Otsu's Binarization OTSU 二值化
# cv2.threshold() -> 返回两个值，其中一个是retval,这个返回值可以在OTSU二值化的时候使用
# 在全局的阈值检测中，通常我们使用一个比较随便的值来作为阈值。 但是我们如何知道这个阈值是好的阈值还是不是呢？
# 答案就是：试错法
# 但是在一个双峰图像中（简单来说，双峰图像就是指这种图像的直方图是有两个峰值），我们可以估计阈值在两个峰值的中间。
# 这就是OTSU的作用：可以为直方图是双峰图的图像自动计算它的阈值。
# 对于那些不是双峰的图像，二值化不会很精确

img = cv2.imread('noise.jpg',0)

# global thresholding
ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# otsu's binarization
ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Otsu's thresholding after gaussian filtering
blur = cv2.GaussianBlur(img, (5,5), 7)
ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

images = [img, 0, th1,
		  img, 0, th2,
		  blur, 0, th3]

titles = ['Original Noise Image', 'Histogram', 'Global Thresholding v= 127',
		  'Original Noisy Image', 'Histogram', "Otus's Thresholding",
		  'Gaussian filtered Image', 'Histogram', "OTSU's Thresholding"]

for i in range(3):
	plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
	plt.title(titles[i*3]),plt.xticks([]),plt.yticks([])
	plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
	plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
	plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
	plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()