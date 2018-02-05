#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-05
# @Author  : Joe

import numpy as np
import cv2

# normally the performance of a function is to measure time they take
# cv2.getTickCount()
# cv2.getTickFrequency
img = cv2.imread('messi.jpg')

e1 = cv2.getTickCount()

for i in range(5,49,2):
	img = cv2.medianBlur(img, i)
e2 = cv2.getTickCount()
elapsedTime = (e2 - e1)/cv2.getTickFrequency()

print (cv2.useOptimized())
print(elapsedTime)

# Note: 可以使用time模块中的 time.time()函数来获取时间



# cv2.useOptimized() 
		# 检查是否当前优化的状态
# cv2.setOptimized()
		# 设置是否是否opencv的优化


# Measuring Performance in IPython

# IPython 提供了一个测试性能的指令： %timeit


# 性能优化技术：
	# 1：避免使用loop循环，特别是嵌套2-3层loop循环
	# 2：Vectorize the algorithm/code to the maximum possible extent because Numpy and OpenCV are optimized for vector operations.
	# 3：Exploit the cache coherence.
	# 4：Never make copies of array unless it is needed. Try to use views instead. Array copying is a costly operation.