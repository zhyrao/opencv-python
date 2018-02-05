#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-03 22:46:52
# @Author  : Joe
# @Version : 

import numpy as np
import cv2


# ROI region of image
# 图片是数组格式存储的数据，则可以在图片中的某一块特定（指定的）区域进行操作

img = cv2.imread('logo.png')
print(img.shape)

roi = img[120:130, 124:133]

img[140:150, 133:142] = roi

cv2.imshow('roi', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

