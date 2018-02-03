#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-03 22:51:36
# @Author  : Joe
# @Version : 

import numpy as np
import cv2


# cv2.split()  (src, dst0, dst1, dst2, dst3) → None
# cv2.merge()  (src0, src1, src2, src3, dst) → None

# 色彩图的中各种单色通道可以被分割出来，可以将不同的通道的内容融合起来

img = cv2.imread('logo.png')

b,g,r = cv2.split(img)

z = np.zeros((img.shape[0], img.shape[1], 1), np.uint8) # all 0

merge_img1 = cv2.merge((b,g, z))

cv2.imshow('test', merge_img1)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Note: cv2.split() 是一个非常消耗的运算，慎用！ numpy的运算速度非常快，尽可能的采用numpy进行运算