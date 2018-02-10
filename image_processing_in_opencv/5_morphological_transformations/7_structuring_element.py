#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-10 23:46:22
# @Author  : Joe
# @Version : 

import numpy as np
import cv2


# cv2.getStructuringElement()
# cv2.getStructuringElement(shape, ksize[, anchor]) → retval
# Returns a structuring element of the specified size and shape for morphological operations.
# MORPH_RECT 
# MORPH_ELLIPSE 
# MORPH_CROSS 
# CV_SHAPE_CUSTOM 

rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
print (rect_kernel)

ellipse_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
print(ellipse_kernel)

cross_kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
print(cross_kernel)