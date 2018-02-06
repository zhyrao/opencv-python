#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-06 09:05:52
# @Author  : Joe

import numpy as np
import cv2

frame = cv2.imread('messi.jpg')

# convert bgr to hsv
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# red for HSV [0, 255, 255]

# define range of red color in hsv (dark red)
lower_blue = np.array([-10, 10, 50])
upper_blue = np.array([10, 255, 255])

# define range of red color in hsv (bright red)
lower_blue1 = np.array([170, 50, 50])
upper_blue1 = np.array([190, 255, 255])

# threshold the hsv image to get only the blue colors
mask = cv2.inRange(hsv, lower_blue, upper_blue)

mask2= cv2.inRange(hsv, lower_blue1, upper_blue1)

mask = mask + mask2

# bitwise-and mask and original image
res = cv2.bitwise_and(frame, frame, mask=mask)

cv2.imshow('frame', frame)
cv2.imshow('mask', mask)
cv2.imshow('mask2', mask2)
cv2.imshow('res', res)
cv2.imshow('hsv', hsv)
cv2.waitKey(0)

cv2.destroyAllWindows()