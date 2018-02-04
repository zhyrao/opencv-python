#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-04 23:43:50
# @Author  : Joe

import numpy as np
import cv2


# 图像基础算法中也包含 与   或   非   异或
# 这些操作对于一些提取图像的某一部分，制定和处理某一些非举行的ROI区域非常有用（速度快？）


# load images
img1 = cv2.imread('messi.jpg')
img2 = cv2.imread('logo.png')

rows, cols, depth = img2.shape
roi = img1[0:rows, 0:cols]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)

img2_fg = cv2.bitwise_and(img2, img2, mask = mask)

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()