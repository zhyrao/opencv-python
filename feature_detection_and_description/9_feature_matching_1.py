#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-18
# @Author  : Joe
# @Version : 

import numpy as np
import cv2
import matplotlib.pyplot as plt

# Goal
	# 我们来看看怎么用一张图像中的特征匹配另外图像中。
	# 我们将使用OpenCV中的Brute-Forece和FLANN匹配器

# Basic of Brute-Force Matcher
	# Brute-Force匹配器很简单。它使用了第一组中的一个
	# 特征的描述子来和第二组的所有其他的特征来进行距离
	# 计算的匹配。并且距离最近的那个将被返回。

	# 在使用BF匹配器中，首先我们必须要使用cv.BFMatcher()
	# 来创建一个BFMatcher对象。它带有两个可选择的参数。
	# 第一个参数是normType。它指定了距离测量的方式。默认
	# 的这个参数是cv.NORM_L2。它对SIFT, SURF等非常有用。
	# 对于基于ORB, BRIEF, BRISK等二进制字符串来说，应该
	# 采用cv2.NORM_HAMMING，这个标志采用hamming距离来做
	# 为测量标准。如果ORB中使用了WTA_K == 3(OR 4),那么应
	# 该使用cv.NORM_HAMMING。

	# 第二个参数是一个布尔变量，交叉检查默认是false。如果
	# 是true，匹配器仅仅返回那些有值(i, j)的匹配，其中的
	# 在A组中有第i个描述子，并且在B组中有第j个描述子作为
	# 最佳匹配。也就是说，这个两个在不同组的特征点彼此匹配。
	# 它提供了一个一致的结果，并且是由D.Lowen在SIFT中提出
	# 的ratio test的很好的替代选择。

	# 一旦它被创建了，那个很重要的方法就是BFMatcher.match()
	# 和BFMatcher.knnMatch()。第一个返回最佳的匹配。第二个
	# 返回了最佳k以上的匹配，这个k是由用户自己定义的。

	# 如同我们使用cv.drawKeypoints()一样绘制关键点，我们
	# 使用cv.drawMatches()来绘制匹配点。它将两幅图像水平的
	# 放在一起，然后从第一张图像绘制线条链接到第二副图像来
	# 显示最佳的匹配。也有函数cv.drawMatchKnn，这函数绘制了
	# 所有的k佳的匹配。

	# 下面来看看SURF和ORB的单独的例子（每个例子中，都使用了
	# 不同的距离测量）

# Brute-Force Matching with ORB Descriptors
	# 在这里我们，来看一个如果在两幅图像中匹配的简单例子。
	# 在这里，有一幅未知图像和一幅训练图像。我们将会尝试使用
	# 特征匹配来在训练图像中找到未知图像的匹配。

	# 我们使用ORB描述子来匹配特征点。

img1 = cv2.imread('box.png',0)          # queryImage
img2 = cv2.imread('box_in_scene.png',0) # trainImage
# Initiate ORB detector
orb = cv2.ORB_create()
# find the keypoints and descriptors with ORB
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

	# 接下来，我们使用距离测绘cv.NORM_HAMMING来创建一个
	# BFCreator对象(因为我们是用ORB所以使用HAMMING)并且
	# 使用交叉检测来得到最佳结果。然后我们使用Matcher.match()
	# 方法来得到两幅图像中的最佳匹配点。我们根据他们的距离
	# 进行降序排序，这样以后最前面的就是匹配最佳的（有最短
	# 距离）。最后我们绘制前十个匹配。
# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
# Match descriptors.
matches = bf.match(des1,des2)
# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)
# Draw first 10 matches.
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None,flags=2)
plt.imshow(img3),plt.show()

# What is this Matcher Object>
	# 通过函数bf.Match(des1, des2)得到返回的结果是一系列
	# 的DMatch对象组合。这个DMatch对象有以下的属性：
		# DMatch.distance描述子之间的距离，越低，越好
		# Dmatch.trainIdx在训练描述子中的下标
		# DMatch.queryIdx在未知描述子中的下标
		# DMatch.imgIdx训练图像的下标

