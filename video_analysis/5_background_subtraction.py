#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-20
# @Author  : Joe
# @Version : 

import numpy as np
import cv2


# Background Subtraction

# Goal 
	# 在本节中，我们将熟悉OpenCV中的去除背景的各种方法

# Basics
	# 背景去除是在众多视频类应用中的一个很重要的步骤。例如，假设
	# 在一个来访者计算器中，有一个静止的相机用来计数有多少个来访
	# 者进入或者离开房间，或者一个交通摄像头来提取车辆信息等等。
	# 在上述所有的情况当中，首先我们需要将人或者车辆提取出来。技
	# 术上来说就是需要将移动的前景从不动静止的背景中抽取出来。

	# 如果你已经有一个单独背景图片，像没有来访者的房间的图像，没
	# 有车的道路的图像，那么背景去除是非常简单的任务。只需要将新的
	# 图像从背景图像中减去即可以得到前景物体。但是在大多数的情况下，
	# 你可能没有单独的背景图像，所以我们需要从任何图像中提取出来背
	# 景图像。如果车产生了阴影，那么情况就更复杂了，因为阴影也是移
	# 动的，简单的背景去除将会将阴影标记为前景。这些情况使得整个事
	# 情变得更复杂。

	# 基于这个目标有很多算法被提出来了。OpenCV实现了3种很简单使用
	# 的方法。我们一个一个来看。

# BackgroundSubtractorMOG
	# 这个算法是基于高斯混合前景/背景分割算法(Gaussian Mixture-Based
	# Background/Foreground Segementation Algorithm).在2001年，由
	# P.KadewTrakuPong和R.Bowden在论文"An improved adaptive background
	# mixture model for real-time tracking with shadow detection"
	# 中提出。它采用了一个方法来讲每个背景像素根据K高斯分布（K=3 TO 5）
	# 进行建模。混合的权重代表了那些颜色停留在场景中的时间比例。有可能是
	# 背景的那些颜色将会是停留时间很长并且很稳定的那些。

	# 在编码中，我们需要使用函数cv.createBackgroundSubtractorMOG()来
	# 创建一个背景对象。它有一些可选的参数例如历史的长度，高斯混合的数字，
	# 阈值等等。它会将这些参数都设置为默认的。然后在视频的循环中，使用函数
	# backgroundsubtractor.apply()来获取背景图的掩码图。

cap = cv2.VideoCapture('vtest.avi')
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()

while (1):
	ret, frame = cap.read()

	if ret == False:
		break

	fgmask = fgbg.apply(frame)
	cv2.imshow('frame',fgmask)

	k = cv2.waitKey(30) &0xff
	if k == 27:
		break

cv2.destroyAllWindows()
cap.release()

# BackgroundSubtractorMOG2
	# 这个方法也是一样的。但是一个很重要的特性就是它为每个像素选定了一个
	# 适当的高斯分布（在上个例子中，整个算法都贯穿使用了K高斯混合）。它
	# 对于环境中的光线变化给予了更好的结果。

	# 跟上个例子一样，我们需要创建一个背景去除物体对象，在这里，你可以有
	# 一个额外的选项就是是否检测阴影。如果detectShadows = True(默认True)
	# 它会检测和遮罩阴影，但是会降低速度。阴影将会被标记为灰色。
# cap = cv2.VideoCapture('vtest.avi')
# fgbg = cv2.createBackgroundSubtractorMOG2()
# while(1):
#     ret, frame = cap.read()
#     fgmask = fgbg.apply(frame)
#     cv2.imshow('frame',fgmask)
#     k = cv2.waitKey(30) & 0xff
#     if k == 27:
#         break
# cap.release()
# cv2.destroyAllWindows()

# BackgroundSubtractorGMG
	# 这个算法结合了统计图像背景估计及单像素贝叶斯分割。在2012年提出。

	# 它使用了最前面的一些帧图像做背景建模（一般是120帧）。它使用了贝
	# 叶斯推理的概率前景物体分割来识别可能的前景物体。预估是可调节的。
	# 新的观察在权重上重于旧的观察的权重。还有一些形态的变换比如扩展
	# 和闭合会被使用来消除一些噪声。在前面的一些帧中，你可能会看到只是
	# 黑色的图像。

	# 最好是在结果中使用形态扩张来移除噪声

# cap = cv2.VideoCapture('vtest.avi')
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
# fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()
# while(1):
#     ret, frame = cap.read()
#     fgmask = fgbg.apply(frame)
#     fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
#     cv2.imshow('frame',fgmask)
#     k = cv2.waitKey(30) & 0xff
#     if k == 27:
#         break
# cap.release()
# cv2.destroyAllWindows()