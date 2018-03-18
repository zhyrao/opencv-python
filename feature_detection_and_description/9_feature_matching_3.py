#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-18
# @Author  : Joe
# @Version : 

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# FLANN based Matcher
	# FLANN代表了Fast Library for Approximate Nearest
	# Neighbors. 它包含了一些已经优化的算法，这些算法能够
	# 快速的在大量的数据集和高维特征点中找到最近的邻近点。
	# 它比BFMatcher对于大量数据集要快很多。

	# 对于基于FLANN的匹配器，我们需要传入两个字典类型参数
	# 这两个参数指定了使用哪种算法，以及这个算法相应的参数
	# 等等。第一个是下标参数。对于各种算法的课传入的参数都在
	# FLANN文档中做了解释。总的来说，对于像SIFT,SURF算法来
	# 说，你可以参考如下的参数：
	# FLANN_INDEX_KDTREE = 1
	# index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)

	# 如果同时使用了ORB，那么就可以如下传参。
	# FLANN_INDEX_LSH = 6
	# index_params = dict(algorithm = FLANN_INDEX_LSH,
	# 			table_number = 6, #12
	# 			key_size = 12, #20
	# 			multi_probe_level = 1 #2)

	# 第二个参数是查询参数。他制定了树应该递归遍历的次数。
	# 越高的值能有越好的精度，但是会占用越多的时间。


img1 = cv.imread('box.png',0)          # queryImage
img2 = cv.imread('box_in_scene.png',0) # trainImage
# Initiate SIFT detector
sift = cv.SIFT()
# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)
# FLANN parameters
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)   # or pass empty dictionary
flann = cv.FlannBasedMatcher(index_params,search_params)
matches = flann.knnMatch(des1,des2,k=2)
# Need to draw only good matches, so create a mask
matchesMask = [[0,0] for i in xrange(len(matches))]
# ratio test as per Lowe's paper
for i,(m,n) in enumerate(matches):
    if m.distance < 0.7*n.distance:
        matchesMask[i]=[1,0]
draw_params = dict(matchColor = (0,255,0),
                   singlePointColor = (255,0,0),
                   matchesMask = matchesMask,
                   flags = 0)
img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)
plt.imshow(img3,),plt.show()