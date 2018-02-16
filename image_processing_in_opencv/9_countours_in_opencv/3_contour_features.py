#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-16
# @Author  : Joe

import numpy as np
import cv2


# 目标：
		# 找到轮廓的不同特征，例如面积，周长，中心点，包围盒等等
		# 很多相关的接口函数

# 1 Moments 矩
	# 图像矩可以帮助我们计算很多图像的特征点，
	# 例如，物体的重心，物体的面积等等。

	# cv2.moments()
	# 返回一个包含所有计算出来矩的字典


img = cv2.imread('star.jpg', 0)
ret, thresh = cv2.threshold(img, 127, 255, 0)
img_c, contours, hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]
M = cv2.moments(cnt)
print (M)

# 从这些数据中就可以找到这个图像的中心
# Cx = M10/ M00
# Cy = M01/ M00

cx = int(M['m10']/M['m00'])

cy = int(M['m01']/M['m00'])

print(cx, cy)

# Contour Area 面积
# 面积是通过 cv2.contourArea()或者矩里面的m00 得到的
area = cv2.contourArea(cnt)
print(area)

# Contour Perimeter 周长
# 也被称为弧长 arc length.
# 可以通过函数 cv2.arcLength()得到，第二个参数
# 可以特别指定为 True 如果轮廓是闭合的，否则
# 如果是一条曲线，则为False

perimeter = cv2.arcLength(cnt, True)
print(perimeter)