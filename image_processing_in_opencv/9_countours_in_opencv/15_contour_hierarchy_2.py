#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-22
# @Author  : Joe

import numpy as np
import cv2


img = cv2.imread('hierarchy.jpg')
img_Gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_Gray, 127, 255, 0)
# Contour Retrival Mode

# 1. RETR_LIST
	# 这种类型是四个当中最简单的模式。
	# 它简单的返回了图像中包含的所有的轮廓，
	# 但是并没有创建或者组织任何层级关系。
	# 父节点和子节点在这个模式下是一样的，
	# 它们只是轮廓而已。同属于同一个层级。

	# 所以在这里，child --- parent 值都为
	# -1.但是显而易见的是，next和previous
	# 是有值的。

# img_contour, coutours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, 0)
# print(hierarchy)

	#    [[[ 1, -1, -1, -1],
	#         [ 2,  0, -1, -1],
	#         [ 3,  1, -1, -1],
	#         [ 4,  2, -1, -1],
	#         [ 5,  3, -1, -1],
	#         [ 6,  4, -1, -1],
	#         [ 7,  5, -1, -1],
	#         [-1,  6, -1, -1]]]
	#  在这里，每一行代表一个轮廓的信息。
	# 第一行代表了轮廓-0的信息，其中下一个
	# 节点为轮廓1.没有上一个节点，所有
	# previous = -1。 以此类推

# 2. RETR_EXTERNAL 
	# 如果使用了这个模式，仅仅返回了最外层的
	# 轮廓信息(最顶层的轮廓信息，所有的子节点
	# 信息都遗弃)。可以这么说，在这种模式下面，
	# 我们仅仅关心最外层的（最顶层的）信息，
	# 其他的信息不管。

	# 那么在图像中，只有3个轮廓信息是最外层的
	# 轮廓信息。轮廓 0，1，2。
# img_contour, coutours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, 0)
# print(hierarchy)
	# [[[ 1 -1 -1 -1]
	#     [ 2  0 -1 -1]
	#     [-1  1 -1 -1]]]


# 3. RETR_CCOMP
	# 这种模式下面，将返回所有的轮廓信息，并且将他们
	# 组织成为2层级的结构形式。例如，外层的轮廓信息
	# 是属于第一层级结构的。内部的轮廓信息是属于第二
	# 层级结构的。如果在第二层中物体还有包含的物体，
	# 那么将这个被包含的物体为第一层级结构。以此类推

# img_contour, coutours, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, 1)
# print(hierarchy)


# 4. RETR_TREE
	# 最后这种模式是具有详细层级结构关系的模式。它返回了
	# 所有的轮廓并且将它们进行父子关系组合为树状结构。

img_contour, coutours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, 1)
print(hierarchy)

cv2.imshow('img_contour',img_contour)

cv2.waitKey(0)
cv2.destroyAllWindows()