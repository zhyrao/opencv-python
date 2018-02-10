#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-10 23:34:17
# @Author  : Joe
# @Version : 

import numpy as np
import cv2

# Closeing 
# 是Opening的相反表现。 
# 先扩张后腐蚀
# 处理一些小的黑点问题

img = cv2.imread('j2.png')
kernel = np.ones((5,5), np.uint8)

close  = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imshow('original',img)
cv2.imshow('close',close)

cv2.waitKey(0)