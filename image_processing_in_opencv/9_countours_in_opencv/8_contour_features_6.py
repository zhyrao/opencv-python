#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-18
# @Author  : Joe

import numpy as np
import cv2

img = cv2.imread('rect.jpg')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(img_gray, 127, 255, 0)

img_c, contours, hierachy = cv2.findContours(thresh, 0, 1)

cnt = contours[0]

ellipse = cv2.fitEllipse(cnt)
img = cv2.ellipse(img, ellipse, (0, 255,0), 2)

cv2.imshow('ellipse', img)

cv2.waitKey(0)
cv2.destroyAllWindows()