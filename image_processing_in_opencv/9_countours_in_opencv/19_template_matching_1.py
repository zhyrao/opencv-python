#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-01
# @Author  : Joe

import numpy as np
import cv2
from matplotlib import pyplot as plt 

# Template Matching 模板/样板匹配

# Goal
	# 通过模板匹配放在在图像中找到目标物体

# Theory
	# 模板匹配是在一副较大图像中查找并且定位较小
	# 目标物体的一种方法。OpenCV提供了cv2.matchTemplate()
	# 方法来实现这个目的。它简单的将模板图像在原图像
	# 中滑动（作2D卷积）并且比较他们。这种比较的方式
	# 在OpenCV中提供了很多种。它返回了一副灰度图，这个
	# 图中的每个像素表示了这个像素的周围像素匹配这个
	# 模板的程度。

	# 如果输入图像的大小为(W,H)，模板图像的大小为(w,h)，
	# 那么返回输入的图像大小为(W-w+1, H-h+1)。一旦我们
	# 得到了这个结果，那么就可以用cv2.minMaxLoc()来定位
	# 最大/最小值。将这个值作为矩形的左上角，将模板图像
	# 的大小作为矩形的宽高，那么这个矩形内的内容就是匹配
	# 的图像区域。
		# NOTE：使用cv2.TM_SQDIFF会给出最佳的匹配


# Template Matching in OpenCV
	# 在这里，我们在图像中查找messi的脸部作为例子。
img = cv2.imread('messi5.jpg', 0)
img2 = img.copy()
template = cv2.imread('template.jpg',0)
w, h = template.shape[::-1]

# 所有的比较方式
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
	'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
	img = img2.copy()
	method = eval(meth)

	# 查找
	res = cv2.matchTemplate(img, template, method)
	min_val, max_val,min_loc,max_loc = cv2.minMaxLoc(res)

	if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
		top_left = min_loc
	else:
		top_left = max_loc

	bottom_right = (top_left[0] + w, top_left[1] + h)

	cv2.rectangle(img,top_left,bottom_right, 255, 2)

	plt.subplot(121),plt.imshow(res,cmap = 'gray')
	plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
	plt.subplot(122),plt.imshow(img,cmap = 'gray')
	plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
	plt.suptitle(meth)

	plt.show()

# 通过结果可以看出cv2.TM_CCORR并没有我们期待中的那么好