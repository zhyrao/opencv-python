#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-07
# @Author  : Joe
# @Version : 

import numpy as np
import cv2


# Harris Corner Detection 

# Goal
	# 在本节中，我们将理解 harris corner detection算法
	# cv2.cornerHarris(). cv2.cornerSubPix()

# Theory
	# 在上章中，角点(corner)就是那些在不同方向局部移动会
	# 导致强度信息产生巨大变化的区域。较早尝试找到这些角点
	# 的是在1988年由 Chris Harris 和Mike Stephens 在论
	# 文 A Combined Corner And Edge Detector中提出。
	# 详细推导过程请google。


# Harris Corner Detector in OpenCV
	# OpenCV含有一个函数来找到角点, cv2.cornerHarris()
	# 它的参数如下：
		# img  -- 源图像，灰度图，数据类型为float32
		# blockSize -- 角点检测考虑的周围像素的范围
		# ksize -- Sobel算子使用的参数
		# k -- 方程中的自由参数


filename = 'chessboard.png'
img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

dst = cv2.dilate(dst, None)
print(dst>0.01)

img[dst>0.01 * dst.max()] = [0,0,255]

cv2.imshow('dst',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
