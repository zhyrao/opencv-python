#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-11
# @Author  : Joe
# @Version : 

import numpy as np
import cv2
from matplotlib import pyplot as plt

# Goal
	# 学习另外另外一个角点检测方法：Shi-Tomasi Corner Detector
	# cv2.googFeaturesToTrack()

# Theory 
	# 在上节中，我们学习了harris角点算法。后来在1994年， J.Shi 
	# 和 C. Tomasi在他们的论文 Good Features to Track中做了
	# 一些小小的更改，但是会比harris角点检测得到更好的结果。在
	# harris角点检测中使用了 
		# R = λ1 * λ2 - k * (λ1 + λ2)^2

	# 而在shi - tomas中提出了
		# R = min(λ1, λ2)

	# 如果这个值比阈值高，那么就会被认为是一个角点

# Code
	# OpenCV中有函数 cv2.goodFeaturesToTrack(). 它通过shi-tomas
	# 方式（或者特别指定harris方式）在图像中找到N个最强强度的角点。
	# 跟通常一样，输入图像是灰度图。然后指定想要找到的角点的数量。再
	# 指定质量水平，0-1之间的值，这个值表示如果角点的质量水平值小于
	# 这个值将都会被拒绝。最后在指定角点之间的最小欧几里得距离值。
	

img = cv2.imread('sample.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)

plt.imshow(img),plt.show()