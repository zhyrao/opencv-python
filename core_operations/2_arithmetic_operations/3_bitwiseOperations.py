#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-04 23:43:50
# @Author  : Joe

import numpy as np
import cv2


# 图像基础算法中也包含 与   或   非   异或
# 这些操作对于一些提取图像的某一部分，制定和处理某一些非矩形的ROI区域非常有用（速度快？）


# load images
img1 = cv2.imread('messi.jpg')
img2 = cv2.imread('logo.png')

# ROI of logo
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

# get the logo mask
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)
cv2.imshow('bitwise',img1_bg)

img2_fg = cv2.bitwise_and(img2, img2, mask = mask)

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.threshold(src, dst, threshold, maxValue, thresholdType)
# src: input image array
# dst: output image array
# threshold: fixed value to compare with image pixel value
# maxValue: if pixel value is greater than threshold then pixel value = maxvalue
# thresholdType:
				# THRESH_BINARY:    Threshold Binary  
							# 			|- maxValue   if src(x,y) > threshod
							# dst(x,y) = 	|
							# 			|-  0			otherwise
				# THRESH_BINARY_INV:    Threshold Binary, Inverted
							# 			|- 0			 if src(x,y) > threshod
							# dst(x,y) = 	|
							# 			|-  maxvalue 	otherwise
				# THRESH_TRUNC:    Truncate   
							# 			|- threshold  if src(x,y) > threshod
							# dst(x,y) = 	|
							# 			|- src(x,y)	otherwise
				# THRESH_TOZERO:    Threshold to Zero
							# 			|- src(x,y)   if src(x,y) > threshod
							# dst(x,y) = 	|
							# 			|-  0			otherwise
				# THRESH_TOZERO_INV:    Threshold to Zero, Inverted 
							# 			|- 0   		if src(x,y) > threshod
							# dst(x,y) = 	|
							# 			|-  src(x,y) 	otherwise