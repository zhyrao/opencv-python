#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-17
# @Author  : Joe

import numpy as np
import cv2
	

# Bounding Rectangle 包围矩形
# 有两种

	# 1. 横竖型包围矩形 straight bounding rectangle
		# 只是一个横竖型的包围矩形，并没有考虑物体的旋转
		# 所以这个包围矩形的面积并不是最低的。
		# cv2.boundingRect()
		# (x,y)是这个矩形的左上角点坐标 
		# (w,h)是这个矩形的宽和高

	# 2. 旋转后的矩形包围
		# 这里的包围盒是经过旋转后的，面积是最小的。
		# cv2.minAreaRect()
		# 返回值是一个 Box2D 结构的信息包含了一下内容：
			# 左上角坐标点(x,y)
			# 矩形的宽和高(width, height)
			# 矩形的旋转角度
		# 但是要绘制出这个矩形我们需要4个点，这样
		# 就从 cv2.boxPoint() 来获得


img = cv2.imread('rect.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
img_c, contours, hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]

x, y, w, h = cv2.boundingRect(cnt)
img = cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)

rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)

im = cv2.drawContours(img, [box], 0, (0,0,255), 2)


cv2.imshow('rect', img)

cv2.waitKey(0)
cv2.destroyAllWindows()