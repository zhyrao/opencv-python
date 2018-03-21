#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-20
# @Author  : Joe

import numpy as np
import cv2 as cv


# Dense Optical Flow in OpenCV
	# lucas-kanade方法是为了计算稀疏特征点集（在例子中，特征点
	# 是采用SHI-TOMASI算法）。OpenCV也提供了另外一种可以计算较
	# 稠密的光流点集。它为图像中的所有点都计算了光流。这个算法是
	# 基于2003年由Gunner Farneback提出的"Two-Frame Motion Estimation
	# Based On Polynomial Expansion"中的Gunner Farneback算法。

	# 下面的例子显示了怎么使用上述的算法来找到稠密的光流。我们有
	# 个2个通道的数组，里面是光流向量(u,v)。我们找到他们的方向和
	# 长度。为了更好的显示，我们将结果颜色化。
cap  = cv.VideoCapture('vtest.avi')

ret,frame1 = cap.read()
prvs = cv.cvtColor(frame1,cv.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[...,1]=255

while (1):
	ret, frame2 = cap.read()
	if ret == False:
		break
	next = cv.cvtColor(frame2,cv.COLOR_BGR2GRAY)

	flow = cv.calcOpticalFlowFarneback(prvs, next, None, 0.5, 5, 20, 3, 5, 1.2, 0)

	mag, ang = cv.cartToPolar(flow[...,0], flow[...,1])
	hsv[...,0] = ang*180/np.pi/2
	hsv[...,2] = cv.normalize(mag,None,0,255,cv.NORM_MINMAX)
	bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)

	cv.imshow('frame2', bgr)
	k = cv.waitKey(30) & 0xff
	if k == 27:
		break
	elif k == ord('s'):
		cv.imwrite('opticalfb.png',frame2)
		cv.imwrite('opticalhsv.png',bgr)

	prvs = next

cv.destroyAllWindows()
cap.release()