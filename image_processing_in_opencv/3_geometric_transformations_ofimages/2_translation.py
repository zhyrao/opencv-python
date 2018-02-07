#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-07 12:37:43
# @Author  : Joe

import numpy as np
import cv2

# Translation：移动物体的位置；
# 如果知道在(x,y)方向的位移，记做：(tx, ty)，则可以创建一个变换矩阵：
# M ：
		# 	1 	0	tx
		# M =
		# 	1 	1	ty

# cv2.warpAffine(src, M, dsize[, dst[, flags[, borderMode[, borderValue]]]]) → dst
# src: 源图像
# M： 变换矩阵
# dsize: size of output image

img = cv2.imread('messi.jpg', 0)
rows, cols = img.shape

M = np.float32([[1,0,100], [0,1,50]])
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('gray', img)
cv2.imshow('translate', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Third argument of the cv2.warpAffine() function is the size
# of the output image, which should be in the form of (width, height). 
#Remember width = number of columns, and height = number of rows.