#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-01
# @Author  : Joe

import numpy as np
import cv2
from matplotlib import pyplot as plt 

# Template Matching with Multiple Objects
# 前节中，我们在一副图像中搜寻messi的脸部，其中
# 在这幅图像中只存在一个。如果在一副图像中存在着
# 多个想要搜寻的物体，那么cv2.minMaxLoc()不会
# 返回给所有的位置。在这种情况下，我们将采用阈值
# 的方法。在这里我们在一副mario的图像查找金币

img_rgb = cv2.imread('mario.jpg')
img_orig = img_rgb.copy()
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('mariotemplate.jpg', 0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.7
loc = np.where( res>= threshold)
for pt in zip(*loc[::-1]):
	cv2.rectangle(img_rgb, pt, (pt[0]+w, pt[1]+h), (0,0,255), 1)

plt.subplot(131),plt.imshow(cv2.cvtColor(img_orig, cv2.COLOR_BGR2RGB))
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(res,cmap = 'gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB),cmap = 'gray')
plt.title('Result'), plt.xticks([]), plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()