#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-07 22:47:24
# @Author  : Joe
# @Version : 

import numpy as np
import cv2
from matplotlib import pyplot as plt 


# 透视变换
# 对于透视变换，需要一个 3x3 的矩阵。 在透视变换后直线任然保持为直线。
# 为了得到透视变换矩阵，你需要 源图片 上的4个位置点，以及相应的输出图片上的4个位置点。
# 这4个点中，不能有3点及3点以上共线

# cv2.getPerspectiveTransform()

img = cv2.imread('sudokusmall.jpg',)
rows, cols, channels = img.shape

pts1 = np.float32([[56,65], [368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(img, M, (300, 300))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()