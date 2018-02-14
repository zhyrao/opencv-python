#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-14
# @Author  : Joe

import numpy as np
import cv2


# 图像金字塔的高层的图像(低分辨率)是通过将
# 底层的图像（高分辨率）中连续的去处行和列
# 的像素得到的。 高层图像的每个像素值为底层
# 图像中的5个像素的高斯权重所分配。

# 这样一来，一个 M X N 大小的图像就变成了
# M/2 X N/2 大小的图像。 整个图像为原始图像
# 的 1/4 大小。 这种方式叫做Octave。连续这样
# 的操作，我们就会得到一个分辨率不断下降的图
# 像金字塔。

# 可以使用函数cv2.pyrDown()和cv2.pyrUp()构
# 建图像金字塔。

# cv2.pyrDown从一个高分辨率大尺寸的图像向上构建一个金字塔（尺寸变小，分辨率降低）
# cv2.pyrUp从一个低分辨率小尺寸的图像向上构建一个金字塔（尺寸变大，但分辨率不会增加）

img = cv2.imread('messi.jpg')

lower_reso = cv2.pyrDown(img)
high_reso = cv2.pyrUp(img)
high_reso1 = cv2.pyrUp(lower_reso)

cv2.imshow('lower_reso', lower_reso)
cv2.imshow('original', img)
cv2.imshow('high_reso', high_reso)
cv2.imshow('high_reso1', high_reso1)

cv2.waitKey(0)
cv2.destroyAllWindows()

# 注意：
	# 要记住的是higher_reso1和 img 是不同的。因为一旦使
	# 用cv2.pyrDown图像的分辨率就会降低，信息就会被丢失。