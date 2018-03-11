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


img = cv2.imread('sample.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)

plt.imshow(img),plt.show()