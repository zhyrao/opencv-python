#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-09
# @Author  : Joe

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt 


# Goal
	# 在本节中，我们将学习从双目图像中创建深度图

# Basics
	# 在上节中，我们看到了一些基本的概念如核点约束以及
	# 其他的相关内容。我们也看到了如果我们有同样场景的
	# 两幅图像，我们可以从图像中直观的获取到深度的信息。
	# 下面是一幅图像和一些数学公式显示了这个过程：
	# link:https://docs.opencv.org/3.4.0/stereo_depth.jpg

	# 上面的图像中有一个等边三角形。等效方程如下：
		# disparity = x - x' = Bf/Z

	# x和x'是场景中的点对应到平面上的点到他们相机中心的距离。
	# B是两个相机之间的距离（已知），f是相机的焦距（已知）。
	# 所以，上面的等式说一个点在场景里的深度和对应图像点和他
	# 们摄像机中心点的距离差成反比。有了这个信息，我们可以得
	# 出图像里所有像素的深度。

	# 所以它在两个图像里找对应的匹配点。我们已经看到了极线约
	# 束会让这个运算快捷和准确，当它找到了匹配，它也就找到了
	# 视差，让我们看看用OpenCV怎么做

# Code
imgL = cv.imread('tsukuba-l.png',0)
imgR = cv.imread('tsukuba-r.png',0)

stereo = cv.StereoBM_create(numDisparities = 16, blockSize = 29)
disparity = stereo.compute(imgL,imgR)
plt.imshow(disparity,'gray')
plt.show()