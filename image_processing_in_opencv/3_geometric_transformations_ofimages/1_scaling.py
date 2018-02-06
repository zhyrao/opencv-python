#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-06 23:36:39
# @Author  : Joe
# @Version : 

import numpy as np
import cv2



# Transformations:
	# OpenCV提供了两个变换函数： 
							# cv2.warpAffine()  接受 2x3 的变换矩阵
							# cv2.wrapPerspective() 接受 3x3 的变换矩阵

# Scaling : 缩放
 	# 缩放的本质就是重新改变图像的大小。
 	# OpenCV有一个函数 cv2.resize() 来改变大小
 	# 图片新的大小可以指定特定的大小或者根据缩放比例因子来缩放。
 	# 缩放时候的插值运算也是不同的：
 			# cv2.INTER_AREA
 			# cv2.INTER_CUBIC
 			# cv2.INTER_LINEAR

img = cv2.imread('messi.jpg')

res = cv2.resize(img, None, fx = 0.5, fy = 0.5, interpolation = cv2.INTER_CUBIC)

# OR 
height, width = img.shape[:2]
res1 = cv2.resize(img, (2*width, 2*height), interpolation = cv2.INTER_CUBIC)

cv2.imshow('original img',img)
cv2.imshow('scaled1',res)
cv2.imshow('scaled2',res1)

cv2.waitKey(0)
cv2.destroyAllWindows()