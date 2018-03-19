#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-19
# @Author  : Joe

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Feature Matching + Homography to find Objects

# Goal
	# 在本节中，我们将在一副较复杂的图像中混合使用特征匹配和
	# calib3d模块中的findHomography来查找已知的物体。

# Basics
	# 所以我们上节中做了什么呢？我们使用了一个未知图像，然后
	# 在它里面找到了一些特征点，我们再使用另外一副训练图像，
	# 也在图像中找到一些特征点，然后在这些特征点当中找到他们
	# 相互匹配的特征点。简单来说，我们在另外一副图像中找到了
	# 一些物体的某些部位的位置。这些信息足够让我们在训练图像
	# 中找到精确的物体。

	# 为了实现这个目标，我们使用了在 calib3d 模块中的函数，cv.findHomography()
	# 如果我们给这个函数传入了在两幅图像中都存在的一些点，这
	# 个函数将会找到这个物体的透视转换信息。然后我们就可以使
	# 用cv2.perspectiveTransform()来找到这个物体。它需要最
	# 少4个正确的点来找到这个变换。

	# 我们可以看到这里将会存在在匹配的时候会出现一些可能的错
	# 误信息将会影响到结果。解决这个问题，算法使用RANSAC或者
	# LEAST_MEDIAN(可以通过标记判断)。所以好的匹配提供了正
	# 确的预测被称为inliers，剩余的被称为outliers。

# Code
MIN_MATCH_COUNT = 10
img1 = cv.imread('box.png',0)          # queryImage
img2 = cv.imread('box_in_scene.png',0) # trainImage
# Initiate SIFT detector
sift = cv.xfeatures2d.SIFT_create()
# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks = 50)
flann = cv.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des1,des2,k=2)
# store all the good matches as per Lowe's ratio test.
good = []
for m,n in matches:
    if m.distance < 0.7*n.distance:
        good.append(m)

if len(good)>MIN_MATCH_COUNT:
    src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
    dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)
    M, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC,5.0)
    matchesMask = mask.ravel().tolist()
    h,w,d = img1.shape
    pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
    dst = cv.perspectiveTransform(pts,M)
    img2 = cv.polylines(img2,[np.int32(dst)],True,255,3, cv.LINE_AA)
else:
    print( "Not enough matches are found - {}/{}".format(len(good), MIN_MATCH_COUNT) )
    matchesMask = None	

draw_params = dict(matchColor = (0,255,0), # draw matches in green color
                   singlePointColor = None,
                   matchesMask = matchesMask, # draw only inliers
                   flags = 2)
img3 = cv.drawMatches(img1,kp1,img2,kp2,good,None,**draw_params)
plt.imshow(img3, 'gray'),plt.show()