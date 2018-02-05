#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-03 23:00:17
# @Author  : Joe
# @Version : 

import numpy as np
import cv2
from matplotlib import pyplot as plt 

# 给图片的周围加上边框

# 通常这类函数的参数
	# src - 源图片
	# top, bottom, left, right - 上下左右的边框宽度-像素单位
	# borderType - 指定了何种类型的边框
				# 1 cv2.BORDER_CONSTANT - 不变的彩色边框，宽度由紧跟的参数指定
				# 2 cv2.BORDER_REFLECT 	- 边框会像镜子一样反射附近的像素  fedcba|abcdefgh|hgfedcb
				# 3 cv2.BORDER_REFLECT_101 or cv2.BORDER_DEFAULT gfedcb|abcdefgh|gfedcba  # 注意有一定的损失
				# 4 cv2.BORDER_REPLICATE 复制最近的一个像素内容  aaaaaa|abcdefgh|hhhhhhh
				# 5 cv2.BORDER_WRAP - cdefgh|abcdefgh|abcdefg
	# value - 如果类型是cv2.BORDER_CONSTANT的边框的颜色

BLUE = [255, 0, 0]

img1 = cv2.imread('logo.png')

replicate = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img1, 10,10,10,10,cv2.BORDER_CONSTANT, value = BLUE)

plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.xticks([]),plt.yticks([])
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.xticks([]),plt.yticks([])
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.xticks([]),plt.yticks([])
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.xticks([]),plt.yticks([])
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.xticks([]),plt.yticks([])
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.xticks([]),plt.yticks([])

plt.show()

