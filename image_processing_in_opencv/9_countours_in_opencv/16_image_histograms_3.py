#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-24
# @Author  : Joe

import numpy as np
import cv2


# OpenCV也提供了直方图均衡化的函数接口
# cv2.equalizeHist()
# 它接收一个灰度图作为输入，返回一个完成
# 直方图均衡化的图像

img = cv2.imread('wiki.jpg',0)
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
cv2.imwrite('res.png',res)

cv2.imshow('result', res)

cv2.waitKey(0)
cv2.destroyAllWindows()


# 直方图均衡化对于图像局限于一个特定的区域有非常好的
# 效果。但是它对于拥有大范围像素值域的图像的作用不大，
# 请参考SOF
# Link：http://stackoverflow.com/questions/10549245/how-can-i-adjust-contrast-in-opencv-in-c
# http://stackoverflow.com/questions/10561222/how-do-i-equalize-contrast-brightness-of-images-using-opencv