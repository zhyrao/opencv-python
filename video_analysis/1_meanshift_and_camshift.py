#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-19
# @Author  : Joe

import numpy as np
import cv2

# Goal
	# 在本节中，我们将学习使用Meanshift和Camshift算法在视频中
	# 找到并且追踪物体对象。

# Meanshift
	# meanshift背后的原理表现很简单。假设你有一个点集。（这个点集
	# 可以是类似直方图反投影的像素分布）。你被赋予了一个小的窗口或
	# 圆，你必须把这个小窗口移动到这样的一个位置，使得小窗口内的像
	# 素强度总和是最大的（或者小窗口内含有的像素是最多的）。其中的
	# 过程如下图表示：
	# link:https://docs.opencv.org/3.4.0/meanshift_basics.jpg

	# 初始的窗口是带有蓝色的，名字是C_1的圆环。原始的中心被标记为蓝
	# 色的矩形，名字为C1_o。但是如果你观察在这个圆环内的像素的图心，
	# 你会发现点C1_r（被标记为蓝色的圆圈）是这个图形的真正图心。很明
	# 了的可以看到圆C1的圆心和圆内的图心不是一致的。所以移动这个窗口
	# 使得这个窗口的中心和原来的那个图心吻合。然后再一次查找新的图心。
	# 很有可能的情况就是，它们依然不是一致的。所以，我们将再次移动，
	# 直到这个图心和窗口的中心吻合一致（或者它们之间有可以理解的差距）。
	# 所以最终你得到的是一个有最大像素分布的窗口。它在图上被标记为绿
	# 色，名字为C2。可以从图像中看出，它包含有最大数量的点。整体的过
	# 程表示为下面的gif图像。
	# link:https://docs.opencv.org/3.4.0/meanshift_face.gif

	# 所以通常我们传入已经反投影的直方图图像并且初始化目标位置。当
	# 目标对象移动了，那么这个移动会在反投影直方图图像中明显的显示
	# 出来。结果就是meanshift将我们的窗口移动到有最大强度的新位置
	# 上。

# Meanshift in OpenCV
	# 为了在OpenCV中使用meanshift，首先我们需要设立目标，并且找到
	# 它的直方图这样我们才能反向投影这个目标，然后在每一帧中计算meanshift
	# 我们也需要提供窗口的初始化位置。对于直方图来说，只有HUE被考虑。
	# 同样的为了避免低强度的光线造成的错误值，低强度的光将会被cv.inRange()
	# 抛弃。

cap = cv2.VideoCapture('slow.flv')

# take first frame of the video
ret, frame = cap.read()

# setup initial locations of window
r,h,c,w = 250,90,400,125 # simple hardcode the values
track_window = (c,r,w,h)

# set up ROI for tracking
roi = frame[r:r+h, c:c+w]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0.,60.,32.)), np.array((180.,255.,255.,)))
roi_his = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv2.normalize(roi_his,roi_his,0,255,cv2.NORM_MINMAX)

# setup the termination criteria, either 10 iteration or move by at least 1 pt
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while True:
	ret, frame = cap.read()

	if (ret == True):
		hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
		 dst = cv.calcBackProject([hsv],[0],roi_hist,[0,180],1)
		  # apply meanshift to get the new location
		  ret, track_window = cv.meanShift(dst, track_window, term_crit)
		  # Draw it on image
		  x,y,w,h = track_window
		  img2 = cv.rectangle(frame, (x,y), (x+w,y+h), 255,2)
		  cv.imshow('img2',img2)
		  k = cv.waitKey(60) & 0xff
		  if k == 27:
		  	break
		  else:
		   cv.imwrite(chr(k)+".jpg",img2)
	else:
	 break
cv.destroyAllWindows()
cap.release()