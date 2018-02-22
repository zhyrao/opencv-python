#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-21
# @Author  : Joe
# @Version : 

import numpy as np
import cv2

# Link:https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_contours/py_contours_hierarchy/py_contours_hierarchy.html#contours-hierarchy
# Contours Hierarchy 轮廓的层次结构

# Goal 目标
	# 理解轮廓的层次结构，例如：轮廓中的父-子 关系

# Theory 理论
	# 在前面的几章关于轮廓的文章中，我们使用一些由
	# OpenCV提供的关于轮廓的接口函数。在是用函数
	# cv2.findContours()中，传入了一个参数，Contour
	# Retrieval Mode。通常是cv2.RETR_LIST或者cv2.
	# RETR_TREE。这些参数是什么意思呢？

# What is Hierarchy? 什么是层级结构
	# 通常我们使用cv2.findContours()来在图像中检测
	# 物体。一般情况下，多个物体可能在不同的位置。但
	# 是在一些情况下，一些形状是另外一些形状的内部。
	# 类似嵌套。在这种情况下，我们认为外层的是父节点，
	# 内层的是子节点。这样，图像中的轮廓相互之间有了
	# 层级关系。

	# 看link中的图

	# 在图像中，已经给物体标出了编号从0-5。 2和2a表示
	# 最外层轮廓中的外层和内层。
	# 在这里，轮廓0，1，2,是外层或者最外面。我们可以说
	# 他们是层级-0或者简单来说他们是在同一个层级的。
	# 接下来是轮廓-2a，它可以认为是轮廓-2的子节点（相
	# 反的来说，轮廓-2是轮廓-2a的父节点）。所以我们
	# 标注为层级-1。 同样的对于轮廓-3来说它是轮廓-2的
	# 子节点。最后轮廓4,5是轮廓-3a的子节点，并且他们是
	# 最后一个 层级。从图中可以看出，可以指定轮廓-4为轮
	# 廓-3a的第一个子节点（也可以是轮廓-5）

	# 上面提到了很多术语如：同等层级、外层轮廓、子轮廓、
	# 父轮廓、第一子节点等等。下面带入OPENCV

# Hierarchy Respresentation in OpenCV OpenCV中的层级表现
	# 每个轮廓都有自己的关于层级的信息：多少层级？子节点？
	# 父节点等等。在Opencv中，表示为一个4个值得数组:
	# [Next, Previous, First_Child, Parent]
	# [下一个兄弟节点，前一个兄弟节点，第一个子节点，父节点]
		
		# “Next denotes next contour at the same hierarchical level.”
	# 例如，在图像中取轮廓-0作为例子。那么下一个同层级的兄弟
	# 节点是谁？ 轮廓-1是。这样Next = 1. 同理对轮廓-1来说，同
	# 层级的下一个节点是轮廓-2，所以Next = 2.

	# 对于轮廓-2 呢？ 它没有同层级的下一个节点，那么Next = -1.
	# 轮廓-4呢？同层级的有轮廓-5，那么指定它的下一个兄弟节点
	# 是轮廓-5， Next = 5

		# Previous denotes previous contour at the same hierarchical level.
	# 原理跟Next一样。轮廓-1的前一个节点是轮廓-0. 对轮廓-2来说
	# 前一个是轮廓-1. 轮廓-0的前一个节点为空，那么它的Previour = -1

		# “First_Child denotes its first child contour.”
	# 第一个子节点
	# 对于轮廓-2来说，它的子节点是轮廓-2a。所以第一个子节点为
	# 轮廓-2a的下标值。对于轮廓-3a来说它有2个子节点。但我们只需要
	# 一个节点作为第一个子节点，轮廓-4. 所以 First_Child = 4.

		# “Parent denotes index of its parent contour.”
	# 父节点指的是轮廓的父轮廓
	# 跟第一子节点相反。对于轮廓-4和轮廓-5来说，他们的父节点
	# 就是轮廓-3a. 对于轮廓-3a来说，它的父节点就是轮廓-3.

	### 注意：如果没有子节点或者父节点，值为-1


