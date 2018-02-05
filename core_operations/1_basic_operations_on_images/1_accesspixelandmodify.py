#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-03 13:32:51
# @Author  : Joe
# @Version : 

import numpy as np
import cv2

# 可以通过行列坐标点来获取某个像素的值：
		# BGR image: 返回一个Blue, Green, Red数组
		# Grayscale image: 返回强度值

img = cv2.imread('logo.png')
px = img[50, 50]
print (px)

# accessing only blue pixel
blue = img[50, 50, 0]
print(blue)

# modify pixel value
img[50, 50] = [255, 255, 255]

cv2.imshow('logo', img)

cv2.waitKey(0)
cv2.destroyAllWindows()


# ***************************************************************  #

# better way to accessing and modifying pixel:

# # accessing red value: 
# img.item(10,10,2)

# # modify rea value
# img.itemset((10,10,2), 100)


#  ************************************************************** #
