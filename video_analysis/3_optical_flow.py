#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-20
# @Author  : Joe

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt 

# Optical Flow

# Goal
	# 在本节中，我们将理解光流现象的概念以及实用Lucas-Kanade方法
	# 来预测
	# 我们将使用cv,calcOpticalFlowPyrLK()函数来追踪视频中的特征点

# Optical Flow
	# 光流现象是连续两帧图像中由于物体的移动或者相机的移动造成的一种
	# 运动现象模式。它是一个2D的矢量场，每个向量都代表着一个点从第一
	# 帧到第二帧的位移向量。看看下图
	# Link:https://docs.opencv.org/3.4.0/optical_flow_basic1.jpg

	# 它显示了一个球在连续5帧中的移动。箭头显示了它的位移向量。光流有
	# 很多的应用区域，例如：
		# 动作重建
		# 视频压缩
		# 视频稳定

	# 光流作用于几个假设中：
		# 1.字连续的帧中，物体的像素强度不会改变。
		# 2. 周围附近的像素也有类似的运动动作

	# 假设在第一帧中的一个像素I(x,y,t)（考虑一个新的维度，时间，在这里加
	# 上了。前期我们仅仅在操作图像，所以不需要时间的概念）。它在下一帧中
	# 移动了距离(dx,dy)，消耗了时间dt。所以因为这些像素点是一样的并且它
	# 们的强度也保持不变，那么我们就可以说：
		# I(x,y,t) = I(x+dx, y+dy, t+dt)
	# 然后对右边进行泰勒级数近似，去掉共同的条件然后除以dt得到下面的方程:
		# f_x * u + f_y * v + f_t = 0
	# 其中:
		#  f_x = δf/δx;  f_y = δf/δy;
		# u = dx/dt; v = dy/dt;

	# 上面的这个方程被称为光流方程。其中，我们看到有f_x和f_y，它们是图像的
	# 梯度。同样的f_t也是随着时间的梯度。但是(u,v)是未知的。我们不能解决有
	# 两个未知参数的一个方程。所以有很多的解决方法被提出来了，其中就有Lucas
	# Kanade方法。

# Lucas- Kanade 方法
	# 我们在前面已经看到了假设情况，所有邻近的像素都有类似的移动动作。Lucas
	# Kanade方法是在这个特征点周围取了一个3x3范围的块。根据假设来说，这9个
	# 像素也有同样的运动动作。我们就可以为这9个点找到(f_x,f_y,f_t)。所以我
	# 们的问题就成了有9个方程而未知变量只有两个，戳戳有余的解决方程。

	# 从使用者角度来看，想法很简单，我们给出了一些点来追踪，然后我们得到了这
	# 些点的光流向量。但是这里依然有一些问题。直到现在我们处理的都是比较小的
	# 移动动作。它在较大的移动动作上会失败。所以我们需要再次使用金字塔方法。
	# 当我们使用金字塔方法的时候，较小的移动动作会被去除，而较大的移动动作会
	# 变成较小的移动动作。然后在使用lucas-kanade方法。

# Lucas-Kanade 光流法在OpenCV中的使用
	# OpenCV把所有的都融合在一个函数中,cv.calcOptialFlowPyrLK()。在这里，我
	# 们创建一个比较简单的在视频中追踪点的示例。我们使用cv.goodFeaturesToTrack()
	# 来获取特征点。我们取视频中的第一帧，监测一些shi-tomasi角点，然后我们持续
	# 的使用lucas-kanade方法来追踪它们。对于cv.calcOptialFlowPyrLK(),我们需要
	# 传入前一帧，前追踪的点和下一帧。它返回下一帧中的点，这些点有一些状态，例如
	# 如果是1，那么这点在下一帧中被找到，如果是0则没有。我们迭代的将这些点作为上
	# 一次点参数传入下一次的步骤中。

cap = cv.VideoCapture('slow_traffic_small.mp4')

# params for shitomas corner detection
feature_params = dict(maxCorners =100,
	qualityLevel = 0.3,
	minDistance = 7,
	blockSize = 7)

# parameters for lucas kanade optical flow
lk_params = dict(winSize = (15,15),
	maxLevel = 2,
	criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))

# create some random colors
color = np.random.randint(0,255,(100,3))

# take first frame and find corners in it
ret, old_frame = cap.read()
old_gray = cv.cvtColor(old_frame, cv.COLOR_BGR2GRAY)
p0 = cv.goodFeaturesToTrack(old_gray, **feature_params, mask = None)

# create a mask image for drawing purposes
mask = np.zeros_like(old_frame)

while True:
	ret,frame = cap.read()

	if ret == False:
		break
	frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

	# calculate optical flow
	p1, st, err = cv.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

	# select good points
	good_new = p1[st==1]
	good_old = p0[st==1]

	# draw the tracks
	for i, (new, old) in enumerate(zip(good_new, good_old)):
		a,b = new.ravel()
		c,d = old.ravel()
		mask = cv.line(mask,(a,b),(c,d),color[i].tolist(),2)
		frame = cv.circle(frame,(a,b), 5, color[i].tolist(), -1)

	img =  cv.add(frame,mask)

	cv.imshow('frame',img)

	k=cv.waitKey(30) & 0xff
	if k == 27:
		break

	# now update the previous frame and previous points
	old_gray = frame_gray.copy()
	p0 = good_new.reshape(-1,1,2)

cv.destroyAllWindows()
cap.release()