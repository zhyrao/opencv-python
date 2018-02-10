#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-10 23:30:33
# @Author  : Joe
# @Version : 

import numpy as np
import cv2


# cv2.morphologyEx(src, op, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]]) → dst

# Opening 
# 这个是先腐蚀后扩张的联合体

img = cv2.imread('j1.png')
kernel = np.ones((5,5), np.uint8)

opening  = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

cv2.imshow('original',img)
cv2.imshow('opening',opening)

cv2.waitKey(0)