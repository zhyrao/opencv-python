#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-03 13:59:40
# @Author  : Joe
# @Version : 

import numpy as np
import cv2


# 图片的属性包含： 行数、列数、通道数、图片数据的类型、总共的像素数量等

# img.shape 
# 返回一个包括图片行数、列数、通道数的元组
		# 如果是灰度图则只返回行列数

# img.size
# 返回图片的总共像素数量 
		# 色彩图等于 行数*列数*通道数
		# 灰度图等于 行数*列数

# img.dtype
# 返回图片的数据类型
		# img.dtype is very important while debugging because a large number of errors in OpenCV-Python code is caused by invalid datatype.


img = cv2.imread('logo.png')
print (img.shape)
print (img.size)
print (img.dtype)

cv2.imshow('logo', img)
cv2.waitKey(0)
cv2.destroyAllWindows()