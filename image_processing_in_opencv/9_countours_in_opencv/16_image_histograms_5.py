#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-24
# @Author  : Joe

import numpy as np
import cv2


# 2D HistogramS
# 二位直方图

# Goal 
	# 在本节中，我们将学习如果找到并且绘制
	# 二位直方图。这对后续的章节很有用

# Introduction 
	# 在第一节中，我们计算并且绘制了一维直方图。
	# 之所以被称为一维直方图是因为我们只是考虑
	# 一个特征，如每个像素的灰度强度。但是在二维
	# 直方图中，我们将考虑两个特征。通常被用来
	# 对色彩图进行计算图像中每个像素的的
	# Hue&Saturation。

# 2D Histogram in OpenCV
	# 在opencv中很简单，依然使用calcHist()。对
	# 于色彩图，我们需要将它从BGR转换到HSV模式。
	# （记住在1D中我们将BRG转换为Grayscale）。
	# 在2D直方图中，函数的参数将修改为下：
		# channesl=[0,1] 因为我们需要处理H和S
		# bins=[180,256] 180是H的值域，256是S的值域
		# range=[0,180,0,256]

img = cv2.imread('tower.jpg')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

hist1 = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
print(hist1)
cv2.imshow('hist1',hist1)
# 2D Histogram in Numpy
	# 在Numpy中也提供了特定的函数: 
		# np.histogram2d()
		# 第一个参数是H数据，第二个是S数据，
		#第三个是区间个数, 第四个是区间范围
		
# img = cv2.imread('tower.jpg')
# hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

hist2, xbins, ybins = np.histogram2d(hsv[0].ravel(),hsv[1].ravel(),[180,256],[[0,180],[0,256]])
print(hist2)
cv2.imshow('hist2',hist2)

cv2.waitKey(0)
cv2.destroyAllWindows()