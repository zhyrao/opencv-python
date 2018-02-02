#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-02
# @Author  : Joe

import numpy as np
import cv2

# 保存视频我们需要 cv2.VideoWriter()
# para1:  保存的名称 filename
# para2:  FourCC code
# para3: FPS frame per second
# para4: 分辨率
# para5: isColor 标志（默认是true， false则存储为gray模式）
#  FourCC is a 4-byte code used to specify the video codec. 
#	The list of available codes can be found in fourcc.org.
#	 It is platform dependent. Following codecs works fine for me.

#  In Fedora: DIVX, XVID, MJPG, X264, WMV1, WMV2. (XVID is more preferable. MJPG results in high size video. X264 gives very small size video)
#  In Windows: DIVX (More to be tested and added)

cap = cv2.VideoCapture(0)

# fourcc
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi', fourcc, 30, (640, 480), True)

while cap.isOpened():
	ret, frame = cap.read()
	if ret:
		frame = cv2.flip(frame, 0) # frame is fliped cv2.flip(src, flipCode) vertical: 0 horizontal:1 both:-1

		out.write(frame)
		cv2.imshow('video', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break

# release all
cap.release()
out.release()
cv2.destroyAllWindows()