#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-02
# @Author  : Joe

import numpy as np
import cv2

cap = cv2.VideoCapture('video.mp4')

while  cap.isOpened():
	ret, frame = cap.read()

	if not ret:
		break
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.imshow('video', gray)

	if  cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
