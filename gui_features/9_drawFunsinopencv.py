#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-02
# @Author  : Joe
# @Version : 

import numpy as np
import cv2

# cv2.line()  			#(img, pt1, pt2, color, thickness=1, lineType=8, shift=0) → None
# cv2.circle()			#(img, center, radius, color, thickness=1, lineType=8, shift=0) → None
# cv2.rectangle()		#(img, pt1, pt2, color, thickness=1, lineType=8, shift=0) → None
# cv2.ellipse()			#(img, center, axes, angle, start_angle, end_angle, color, thickness=1, lineType=8, shift=0) → None
# cv2.putText()			#(img, text, org, font, color) → None

# common arguments:
	# img: 在哪个图片上绘制
	# color: 几何形状的颜色。 如果是BGR，传入一个元组(tuple): (255,0,0). 如果是灰度图则传入单个缩放量
	# thickness: 线条的粗细 像素单位  （如果是闭合类型的图形--圆、巨型， 传入-1是填充整个图形）
	# lineType: 线条的类型例如：8-连接、抗锯齿等

# create a black image
img = np.zeros((512, 512, 3), np.uint8)

# draw a blue line
img = cv2.line(img, (0,0), (511, 511), (255,0,0), 3)

# draw a rectangle
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

# draw a circle
img = cv2.circle(img, (200, 143), 55, (0, 0, 255), -1)

# draw a ellipse
img = cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)

# draw a polygon
pts = np.array([[10, 5], [20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1, 1, 2))
img = cv2.polylines(img, [pts], True, (0,255,255)) #(img, polys, is_closed, color, thickness=1, lineType=8, shift=0) → None

# add text on image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "OpenCV", (10, 300), font, 4, (25, 255, 255), 2, cv2.LINE_AA)


# show image
cv2.imshow('draw', img)
cv2.waitKey(0)

# release stuff
cv2.destroyAllWindows()