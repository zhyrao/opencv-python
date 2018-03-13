#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-13
# @Author  : Joe
# @Version : 

import numpy as np
import cv2

# link: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_surf_intro/py_surf_intro.html#surf

# 理论

	# 在前一节，我们看到了SIFT来做关键点检测和描述，但
	# 是它相对来说比较慢，人们需要更快的版本。在2006， 
	# 三个人，Bay，H.，Tuytelaars,T.和Van Gool, L, 
	# 发表了另一篇论文“SURF: Speeded Up Robust Features”
	# 介绍了一个新的算法叫SURF，名字中可以知道，他是加速版的SIFT。

	# SURF用盒子过滤器来近似LoG，下面的图演示了这种近似。一
	# 个很大的好处是用盒子过滤器卷积可以很容易的计算，还可以
	# 在不同尺度并行计算。SURF在尺度和位置上依赖Hessian矩阵的决定。
# OpenCV里的SURF

	# OpenCV提供了SURF函数，你用一些可选条件，比如64/128
	# -维的描述来初始化一个SURF对象，然后做SIFT，我们可以
	# 使用SURF.detect()， SURF.compute()来找关键点和描述。

	# 首先我们会看到一个简单的demo

		# >>> img = cv2.imread('fly.png',0)

		# Create SURF object. You can specify params here or later.
		# Here I set Hessian Threshold to 400
		# >>> surf = cv2.SURF(400)

		# Find keypoints and descriptors directly
		# >>> kp, des = surf.detectAndCompute(img,None)

		# >>> len(kp)
		#  699

	# 1199个关键点太多，我们减少到50好画他们，当
	# 匹配时我们需要所有的特征，所以我们提高Hessian阈值。

		# Check present Hessian threshold
		# >>> print surf.hessianThreshold
		# 400.0

		# We set it to some 50000. Remember, it is just for representing in picture.
		# In actual cases, it is better to have a value 300-500
		# >>> surf.hessianThreshold = 50000

		# Again compute keypoints and check its number.
		# >>> kp, des = surf.detectAndCompute(img,None)

		# >>> print len(kp)
		# 47
	
	# 这比50少了，我们画出它来
		# >>>img2 = cv2.drawKeypoints(img,kp,None,(255,0,0),4)
		# >>> plt.imshow(img2),plt.show()

	# 现在使用U-SURF.
		# Check upright flag, if it False, set it to True
		# >>> print surf.upright
		# False

		# >>> surf.upright = True

		# Recompute the feature points and draw it
		# >>> kp = surf.detect(img,None)
		# >>> img2 = cv2.drawKeypoints(img,kp,None,(255,0,0),4)

		# >>> plt.imshow(img2),plt.show()

	# 看下面的结果，所有的方向都一样了，这比前面的更快，
	# 如果你遇到的是不太关心方向的，这就更好。


	# 最后我们检查描述的大小，如果是64维的话就把它变成128
		# Find size of descriptor
		# >>> print surf.descriptorSize()
		# 64

		# That means flag, "extended" is False.
		# >>> surf.extended
		#  False

		# So we make it to True to get 128-dim descriptors.
		# >>> surf.extended = True
		# >>> kp, des = surf.detectAndCompute(img,None)
		# >>> print surf.descriptorSize()
		# 128
		# >>> print des.shape
		# (47, 128)