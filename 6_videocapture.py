#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-02
# @Author  : Joe

import numpy as np
import cv2
		
# 视频就是一系列的帧、图片构成的，所以处理视频就是处理一系列的帧、图片

# cv2.VideoCapture() 
# 参数可以是数值或者是一个视频文件的名称路径
# 数值： 表示摄像机硬件的下标（有可能多个摄像机） 只有一个相机可以是0或者-1
#               如果多个相机的话可以传递1、2等等
#  
# 有时候capture初始化的时候会失败，这个时候可以用cap.isOpened()来检查是否开启
# 如果没有开启则使用cap.open()来开启
#
# 可以通过cap.get(propid) 来获取capture的属性 propid 是0-18的数字，每个数字代表
# 不同的属性
# 也可以通过cap.set(propid, value)来设置capture的相关属性
# width = cap.get(3) height = cap.get(4)
# cap.set(3, 320)  cap.set(4, 240)


#  ret, frame = cap.read()  
# 这个函数囊括了grab() 和 retrieve()， 如果没有更多的frame了则ret = False
# returns a bool. if frame is read correctly, it will be true.


cap = cv2.VideoCapture(0)

while  True:
	# capture frame by frame 
	ret, frame = cap.read()
	if not ret:
		break
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	cv2.imshow('frame', gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()


# CV_CAP_PROP_POS_MSEC Current position of the video file in milliseconds or video capture timestamp.
# CV_CAP_PROP_POS_FRAMES 0-based index of the frame to be decoded/captured next.
# CV_CAP_PROP_POS_AVI_RATIO Relative position of the video file: 0 - start of the film, 1 - end of the film.
# CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
# CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
# CV_CAP_PROP_FPS Frame rate.
# CV_CAP_PROP_FOURCC 4-character code of codec.
# CV_CAP_PROP_FRAME_COUNT Number of frames in the video file.
# CV_CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() .
# CV_CAP_PROP_MODE Backend-specific value indicating the current capture mode.
# CV_CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).
# CV_CAP_PROP_CONTRAST Contrast of the image (only for cameras).
# CV_CAP_PROP_SATURATION Saturation of the image (only for cameras).
# CV_CAP_PROP_HUE Hue of the image (only for cameras).
# CV_CAP_PROP_GAIN Gain of the image (only for cameras).
# CV_CAP_PROP_EXPOSURE Exposure (only for cameras).
# CV_CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.
# CV_CAP_PROP_WHITE_BALANCE_U The U value of the whitebalance setting (note: only supported by DC1394 v 2.x backend currently)
# CV_CAP_PROP_WHITE_BALANCE_V The V value of the whitebalance setting (note: only supported by DC1394 v 2.x backend currently)
# CV_CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently)
# CV_CAP_PROP_ISO_SPEED The ISO speed of the camera (note: only supported by DC1394 v 2.x backend currently)
# CV_CAP_PROP_BUFFERSIZE Amount of frames stored in internal buffer memory (note: only supported by DC1394 v 2.x backend currently)

