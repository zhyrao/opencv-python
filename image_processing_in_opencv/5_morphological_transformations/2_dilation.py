#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-10 23:23:15
# @Author  : Joe
# @Version : 

import numpy as np
import cv2

# Dilation 扩张
# 腐蚀的相反表现。
# 一个像素的所在的内核范围里的值为1，那么这个像素的值就为1.
# 这样就会增加白色区域或者前景物体的宽度。
# 通常的情况是一般我们先腐蚀，因为腐蚀可以消除掉白色噪声，
# 但是得到的结果是变窄了或者变小了，所以我们进行扩张操作。
# 这样以来我们的白色区域增加了，但是白色噪声却不会再出现。

# 也对连接一个物体的零散部件有用处
# cv2.dilate(src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]]) → dst


img = cv2.imread('j.png')
kernel = np.ones((5,5), np.uint8)

erosion = cv2.erode(img, kernel, iterations = 1)

dilation = cv2.dilate(erosion,kernel,iterations = 1)

cv2.imshow('original', img)
cv2.imshow('erosion',erosion)
cv2.imshow('dilation',dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()