#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-02
# @Author  : Joe

import numpy as np
import cv2


img = cv2.imread('logo.jpg',  0)
cv2.imshow('image', img)

k = cv2.waitKey(0)

if  k == 27:
	cv2.destroyAllWindows()
elif k == ord('s'):
	cv2.imwrite('logogray.jpg', img)
	cv2.destroyAllWindows()