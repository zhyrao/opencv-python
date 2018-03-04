#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-04
# @Author  : Joe
# @Version : 

import numpy as np
import cv2
from matplotlib import pyplot as plt 

# Image Segmentation with Watershed Algorithm

# Goal
	# 我们将学习使用分水岭算法来进行图像分割
	# cv2.watershed()

# Theory
	# 任何灰度图都可以看作是地质表面，其中强度高的
	# 地方表示了山峰，强度低的地方表示了低谷。如果
	# 给每个低谷灌入不能颜色的水，当水慢慢涨高的时
	# 候，水会依据不能的山峰的高度将会慢慢的合并起
	# 来。为了避免水的混合，我们在水将合并的地方建
	# 造障碍来阻止不同颜色的水混合。当我们继续灌入
	# 水、建造障碍物，直到所有的山峰都被淹没。那些
	# 创建了的障碍物就是分割的结果。这就是分水岭算
	# 法的原理。

	# link:http://cmm.ensmp.fr/~beucher/wtshed.html

	# 但是这种直接的算法会因为噪声或者其他不规则的行为
	# 将导致图像过度分割。所以OpenCV实现了一个基于标记
	# 的分水岭算法，这里将指出那些山谷是可以合并的，那些
	# 是不可以合并的。这是一个有交互性的图像分割。我们会
	# 给那些我们已知的物体不能的标签。标记那些我们确定
	# 是前景物体或者只有一种颜色（强度）的物体，也标记
	# 那些我们确定是背景或者有另外一种颜色的非物体，最后
	# 对于那些我们不确定的区域做标记，标记为0.这些就是
	# 我们的标记。然后再应用分水岭算法。


# Code
	# 下面的例子我们来看看如何使用距离变换和分水岭算法来
	# 分割邻近的物体

	# 考虑下面的硬币图，所有的硬币都是相互紧靠在一起，即使
	# 对图像作二值化，他们依然是贴在一起的
img = cv2.imread('water_coins.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+ cv2.THRESH_OTSU)

cv2.imshow('gray',gray)
cv2.imshow('thre', thresh)
	# 现在我们需要去除掉图像中的所有的小的白色噪声点，对于这个
	# 我们使用形态学的开运算。为了去除图像中的所有小洞，我们使用
	# 形态学的闭运算。现在，我们确定靠近物体中心点的区域是前景，
	# 距离物体远的区域是背景。只有硬币的包围区域是不确定的。

	# 所以我们需要提取出我们确定是硬币的区域。腐蚀将去除包围的
	# 像素。 这样以来还存在的物体我们就能肯定是硬币。然而这种情
	# 况只在物体没有贴在一起才有用。但是因为他们是相互贴在一起
	# 的，所以更好的方法是对他们进行距离变换并且应用适当的阈值。
	# 接下来我们需要找到那些我们确定不是硬币的区域。对于这个，
	# 我们扩张结果图像。扩张在背景上增加了物体包围的大小。这样一
	# 来，我们就能确定在扩张后的图像中，背景区域(黑色区域)确定
	# 是背景区域，因为包围区域已经通过扩张移除掉了。如图

	# link:https://opencv-python-tutroals.readthedocs.io/en/latest/_images/water_fgbg.jpg

	# 现在任然存在的区域我们不能断定它是硬币还是背景。那么该分
	# 水岭算法上场了。这些区域通常是硬币的包围位置，这里前景和
	# 背景交互的地方（两个硬币也是），我们成为边界。这个结果可
	# 以通过确定背景图减去确定前景图得到。

# noise normal
kernel = np.ones((3,3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations = 2)

# sure background area
sure_bg = cv2.dilate(opening, kernel, iterations = 3)

# finding sure foreground area
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2,5)
cv2.imshow('dist_transform', dist_transform)
ret,sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)

# find unkown area
sure_fg = np.uint8(sure_fg)
unkown = cv2.subtract(sure_bg, sure_fg)
cv2.imshow('sure_bg', sure_bg)

cv2.imshow('sure_fg',sure_fg)
cv2.imshow('unkown',unkown)

	# 从图像中可以看出，在阈值化图像中，我们得到了一些已经分离开的
	# 硬币的区域。（在一些情况下，你可以仅仅对前景物体分割有兴趣，
	# 不用将贴在一起的物体分离开来。在这种情况下，不需要使用距离变换，
	# 仅仅使用扩张是一一种非常有效率的方式。扩张也是一种提取前景物体
	# 的方法）

	# 现在我们已经知道了哪些区域值硬币，哪些是背景已经其他的区域。所以
	# 我们可以创建标签(是同原始图像大小一致的数组，但是数据类型是int32)
	# 并且将他们进行不同的标记。我们已知确定的区域将赋值给不同的正整数，
	# 那些不知道区域赋值给0.我们可以使用cv2.connectedComponents()函数。
	# 它将图像的背景标记为0，其他的物体将从1开始做标记。

	# 但是我们知道如果将背景标记为0，分水岭算法中将会认为是一个未知的区域。
	# 所以我们想要将它标记为其他不同的整数。同时，我们将标记未知区域为0.

# mark labelling
ret, markers = cv2.connectedComponents(sure_fg)

# add one to all labels so that background is not 0, but 1
markers = markers + 1

# now, mark unkown region as 0
markers[unkown==255] = 0

cv2.imshow('markers',markers)
	
	# 现在从一幅彩色JET图像中看看结果。其中深蓝色的区域是未知区域。确定的硬币区域
	# 被不同的颜色值填充。剩下的是已知的背景区域，它相对于未知区域来使用了浅蓝色。

	# 现在我们的标记信息已经准备好了。是时候进行最后的步骤了，应用分水岭算法。
	# 那么标记图像将会被改变。那些包围的区域将被标记为-1
markers = cv2.watershed(img, markers)

img[markers== -1] = [255, 255,0]
cv2.imshow('watershed', img)

	# 通过图像结果可以看出，对于一些硬币来说，它们紧贴的位置被很好的分割开来，然而
	# 有一些并没有

cv2.waitKey(0)
cv2.destroyAllWindows()