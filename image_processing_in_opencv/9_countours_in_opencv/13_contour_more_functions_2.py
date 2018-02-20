#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-20
# @Author  : Joe

import numpy as np
import cv2

# Match Shapers
# 形状匹配

# 在OpenCV中提供了一个函数， cv2.matchShapes()
# 可以对两个物体，或者两个轮廓进行对比，返回一个
# 有关两个对比物体的相似程度值。 
# 这个值越低，表示两个物体越相似。
# 是在 hu-moment 值的基础上计算的。


img1 = cv2.imread('star.jpg',0)
img2 = cv2.imread('star1.jpg',0)

ret, thresh = cv2.threshold(img1, 127, 255,0)
ret, thresh2 = cv2.threshold(img2, 127, 255,0)
img_c,contours,hierarchy = cv2.findContours(thresh,2,1)
cnt1 = contours[0]
img_cc,contours,hierarchy = cv2.findContours(thresh2,2,1)
cnt2 = contours[0]

ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
print (ret)