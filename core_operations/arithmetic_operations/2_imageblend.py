#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-04 23:25:42
# @Author  : Joe

import numpy as np
import cv2


# 图片混合：
			# 这个本质上也是图片的相加，但是不同的图片对应不同的权重比例，
			# 这样的结果给人一种混合或者透明的感觉。
			# 公式如下：
				# g(x) = (1-α)f(x) + αf(y)
				# 对 α 取值不同（0 -- 1），就能得到不同的变换效果

img1 = cv2.imread('ml.jpg')
print(img1.shape)
img2 = cv2.imread('logo.png')
print(img2.shape)

dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

cv2.imshow('image blend', dst)


cv2.waitKey(0)
cv2.destroyAllWindows()