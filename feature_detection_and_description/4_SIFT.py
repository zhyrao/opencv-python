#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-12
# @Author  : Joe
# @Version : 

import numpy as np
import cv2


# Introduction to SIFT(scale-invariant Feature Transform)

# Goal
	# 理解SIFT 缩放不变特征转换
	# 学会如何找到SIFT的关键点和描述符

# Theory
	# 在上几节中，我们看到了如果去检测角点，例如使用harris算法等。
	# 这类的算法中，角点是保持旋转不变的，这意味着，即使图像被旋转
	# 了，我们任然能找到同样的角点。 这个很明显的看出来是因为即使图
	# 像旋转了，那些角点依然保持为角点。 但是如果是缩放呢？ 例如，
	# 在下副图像中。
	# link: https://opencv-python-tutroals.readthedocs.io/en/latest/_images/sift_scale_invariant.jpg

	# 在这幅图像中，角点明显在图像缩放过程中变化了，这样看来harris
	# 算法是不能在缩放中保持角点不变的。

	# 在2004年， D.Lowe, 大不列颠哥伦比亚大学，提出来了一个新的算
	# 法，缩放保持不变特征转换(SIFT), Distinctive Image Feature
	# from Scale-Invariant Keypoints，这个算法提取了关键点并且计
	# 算出它的描述符。

img = cv2.imread('home.jpg')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#sift = cv2.SIFT()
sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray,None)

img=cv2.drawKeypoints(gray,kp)

cv2.imshow('shit_keypoints', img)

cv2.waitKey(0)
cv2.destroyAllWindows()