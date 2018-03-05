#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-05
# @Author  : Joe
# @Version : 

import numpy as np
import cv2
from matplotlib import pyplot as plt 

# Interactive Foreground Extraction using Grabcut Algorithm

# Goal
	# 理解GrabCut算法的原理
	# 使用这个算法

# Theory
	# GrabCut 算法是有英国微软研究院的Carsten Rother, Vladimir
	# Kolmogorov 和 Andrew Blake 设计的。
	# paper link：http://dl.acm.org/citation.cfm?id=1015720
	# 这个算法可以用来做最小程度用户交互的前景提取。

	# 那么它在用户的眼中是怎么工作的呢？最初的时候，用户需要在图像
	# 中关于前景的部分画一个矩形（前景区域必须完全被矩形包围）。然
	# 后算法开始迭代分割来得到更好的结果。但是在有些情况下，这个分
	# 割的结果不是很好，例如，它可能会将某些前景区域标记为背景区域
	# 等等。在这种情况下，用户需要定义一些规则(touchups)。只需要在
	# 图中出错的部位描画几笔。这些笔画基本上是指"嘿，这些区域应该是
	# 前景区域，但是你却标记成了背景区域，下次迭代的时候要修正"或者
	# 相反。那么，在下一次的迭代中，就能得到更好的结果。

	# 在下面的图像中，球员messi和足球都在蓝色的包围矩形内。还有一些
	# 白色的笔画表示前景和一些黑色的笔画表示背景。结果很不错。

	# link:https://opencv-python-tutroals.readthedocs.io/en/latest
	# /_images/grabcut_output1.jpg

	# 那么后台是怎么处理的呢？
		# 用户输入矩形。任何在矩形外的都会被认为是确定的背景（这就是
		# 原来提到的为什么一定要包围整个前景的原因）。在包围矩形内的
		# 东西是未知的。同样的，任何用户已经指定的前景或者背景都会被
		# 认为是硬标记，这些硬标记在处理的过程中保持不变。

		# 通过我们有点信息将图像作初始化的标记。它会标记前景和背景的
		# 像素（或者硬标记）。

		# 现在运用高斯混合模型对前景和背景进行建模

		# 依据我们设定的数据信息，高斯混合模型学习和创建新的像素分布。
		# 结果就是那些未知区域的像素依据和其他硬标记的像素在颜色统计的
		# 概率上标记为可能前景和可能背景。（很像聚类）

		# 在这个新的像素分布上建立了一副图。其中的节点就是像素。额外还
		# 有两个节点，Source Node 和 Sink Node。所有的前景像素都被连接
		# 到source node，所有的背景像素都被连接到sink node。

		# 连接 source node 和sink node边缘的像素的权重是这个像素属于前景
		# 或者背景的几率。像素之间的权重是通过边界信息或者像素相似度来决
		# 定的。如果它们之间在颜色上有很大的差别，那么他们之间就是一个比
		# 较低的权重。

		# 然后在这个图中使用 mincut 算法。它会把这个图用最小的函数消耗来
		# 分割为source code 和 sink code。在裁剪之后，所有连接到source code
		# 的像素就是前景，所有连接到sink code的像素就是背景。

		# 持续这个过程知道分类完成。

		# img link:http://www.cs.ru.ac.za/research/g02m1682/

		