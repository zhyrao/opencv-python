#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-18
# @Author  : Joe

import numpy as np
import cv2
from matplotlib import pyplot as plt 


# Minimum Enclosing Circle 最小包围圈

# cv2.minEnclosingCircle()
	# 获得一个完全包围物体并且是最小面积的圆圈

img = cv2.imread('rect.jpg')
plt.subplot(221),plt.imshow(img)
plt.title('original')
plt.xticks([]),plt.yticks([])
#cv2.imshow('original', img)
img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.subplot(222),plt.imshow(img_g)
plt.title('gray')
plt.xticks([]),plt.yticks([])


ret, thresh = cv2.threshold(img_g, 127, 255, 0)

img_c, contours, hierachy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]

(x, y), radius = cv2.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)

img_d = cv2.circle(img, center, radius, (0, 255, 0), 2)

#cv2.imshow('circle', img_d)
#
#cv2.imshow('gray', img_g)
#cv2.imshow('threshold', thresh)

plt.subplot(223),plt.imshow(thresh)
plt.title('thresh')
plt.xticks([]),plt.yticks([])


plt.subplot(224),plt.imshow(img_d)
plt.title('circle')
plt.xticks([]),plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()