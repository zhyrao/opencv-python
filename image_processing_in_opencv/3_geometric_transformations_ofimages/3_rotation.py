#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-07 16:41:56
# @Author  : Joe

import numpy as np
import cv2


# 将一副图片旋转角度 α 的变换矩阵
# 	|-    cos α    	- sin α  -|
# M =|					|
# 	|-	sin α 	    cos α  -|

#  OpenCV提供了一个可以以任何点左右中心点并且能都缩放的矩阵；
# 这个矩阵可以使用cv2.getRotationMatrix2D()来得到
# retval	=	cv.getRotationMatrix2D(	center, angle, scale	)
# center:	图片中选择的旋转中心点
# angle:		旋转的角度。正值表示顺时针方向
# scale:		缩放量

img = cv2.imread('messi.jpg', 0)
rows, cols = img.shape

M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1) # 中心点顺时针旋转90度，无缩放
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('gray', img)
cv2.imshow('rotation', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()