#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-05 16:49:47
# @Author  : Joe

import numpy as np
import cv2


# 如果将图片的色彩空间转换到另一种色彩空间，例如： BGR <-> Gray  BGR <-> HSV

# cv2.cvtColor()  # 将一个图像从一种色彩空间转换到另外一种
	# cvtColor(src, code[, dst[, dstCn]]) → dst
			# src: 源图像
			# code: 色彩空间转换码
					# RGB <-> GRAY: COLOR_BGR2GRAY, COLOR_RGB2GRAY, COLOR_GRAY2BGR, COLOR_GRAY2RGB
					# RGB <-> HSV: COLOR_BGR2HSV, COLOR_RGB2HSV, COLOR_HSV2BGR, COLOR_HSV2RGB
					# RGB <-> YCC:
					# RGB <-> HLS:
					# RGB <-> CIE L*b*b*
					# RGB <-> CIE L*u*v*
					# Bayer <-> RGB:
	# 总共有150多种色彩空间转换方式，大量使用的两个: RGB <-> GRAY  RGB <=> HSV
	# flag: cv2.COLOR_BGR2GRAY 		cv2.COLOR_BGR2HSV
	# 在终端获取所有编码的方法：
		# 	>>> import cv2
		# 	>>> flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
		# 	>>> print flags

# cv2.inRange()

img = cv2.imread('messi.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('original', img)
cv2.imshow('gray', img_gray)
cv2.imshow('hsv', img_hsv)

cv2.waitKey(0)
cv2.destroyAllWindows()

# 对于HSV色彩空间，Hue区间为[0, 179], Saturation 范围是[0. 255], Value范围是[0,255]