#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-09 23:33:37
# @Author  : Joe
# @Version : 

import numpy as np
import cv2


# 腐蚀的基本思想就像土地被腐蚀一样， 他总是腐蚀掉 前景物体(forground object)
# 的边界（尝试尽可能保持前景物体为白色）。

# 那么它是做什么的呢？内核在图像中滑动 (如2D 卷积)。
# 如果内核下的所有像素为 1, 则原始图像中的像素 (1 或 0) 将被视为 1, 否则它将被侵蚀 (使其为零)。

# 发生的情况如下：所有靠近前景边缘的像素将根据内核的大小来决定是否会被丢弃(置零)。
# 这样以来前景物体的宽度或者大小将减少或者简单来说图像中的白色区域会减少。
# 这对于移除较小的白色噪声或者分离两个相连的物体比较有用

# cv2.erode()
# cv2.erode(src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]]) → dst

img = cv2.imread('j.png')
kernel = np.ones((5,5), np.uint8)

erosion = cv2.erode(img, kernel, iterations = 2)

cv2.imshow('original', img)
cv2.imshow('erosion',erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()