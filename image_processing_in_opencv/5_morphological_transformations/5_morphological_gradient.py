#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-10 23:39:05
# @Author  : Joe
# @Version : 

import numpy as np
import cv2

# 类似一个物体的轮廓线

img = cv2.imread('j.png')
kernel = np.ones((5,5), np.uint8)

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

cv2.imshow('original',img)
cv2.imshow('gradient',gradient)

cv2.waitKey(0)