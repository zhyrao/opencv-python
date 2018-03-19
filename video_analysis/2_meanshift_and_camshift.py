#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-19
# @Author  : Joe
# @Version : 

import numpy as np
import cv2 as cv


# CAMshift
	# 如果你很近的看最后的结果会发现什么呢？是存在一个问题。
	# 我们的窗口一直都是同样的大小而当车子由远到近的时候，窗
	# 口没有变化。这样看起来非常不好。我们需要调整窗口的大小，
	# 随着目标的大小和旋转角度来调整。再一次的这个解决方案来自
	# 于opencv实验室，它称为CAMshit(Continuously Adaptive 
	# Meanshift)，由Gary Bradsky在1988年在论文"Computer 
	# Vision Face Tracking for Use in a Perceptual User
	# Interface"。

	# 它首先使用了meanshift。一旦得到了meanshift，就会更新
	# 窗口的大小为，
			# s = 2 * sqrt(M00/256)

	# 它也计算了最佳匹配的椭圆的角度。然后再一次的在新的缩放
	# 后的窗口和前面的窗口位置的地方应用meanshift。这个过程
	# 会持续到精度达到要求。
	# link:https://docs.opencv.org/3.4.0/camshift_face.gif

# CAMshift in OpenCV
	# 它更meanshift几乎一样，但是它返回了一个旋转后的矩形(是
	# 我们的结果)和一个方盒的参数（用来作为下一次搜寻窗口的参
	# 数）。
cap = cv.VideoCapture('slow_traffic_small.mp4')
# take first frame of the video
ret,frame = cap.read()
# setup initial location of window
r,h,c,w = 200,40,300,55  # simply hardcoded the values
track_window = (c,r,w,h)
# set up the ROI for tracking
roi = frame[r:r+h, c:c+w]
hsv_roi =  cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
roi_hist = cv.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv.normalize(roi_hist,roi_hist,0,255,cv.NORM_MINMAX)
# Setup the termination criteria, either 10 iteration or move by atleast 1 pt
term_crit = ( cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1 )
while(1):
    ret ,frame = cap.read()
    if ret == True:
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv],[0],roi_hist,[0,180],1)
        # apply meanshift to get the new location
        ret, track_window = cv.CamShift(dst, track_window, term_crit)
        # Draw it on image
        pts = cv.boxPoints(ret)
        pts = np.int0(pts)
        img2 = cv.polylines(frame,[pts],True, 255,1)
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