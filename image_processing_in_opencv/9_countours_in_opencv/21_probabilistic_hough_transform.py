#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-03
# @Author  : Joe
# @Version : 

import numpy as np
import cv2


# Probabilistic Hough Transform
# 在霍夫变换中，你可以看到即使一条带有两个
# 参数的线，也需要大量的计算。概率霍夫变换
# probabilistic hough transform是上述的
# 霍夫变换的改进版本。它没有把所有的点都进
# 行计算，它仅仅计算这个线的一部分子集点，
# 这样也能满足要求。只是我们必须要降低阈值。
# 如下图，比较了普通霍夫变换和概率霍夫变换
# 的表现
# link:https://opencv-python-tutroals.readthedocs.io/en/latest/_images/houghlines4.png

# 在OpenCV中实现了给予 Robust Detection of Lines
# Using he Progreesive Probabilistic Hough Transform
# 由 Mats, J. Galambos,C. Kittler,J.V..提出

# cv2.HoughLinesP() 
# 含有两个参数
	# minLineLength - 线段长度的最短值。
		# 低于这个长度的线段将被抛弃
	# maxLineGap - 如果两个线段之间的间隙
		#低于这个值，则考虑他们为一条线段

# 这个函数最好的在于，它直接返回所有线段的
# 两个端点。 在上节中，只能得到线段的所有参
# 数信息，自己必须去找到这些点。在这个函数中
# 所有的返回都是简单直接的

img = cv2.imread('sudoku.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize = 3)

minLineLength = 50
maxLineGap = 5

lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength, maxLineGap)

for line in lines:
	x1,y1,x2,y2 = line[0][0], line[0][1], line[0][2], line[0][3]
	cv2.line(img, (x1,y1),(x2,y2), (0,255,0), 1)

cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()