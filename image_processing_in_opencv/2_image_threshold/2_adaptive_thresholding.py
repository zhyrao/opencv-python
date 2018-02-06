#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-06 22:27:32
# @Author  : Joe
# @Version : 

import numpy as np
import cv2
from matplotlib import pyplot as plt 


# 上次的简单阈值法中我们采用了公开的唯一的一个阈值来对整个图片进行检查。 
# 但是这样对于图片中的一些不同的光照条件下的局域不一定是好的方法。
# 这样以来，我们采用 自适应的阈值分割。 这种方法中，由算法来对图片中的一小块局域计算出该局域的阈值。
# 这样我们就能对图片中光照不同的局域分别计算得到不同的阈值来进行阈值分割。

# cv2.adaptiveThreshold()
	# 这个函数有3个“特别”的参数，并且只有一个返回值
	# 1: Adaptive Method  -- 这个参数决定了阈值是怎么计算的
			# cv2.ADAPTIVE_THRESH_MEAN_C: 阈值是附近区块的平均值
			# cv2.ADAPTIVE_THRESH_GAUSSIAN_C: 阈值是附近值的加权和，权重是一个高斯窗口（？？？）
					# threshold value is the weighted sum of neighbourhood values where weights are a gaussian window.
	# 2: Block Size: 决定邻近区域的大小
	# 3: C: 只是一个常量值，用来对平均值或者权重值进行消减

img = cv2.imread('keyboard.JPG', 0)
img = cv2.medianBlur(img, 5)

ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,\
	cv2.THRESH_BINARY, 15, 2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
	cv2.THRESH_BINARY, 15, 2)

titles =['Original Image', 'Global threshold', 'Adaptive Mean threshold', 'Adaptive Gaussian threshold']
images = [img, th1,th2,th3]

for i in range(4):
	plt.subplot(2,2,i+1), plt.imshow(images[i], 'gray')
	plt.title(titles[i])
	plt.xticks([]),plt.yticks([])

plt.show()