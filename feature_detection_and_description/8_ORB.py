#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-17
# @Author  : Joe
# @Version : 

import numpy as np
import cv2
from matplotlib import pyplot as plt

# ORB (Oriented FAST and Rotated BRIEF)

# Goal
	# 理解ORB的基本知识

# Theory
	# 作为一个OpenCV的狂热者，最重要的事情就是ORB算法是从OpenCV实验室
	# 出来的。这个算法是Ethan Rublee, Vincent Rabaud, Kurt Konolige
	# 和Gary R. Bradski在2011年在他们的论文"ORB:An Eficient alterna
	# tive to SIFT or SURF"中提出的。如果论文标题所说，这个算法对于SIFT
	# 和SURF来说，在计算消耗和主要在专利上是一个非常好的代替性的选择，是
	# 的SIFT和SURF是有专利的，你如果想要使用它们必须付费，但是ORB是免费
	# 的！

	# ORB基本上是一个FAST关键点检测和BRIEF描述子的融合，同时做了很多修
	# 改提高了性能。首先它使用FAST来找关键点，然后用Harris角点测量来找到
	# 头N个点。还使用金字塔来产生多层级特征，但是问题是FAST不计算方向，
	# 所以旋转不变呢？作者做了如下修改。

	# 它计算定位的角点小块质心的亮度权重，这个角点到质心的向量的方向就是
	# 方向，要改进旋转不变，通过x和y计算应该在圆形区域的半径r，r是这小块
	# 的大小。

	# 现在对于描述子，ORB使用BRIEF描述子，但是我们已经看到了BRIEF对旋转
	# 处理很差，所以ORB做的是按关键点的方向引导BRIEF。对于任何位置(xi, yi)
	# 的n个二进制测试的特征集合。定义一个2xn的矩阵，S包含这些像素的坐标，
	# 然后使用方块的方向θ，它的旋转矩阵被找到，并旋转S得到旋转后的Sθ.

	# ORB把角度离散成2π/30(12度），构建一个预计算BRIEF模式的查找表，
	# 只要关键点方向θ，Sθ的正确集合就会被用来计算它的描述子。

	# BRIEF有一个重要的属性，每个位特征有一个大的变化，差接近0.5.
	# 但是当他和关键点方向一致，它丢失了这个属性变得更加分散。高不
	# 一致使得一个特征值更加有区分姓，因为他对输入的响应更加多样。
	# 另一个想要的属性是有不相关测试，因为每个测试会对结果有贡献，
	# 要解决这个，ORB使用一个贪婪搜索所有可能的二进制测试来找既有
	# 高不一致并且差接近0.5的，如果不相关，结果就被叫做rBRIEF。

	# 对于匹配的描述子，使用了多探针LSH提高传统的LSH。论文说ORB
	# 比SURF和SIFT都快很多并且ORB描述子做的也比SURF好。ORB是一个
	# 低性能设备做全景拼接的好选择

# ORB in OpenCV
	# 和通常一样，我们需要用函数cv2.ORB()建立一个ORB对象，或者使
	# 用一个feature2d通用接口。有很多可选参数据，最有用的一个是
	# nFeature，用来指明要保留的特征值的最大数量（默认是500）。
	# scoreType指明是Harris分数或者FAST分数来给特征评分（默认是
	# Harris分数）。另一个参数WTA_K决定要产生有方向的BRIEF描述子
	# 的每个元素的点的数量。默认是2，一次选择两个点。对于匹配，使用
	# NORM_HAMMING距离，如果WTA_K是3或者4，会取3或者4个点来产生
	# BRIEF描述子，然后匹配距离是NORM_HAMMING2.


img = cv2.imread('sample.jpg',0)
# Initiate ORB detector
orb = cv2.ORB_create()
# find the keypoints with ORB
kp = orb.detect(img,None)
# compute the descriptors with ORB
kp, des = orb.compute(img, kp)
# draw only keypoints location,not size and orientation
img2 = cv2.drawKeypoints(img, kp, None, color=(0,255,0), flags=0)
plt.imshow(img2), plt.show()