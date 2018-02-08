#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-07 17:27:53
# @Author  : Joe

import numpy as np
import cv2
from matplotlib import pyplot as plt 

# 放射变换：
	# 在放射变换中，所有在源图像中平行的线条，在变换以后
	# 任然在输出图片中是平行的
	# cv2.getAffineTransform()
	# retval	=	cv.getAffineTransform(	src, dst	)
img = cv2.imread('line.jpg')
rows, cols, chs = img.shape

pts1 = np.float32([[50,50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200,50],[100,250]])

M = cv2.getAffineTransform(pts1, pts2)

dst = cv2.warpAffine(img, M, (cols, rows))

plt.subplot(121), plt.imshow(img),plt.title("Input")
plt.subplot(122),plt.imshow(dst),plt.title('Output')

plt.show()