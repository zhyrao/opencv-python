#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-16
# @Author  : Joe

import numpy as np
import cv2


# 在 cv2.findContour()中，第三个参数
# 是做什么的呢？

# 上次可以知道，轮廓是一个形状的共同
# 强度的边界。 他们存储了这个形状边界
# 的坐标（x,y）。 那么是不是存储了所有的
# 点呢？ 这里就需要引入轮廓近似值的方法

# 如果参数传入为 cv2.CHAIN_APPROX_NONE,
# 那么所有的边界点都会被存储下来。但是在
# 实际情况中我们是不是需要存储所有的点呢？
# 例如，找到的轮廓是一条线段，那么还需要
# 将所有的点都存储下来吗？
# 不，只需要存储线段的两个端点。 这时就是
# 传入 cv2.CHAIN_APPROX_SIMPLE 为参数。
# 这样就会移除多余的点，节约内存开支。

img = cv2.imread('test.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 127, 255, 0)

image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow('contours', image)
cv2.imshow('thresh', thresh)
cv2.imshow('gray', img_gray)

# 绘制轮廓
# cv2.drawContours()

# 绘制所有的轮廓
#img_1 = cv2.drawContours(img.copy(), contours, -1, (0, 255, 0), 1)

#cnt = contours[4]

# 绘制单个轮廓
img_in = cv2.drawContours(img.copy(), contours, -1, (0,0, 255), 1)
#cv2.imshow('contour',img_1)
cv2.imshow('ind_contour', img_in)

print(len(contours))

cv2.waitKey(0)
cv2.destroyAllWindows()