#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-13
# @Author  : Joe

import numpy as np
import cv2
from matplotlib import pyplot as plt

# 原理
# Canny边缘检测算法是一个被广泛使用的边缘检测算法。
# 它是有Jhon F.Canny 在1986年提出的。
# 它是一个多阶段的算法

# 1. 噪声消除
	# 由于边缘检测法容易受到图像中的噪声的干扰，
	# 那么首先我们要使用一个 5x5 的高斯滤波来消除图像噪声
# 2. 找到图像的强度梯度
	# 对平滑后的图像使用Sobel算子计算水平方向和竖直方向的
	# 一阶导数（图像梯度）（Gx和Gy）。根据得到的这两幅梯度
	# 图找到边界的梯度和方向。
	# 梯度的方向一般总是与边界垂直。梯度方向被归为四类：垂直，水平，和两条对角线。

# 3. 非极大值抑制
	# 在获得梯度的方向和大小之后，应该对整幅图想做一个扫描，
	# 出去那些非边界上的点。对每一个像素进行检查，
	# 看这个点的梯度是不是周围具有相同梯度方向的点中最大的。

# 4. 滞后阀值
	# 现在要确定那些边界才是真正的边界，需要设置两个阀值：
	# minVal和maxVal。当图像的灰度梯度高于maxVal时被认为
	# 是真的边界，那些低于minVal的边界会被抛弃。
	# 如果介于两者之间的话，就要看这个点是否与某个被
	# 确定为真正边界点相连，如果是，就认为它也是边界点，
	# 如果不是就抛弃。

# OpenCV中的Canny边界检测
	# cv2.Canny（）第一个参数是输入图像，第二和第三个分别是minVal和maxVal。
	# 第三个参数设置用来计算图像梯度的Sobel卷积核的大小，默认值为3。
	# 最后一个参数是L2gradient，它可以用来设定求梯度大小的方程。如果设为True，
	# 就睡使用我们上面提到过的方程，否则使用方程：
	# Edge_Gradient(G) = |Gx| + |Gy|
	# 代替，默认值为False。



img = cv2.imread('messi.jpg',0)
edges = cv2.Canny(img,100,180)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()