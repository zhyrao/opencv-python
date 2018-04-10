#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-10
# @Author  : Joe

import numpy as np
import cv2
from matplotlib import pyplot as plt 

# Goal
	# 在本章中，我们将会理解k近邻（KNN）算法

# Theory
	# kNN是监督学习中一个非常简单的分类算法。它的想法就是
	# 搜索测试数据在特征点空间中最近匹配。如下图：
	# link:https://docs.opencv.org/3.4.0/knn_theory.png

	# 在这个图中，有两个家族，蓝色方块和红色三角。我们称每
	# 个家族为类(Class).他们的小镇地图上显示了他们的房屋分
	# 布，称为特征空间。*（你可以认为特征空间就是所有的数据
	# 都被投影到的这个空间。例如，考虑一个2D坐标系空间，每个
	# 数据有两个特征，x和y坐标。那么你就可以在2D坐标空间中表
	# 示你的数据。现在想想如果它们有3个特征点，那么你需要3D
	# 空间。我们接着考虑N个特征点，这里你就需要N-维度的空间。
	# 这个N-维度的空间就是特征空间。在我们的图像中，可以认为
	# 是一个2D情况下，只有两个特征点）。

	# 现在一个新的成员来到了小镇然后建了一所新房子，在图中表示
	# 为绿色圆形。他应该加入其中的一个家族（蓝色或者红色）。我
	# 们称这个过程为分类。那么我们怎么做呢？既然我们在学习kNN
	# 那么我们就在这个问题上使用kNN算法。

	# 一个方法是来检查谁是他最近的邻居。从图中可以看出，最近的
	# 明显是红色三角。所以他应该加入红色三角家族。这个方法就是
	# 简单的最近邻居法，因为这个分类只是仅仅依据最近的一个邻居
	# 来划分。

	# 但是这里有个问题。红色三角是最近的一个，但是如果相比较而
	# 言有更多的蓝色方块邻近他呢？那么蓝色方块在位置上拥有比红
	# 色三角更多的强度。所以仅仅检查最近的一个是不充分的。替而
	# 代之的是我们监测  k个邻近的家庭。那么谁有更多的数量，这个
	# 新新就属于这个家族。在我们的图中，如果选择  k = 3，有3个邻
	# 近的家庭。他有两个红色和一个蓝色（其中有两个蓝色是一样距
	# 离的，因为k=3，我们仅仅取其中的一个），那么再次看来他应该
	# 加入红色家族。但是如果我们规定k=7呢？现在他有个蓝色家庭和
	# 2个红色家庭。太好了！他现在应该加入蓝色家庭。所以这些变化
	# 都在于k值的改变，如果k=4呢？他有2个红色和2个蓝色邻居。那么
	# 这里就卡住了。所以最好k取值为一个奇数值。这样的方法被称为k-
	# 近邻算法因为它的分类依靠k个邻近的邻居。

	# 再来看着个问题，在kNN算法中，我们是考虑了附近的k个邻居，但
	# 是我们给这些邻居的重要性是一样的，这样公平么？举例来说，在
	# k值等于4的时候。我们已经知道这个是个死局。但是再来看看，其
	# 中的2个红色家庭比2个蓝色家庭距离新家庭更近。所以他加入红色
	# 家族更合适。那么我们怎么从数学方式上来解释这个问题呢？我们
	# 首先根据每个家庭距离新来家庭的距离给他们一个权重值。对于那
	# 些更接近的家庭将获得更高的权重而那么比较远的家庭只有较少的
	# 权重。然后我们将每个邻近范围内的家族中的家庭权重全部加起来，
	# 最后哪个家族有更高的权重，那么新来的家庭就加入哪个家族。这
	# 就是改良版本的kNN。

	# 那么我们在这里看到了什么重要的信息呢？
		# 首先，我们需要整个小镇所有的房屋的信息。因为我们需要监测
		# 所有的已经存在的房屋对于新来的距离来确定最近的邻居。如果
		# 存在很多的房屋和家庭，那么将耗费很多内存和时间来计算。

		# 对于训练和准备几乎是没有时间的。
	# 现在来看看OpenCV中knn

# kNN in OpenCV
	# 在这里我们只处理一个简单的例子，跟上面一样只有两个家族(类)。
	# 然后在下章中，我们将处理更为复杂的例子。

	# 在这里，我们标记红色家族为Class-0（表示为0），蓝色家族为
	# Class-1（表示为1）。我们创建25个家庭或者25个训练数据，然
	# 后标记它们为class-0或者class-1.我们通过使用numpy的随机数
	# 来获得这些数据

	# 然后我们通过matplotlib来展示这些数据，其中红色三角代表红色
	# 家族，蓝色方块代表蓝色家族。

# feature set containing (x,y) values of 25 known/training data
trainData = np.random.randint(0,100,(25,2)).astype(np.float32)

# labels each one either red or blue with numbers 0 and 1
responses = np.random.randint(0,2,(25,1)).astype(np.float32)

# take red families and plot them
red = trainData[responses.ravel()==0]
plt.scatter(red[:,0],red[:,1], 80,'r','^')

# take blue families and plot them
blue = trainData[responses.ravel()==1]
plt.scatter(blue[:,0],blue[:,1],80,'b','s')

#plt.show()

# 这里将看到和我们上面例子中的图像差不多的结果。因为使用随机数来生成数据，
# 所以每次运行的时候都会得到不同的数据。

# 接下来初始化kNN算法然后将训练数据和标记数据传入给kNN算法来训练（它生成
# 了一个搜索树）。

# 然后我们将引入一个新来的然后在opencv的帮助下来将他分类为一个家族里面去。
# 在应用kNN之前，我们需要了解测试数据的一些信息（新来的数据）。我们的数据
# 格式应该是一个浮点型的数组，大小为number of testdata * number of features.
# 然后我们找到新来家庭的最近邻居。我们可以制定搜寻多少个邻居。kNN将返回：
	# 1. 新来成员的标记，依据我们了解的kNN原理来划分。如果想使用最近邻居
		# 算法，只需要指定k=1.
	# 2. k-邻近邻居的标记
	# 3. 新来成员到每个相邻邻居的距离

# 现在来看看是怎么工作的，新来成员标记为绿色
newcomer = np.random.randint(0,100,(1,2)).astype(np.float32)
plt.scatter(newcomer[:,0],newcomer[:,1],80,'g','o')

knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE,responses)
ret, results, neighbours, dist = knn.findNearest(newcomer, 4)
print("result: {}\n".format(results))
print("neighbours: {}\n".format(neighbours))
print("distance: {}\n".format(dist))

plt.show()

# 如果有大量的新来的测试数据，只需要传入整个数组。
# 10 new comers
# newcomers = np.random.randint(0,100,(10,2)).astype(np.float32)
# ret,results,neighbours,dist = knn.findNearest(newcomer,3)