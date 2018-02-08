#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-07 23:15:04
# @Author  : Joe
# @Version : 

import numpy as np
import cv2
from matplotlib import pyplot as plt

# 2D Convolution (Image Filtering)
# 对于一维的信号，图像可以被各种各样的 低通滤波器(Low pass Filter, LPF)
# 或者 高通过滤器(high pass Filter, HPF) 进行过滤。
# 通常 低通滤波器 过滤可以帮助除掉图像中的噪点或者能够模糊图像， 高通滤波器 可以帮助检测图像中的边缘轮廓

# OpenCV 提供了方法cv2.filter2D(), 来用一个 核(kernel) 对图像进行卷积运算。
# 例如：我们尝试对图像进行平均过滤 (an averaging filter)。
# 一个 5x5 的平均过滤核可以定义为下面的形式：
	# 		-	1   1	  1   1   1	-
	# 	1	|	1   1	  1   1   1	|
	# K  = -- *|	1   1    1   1   1	|
	# 	25	|	1   1    1   1   1	|
	# 		-	1   1    1   1   1	-

# 操作如下：
	# 对于图像中的每一个像素，以此像素作为中心，分割出一个 5x5 的像素块，
	# 然后将所有的像素块内的像素值加起来，将这个结果 除以 25. 这样相当于
	# 计算出这个像素块内的平均值，然后将这个平均值赋值给中心点的那个像素

img = cv2.imread('opencv.png')

kernel = np.ones((5,5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()