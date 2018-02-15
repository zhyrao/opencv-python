#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-15
# @Author  : Joe

import numpy as np
import cv2

# cv2.findContours()
	# 参数： 
			# 1. 原图像
			# 2. 轮廓检索模型
			# 3. 轮廓近似值方法
	# 返回值：
			# 1. 原图像
			# 2. 轮廓（是一个python list，包含所有的轮廓）
			# 3. 层次
img = cv2.imread('messi.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 127, 255, 0)

image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow('contours', image)
cv2.imshow('thresh', thresh)
cv2.imshow('gray', img_gray)

# 绘制轮廓
# cv2.drawContours()

# 绘制所有的轮廓
#img_1 = cv2.drawContours(img.copy(), contours, -1, (0, 255, 0), 1)

#cnt = contours[4]

# 绘制单个轮廓
img_in = cv2.drawContours(img.copy(), contours, -1, (0,0, 255), 1)
#cv2.imshow('contour',img_1)
cv2.imshow('ind_contour', img_in)

print(len(contours))

cv2.waitKey(0)
cv2.destroyAllWindows()