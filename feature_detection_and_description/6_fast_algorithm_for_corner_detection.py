#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-15
# @Author  : Joe
# @Version : 

import numpy as np
import cv2
from matplotlib import pyplot as plt

# FAST Algorithm for Corner Detection

# Goal
	# 在本节中，理解基础的FAST算法


# Theory
	# 我们已经看过了好几个特征点检测方法，并且其中
	# 有一些的效果非常不错。但是如果用在实时的角度
	# 来检测一些东西，它们的速度任然不够快。其中一个
	# 很好的例子就是只具有有限的计算资源的移动机器人
	# 使用SLAM(simultaneour localization and map-
	# ping)技术定位。

	# 为了解决这个问题，在2006年，Edward Rosten和
	# Tom Drummond在他们的论文"Machine learning
	# for high-speed corner detection"中提出了这
	# 个算法，FAST(Features from Accelerated Segment
	# Test)。下面讲解了这个算法的基本总结，详细的信
	# 息请解读原论文。

# Feature Detection using FAST
	# 1. 选择图像中的一个像素p，p将被识别为是否是一个感
		#兴趣的点。让p的强度为 I_p
	# 2. 选择一个适当的阈值 t 。
	# 3. 将这个像素p周围的一圈16个像素作为参考。
	# 4. 现在如果这个像素p是一个角点的话，那么将存在一系
		#列n个连续邻近的像素（这些像素属于这个圆圈）的强
		#度值都会大于 I_p + t（亮），或者都会小于 I_p-t
		#(更暗一些). n 大部分会被赋值为12.
	# 5. 一个更高速度的测试用于检测大量不是角点的像素。这个
		#测试中仅仅检测4个像素，1、9、5、13（首先检测1和9像
		#素的强度看他们是否更亮或者更暗。如果更亮或者更暗那
		#么再检测第5和第13个像素）。如果这个像素p是一个角点，
		#那么这个4个像素中最少有3个像素会比阈值(Ip+t)或者
		#(I_p - t)。如果上述的检测不成立，那么这个像素p不
		#可能是角点。


# FAST Feature Detector in OpenCV

img = cv2.imread('sample.jpg',0)

# Initiate FAST object with default values
#fast = cv2.FastFeatureDetector()
fast = cv2.FastFeatureDetector_create()

# find and draw the keypoints
kp = fast.detect(img,None)
img2 = cv2.drawKeypoints(img, kp, None, color=(255,0,0))

# Print all default params
print("Threshold: {}".format(fast.getThreshold()))
print("nonmaxSuppression:{}".format(fast.getNonmaxSuppression()))
print("neighborhood: {}".format(fast.getType()))
print("Total Keypoints with nonmaxSuppression: {}".format(len(kp)))

cv2.imwrite('fast_true.png',img2)

# Disable nonmaxSuppression
fast.setNonmaxSuppression(0)
kp = fast.detect(img,None)

print ("Total Keypoints without nonmaxSuppression: ", len(kp))

img3 = cv2.drawKeypoints(img, kp, None, color=(255,0,0))
cv2.imshow("img",img3)
cv2.waitKey(0)
cv2.destroyAllWindows()

#cv2.imwrite('fast_false.png',img3)