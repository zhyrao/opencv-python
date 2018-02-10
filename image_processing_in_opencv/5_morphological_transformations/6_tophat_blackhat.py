#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-10 23:41:32
# @Author  : Joe
# @Version : 

import numpy as np
import cv2


# TOP HAT
# 源图像和经过Opening之后的图像的区别

# Black Hat
# 源图像和经过closing之后的图像的区别

img = cv2.imread('j.png')
kernel = np.ones((11,11), np.uint8)

tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow('original',img)
cv2.imshow('tophat',tophat)
cv2.imshow('blackhat',blackhat)

cv2.waitKey(0)