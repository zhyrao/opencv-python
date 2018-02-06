#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-06 15:57:38
# @Author  : Joe

import numpy as np
import cv2

# Applies a fixed-level threshold to each array element.
# 对于每个数组元素使用一个固定的阈值来检测
# cv2.threshold(src, thresh, maxval, type[, dst]) → retval, dst
	# src: 源图像
	# threshold: 阈值
	# maxvalue: 大于阈值则赋值为maxvalue
	# type: 二值化类型