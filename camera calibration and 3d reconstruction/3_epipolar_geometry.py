#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-09
# @Author  : Joe

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt 


# Goal
	# 在本节中，
		# 我们将学习多视图几何的基本理念
		# 我们将了解什么是核点，核点线，核点约束等。

# Basic Concepts
	# 当我们使用针孔相机照相的时候，我们失去了一个非常重要的
	# 信息，图像的深度信息。或者说图像中的每个点距离相机多远
	# 的距离，造成的原因是照相的过程是一个从3D转为2D的过程。
	# 所以一个重要的问题就是我们是否能够使用相机来找到深度的
	# 信息。答案就是使用不止一个相机。我们人类的眼睛的原理就
	# 是类似于我们使用两个相机来观察，这种方法叫做立体视觉。
	# 现在来看看OpenCV在这个区域内提供了什么。

	# 在继续深入到图像的深度之前，我们首先来理解下多视图几何
	# 的一些基本理念。在本节中，我们将处理核面几何。下图中展
	# 示了在拍摄同一个场景中两个相机的基本设置情况。
	# link:https://docs.opencv.org/3.4.0/epipolar.jpg

	# 如果我们仅仅使用左边的相机，我们不能找到图像中的点 x对应
	# 的3D点，这是因为所有在线 OX 上的都都会投影到图像平面的同
	# 一个位置。但是如果同时考虑右边的图像。现在在线 OX 中的不
	# 同的店都会在右边的图像平面中投影到不同的位置（x'） 所以
	# 通过这两幅图像，我们可以通过三角分裂来得到3D点。这就是
	# 整个想法。

	# OX线上不同的点在右边平面上投影成一条直线。我们将它称为
	# 关于点x 的epiline。它表示，在右边图像中找这个点，只需要
	# 搜索这条epiline，它应该在这条线中的某个位置(可以这么认
	#  为，为了在其他的图像中找到这个匹配点，你不需要搜寻整个
	# 图像，只需要搜索epiline，这样就能提高性能和精度)。这称
	# 为Epipolar Constraint。同样的所有的点都会在其他的图像中
	# 有与之对应的epiline。平面XOO'被称为Epipolar Plane。

	# O和O'是相机的中心点。从上面的设置我可以得知，右相机O'在
	# 左图像中的投影是点e.它被称为epipole（核点）。核点是连接
	# 两个相机并且与图像平面相交的点。同样的e'是左相机的核点。
	# 在一些情况下，我们可能不能在图像中定位到核点，它们可能
	# 在图像外面（这意味着，相机之间不能看到对方）

	# 所有的epilines都经过核点，所以为了找到核点的位置，我们
	# 可以找到多条epilines然后找到它们的交点。

	# 所以在这里，我们着重在寻找核点以及epilines。但是为了找到
	# 它们，我们需要另外的2个信息，Fundamental Matrix(F)和Essential 
	# Matrix(E).Essential Matrix包含了关于移动和旋转的信息，
	# 它描述了第二个相机在全局坐标系下相对于第一个相机的位置。
	# 如下图：
	# link:https://docs.opencv.org/3.4.0/essential_matrix.jpg

	# 但是我们倾向于使用像素坐标来测量。Fundamental Matrix除了含
	# 有Esstial Matrix的信息之外，还含有两个相机之间的本质关系从
	# 而使我们将两个相机在像素坐标系下关联起来。简单来说，Foundamental 
	# Matrix F映射了一副图像中的点到另外一副图像中的线的关系。这个
	# 是通过计算两幅图像中的匹配点来得到的。

# Code
	# 首先我们需要尽可能的在两幅图像中找到多的匹配点来找到foundamental
	# matrix F. 这个可以使用SIFT 描述器带有基于匹配和比例测试的FLANN来
	# 实现。
img1 = cv.imread('myleft.jpg',0)
img2 = cv.imread('myright.jpg', 0)

sift = cv.xfeatures2d.SIFT_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# FLANN parameters
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)

flann = cv.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des1,des2, k=2)

good = []
pts1 = []
pts2 = []

# ratio test as per love's paper
for i,(m,n) in enumerate(matches):
	if m.distance < 0.8*n.distance:
		good.append(m)
		pts2.append(kp2[m.trainIdx].pt)
		pts1.append(kp1[m.queryIdx].pt)

pts1 = np.int32(pts1)
pts2 = np.int32(pts2)
F, mask = cv.findFundamentalMat(pts1, pts2, cv.FM_LMEDS)

# we select only inlier points
pts1 = pts1[mask.ravel() == 1]
pts2 = pts2[mask.ravel() == 1]

def drawlines(img1, img2, lines, pts1, pts2):
	r,c = img1.shape
	img1 = cv.cvtColor(img1, cv.COLOR_GRAY2BGR)
	img2 = cv.cvtColor(img2, cv.COLOR_GRAY2BGR)

	for r, pt1, pt2 in zip(lines, pts1, pts2):
		color = tuple(np.random.randint(0,255,3).tolist())
		x0,y0 = map(int, [0, -r[2]/r[1]])
		x1,y1 = map(int, [c,-(r[2]+r[0]*c)/r[1]])
		img1 = cv.line(img1,(x0,y0),(x1,y1), color, 1)
		img1 = cv.circle(img1,tuple(pt1), 5, color, -1)
		img2 = cv.circle(img2, tuple(pt2), 5, color, -1)
	return img1, img2

# find epilines corresponding to points in right image(second image)
# and drawing its lines on left image
lines1 = cv.computeCorrespondEpilines(pts2.reshape(-1,1,2), 2, F)
lines1 = lines1.reshape(-1, 3)
print(pts2.shape)
img5, img6 = drawlines(img1, img2, lines1, pts1, pts2)

# find epilines correponding to points in left image(first image)
# and drawing its line on right iamge
line2 = cv.computeCorrespondEpilines(pts1.reshape(-1,1,2), 1,F)
line2 = line2.reshape(-1,3)
img3, img4 = drawlines(img2, img1, line2, pts2, pts1)

plt.subplot(121),plt .imshow(img3)
plt.subplot(122),plt.imshow(img5)
plt.show()
