#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-24
# @Author  : Joe

import numpy as np
import cv2
from matplotlib import pyplot as plt

# Plotting 2D Histograms
# 绘制2D直方图

# 方法1. 使用cv2.imshow()
	# 结果是一个2维的数组。所以可以使用cv2.imshow()
	# 来显示。只不过是一个灰度图，并且不是很明显的能
	# 看出效果。

# 方法2. 使用matplotlib
	# 我们可以使用matplotlib.pyplot.imshow()函数来
	# 绘制不同颜色空间的2d直方图。能够显示出明显的像素
	# 的不同强度。

img = cv2.imread('home.jpg')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
hist = cv2.calcHist( [hsv], [0, 1], None, [180, 256], [0, 180, 0, 256] )

plt.imshow(hist,interpolation = 'nearest')
plt.show()