#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-05 22:55:16
# @Author  : Joe

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while  True:
	# take each frame
	_, frame = cap.read()

	# convert bgr to hsv
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# define range of blue color in hsv
	lower_blue = np.array([110, 50, 50])
	upper_blue = np.array([130, 255, 255])

	# threshold the hsv image to get only the blue colors
	mask = cv2.inRange(hsv, lower_blue, upper_blue)

	# bitwise-and mask and original image
	res = cv2.bitwise_and(frame, frame, mask=mask)

	cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('res', res)
	cv2.imshow('hsv', hsv)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()