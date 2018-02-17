#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-17
# @Author  : Joe

import numpy as np
import cv2


# Contour Approximation
# 将一个轮廓形状 近似成为另外一个 更少的点组成的
# 形状。 其中的精度由我们自己指定。

# 假设需要在一副图像中找到一个矩形，但是由于
# 图像中的某些问题，不能够直接找到一个很‘完美’的
# 矩形，而是一个‘坏’的形状。在这种情况下就可以用
# 近似值 函数来得到这个形状。



img = cv2.imread('star.jpg', 0)
ret, thresh = cv2.threshold(img, 127, 255, 0)
img_c, contours, hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]

epsilon = 0.1 * cv2.arcLength(cnt, True)
approx = cv2.approxPolyDP(cnt, epsilon, True)

cv2.imshow('original', img)
cv2.imshow('thresh', thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()