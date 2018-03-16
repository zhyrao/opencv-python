#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-16
# @Author  : Joe

import numpy as np
import cv2
from matplotlib import pyplot as plt

# BRIEF (Binary Robust Independent Elementary Features)

# Goal 
	# 学习BRIEF的基本概念

# Theory	
	# 我们知道SIFT使用128维度的向量作为描述。因为它使用了浮点数，
	# 所以基本上也要使用512个字节。同样的SURF也是最小的使用了256
	# 个字节（64维度）。如果给上千个特征点创建这样的向量将会使用
	# 大量的内存，这样对于一些有资源限制的、特别是嵌入式的系统来
	# 说是不可行的。并且越大的内存将会使用越长的时间来匹配。

	# 在实际的匹配当中，这么多所有的维度并不是必须的。我们可以使
	# 用多种方式来压缩，例如PCA,LAD等。即使其他的方式例如hashing
	# 使用LSH（locality sensitive hasing）来将这些SIFT描述子从
	# 浮点数转换为二进制字符串。这些二进制的字符串会使用Hamming 
	# Distance来进行特征点匹配。这样就提升了很大的速度，因为hamming
	# distance只是进行了XOR和位运算，这种类型的运算对于有SSE结构
	# 的现代CPU是非常快速的。但是在这里，我们需要首先找到描述子，
	# 然后在使用hashing，这样一来还是没有解决一开始的内存问题。

	# 这个时候BRIEF出现了。它提供了一个不需要找到描述子就能得到
	# 二进制字符串的捷径。它使用了被平滑过的图像块，然后使用独特
	# 的方式选择了一系列的Nd(x,y)位置对。然后对这些位置上的强度
	# 做对比。例如，让第一个位置中的对位p和q，如果 I(p) < I(q)，
	# 那么结果就为1，否则为0.这样的方式被应用与所有的n个位置对，
	# 然后获得了一个nd-维度的位串。

	# 这个nd可以是128,256,512.OpenCV对他们都支持，但是默认来说
	# 会是256.

	# 一个比较重要的点就是BRIEF是一个特征点描述子，它并不提供任何
	# 找到这些特征点的方式。所以你就将要使用别的特征点检测算法例如
	# SIFT,SURF等。论文推荐使用CenSurE（这是一个快速检测器）和BRIEF
	# 来使用。

#note : that you need opencv contrib) to use this.
# BRIEF in OpenCV
img = cv2.imread('sample.jpg',0)
# Initiate FAST detector
star = cv2.xfeatures2d.StarDetector_create()
# Initiate BRIEF extractor
brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()
# find the keypoints with STAR
kp = star.detect(img,None)
# compute the descriptors with BRIEF
kp, des = brief.compute(img, kp)
print( brief.descriptorSize() )
print( des.shape )