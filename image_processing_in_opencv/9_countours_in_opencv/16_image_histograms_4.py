#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-24
# @Author  : Joe

import numpy as np
import cv2


# CLAHE (contrast limited adaptive histogram equalization)
#  有限对比适应性直方图均衡化

# 在原来的直方图均衡化中，我们考虑的是对全局的图像的对比。
# 在很多情况中，这并不是一个好主意。如同链接中的图一样，
# 直方图均衡化以后并不是我们想要的结果
# https://opencv-python-tutroals.readthedocs.io/en/latest/_images/clahe_1.jpg

# 均衡后的图中可以看出后面背景部分的对比度效果确实提升了。但是
# 比较两幅图中的脸部雕塑可以看出，均衡后的脸部雕塑的细节效果因
# 为过度亮的原因大部分都丢失了。这是因为直方图均衡化没有对特定
# 的区域进行运用而是对整个图像。

# 为了解决这个问题，我们使用adaptive histogram equalization。
# 首先，将图像分割为很多大小一样的小块(tiles)，在OpenCV中默认
# 是8x8像素。然后每个小块进行直方图均衡化。这样以来，在这个小块
# 中，直方图会被限制到一个比较小的区域范围内（在没有噪声的情况下）。
# 如果存在噪声，那么这个区域将被放大。为了避免这个情况发生，contrast
# limiting将被使用。如果有任何直方图区间(bin)在制定的对比度限制范围
# 上（在opencv中默认为40），那么这些像素将被裁减并且会在均衡化之前
# 被均匀分布给其他的区间。

img = cv2.imread('tsukuba.jpg',0)

# create a CLAHE object
clahe = cv2.createCLAHE(clipLimit = 2.0, tileGridSize=(4,4))
cl1 = clahe.apply(img)

cv2.imshow('original',img)
cv2.imshow('equalized',cl1)

cv2.waitKey(0)
cv2.destroyAllWindows()