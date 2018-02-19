#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-19
# @Author  : Joe

import numpy as np
import cv2
	

# 目标：
	# 凸包的缺陷以及如何找到这个
	# 找到一个点到一个多边形的最短距离
	# 匹配不同的形状

# 1. 凸包缺陷
	# 在第二章中我们了解了什么是轮廓的凸包。

	# OpenCV已经提高了一个函数来找到缺陷
	# cv2.convexityDefects()

	# hull = cv2.convexHull(cnt, returnPoints = False)
	# defects = cv2.convexityDefects(cnt, hull)

		# 注意，为了找到凸包缺陷，必须在找凸包的
		# 时候，传入 returnPoints = False

	# 返回了一个数组，这个数组的每行包括了：
	# start point, end point, farthest point,
	# approximate distance to farthest point.
	# 我们可以通过可视化来看到这些信息

img = cv2.imread('star1.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255,0)
img_c,contours,hierarchy = cv2.findContours(thresh,2,1)
cnt = contours[0]

hull = cv2.convexHull(cnt,returnPoints = False)
defects = cv2.convexityDefects(cnt,hull)

for i in range(defects.shape[0]):
    s,e,f,d = defects[i,0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img,start,end,[0,255,0],2)
    cv2.circle(img,far,5,[0,0,255],-1)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()