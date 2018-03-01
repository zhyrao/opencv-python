#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-01
# @Author  : Joe

import numpy as np
import cv2


# Goal 目标
	# 在这节中，我们来理解霍夫变换的原理
	# 展示如果使用霍夫变换在图像中检测线条
	# cv2.HoughLines(), cv2.HoughLinesP()

# Theory 理论
	# 如果将任何形状用数学方式来表示，霍夫变换
	# 是一个监测这些形状的一个非常流行的方式。
	# 它甚至可以监测有一点破损或者被腐蚀掉的形‘
	# 状。下面我们来看看它是对监测线条是如何工
	# 作的。

	# 一条线可以被表示为 y = m * x + c 或者以参数
	# 形式表示为 p =  x * cos θ  + y * sin  θ ,其中
	# p是指从源点到这条线的垂线的距离， θ 是指
	# 这条垂线与水平线构成的逆时针方向的夹角。
	# 如图：https://opencv-python-tutroals.readthedocs.io/en/latest/_images/houghlines1.svg

	# 所以一条线如果在源点的下面，那么就会有
	# 正值的p，夹角小于180度。如果它是在源点的
	# 上方，我们任然认为夹角是小与180的，但是
	# p是负值。任何竖线的角度为0，任何水平线的
	# 角度为90度。

	# 现在来看看霍夫变换是怎么处理线的。所有的
	# 线都可以被表示为两个值，(p,θ)。所以首先
	# 它创建了一个2维数组或者累加器来存储这两个
	# 值并且初始化全部为0。让行表示为p，列表示
	# 为θ。数组的大小取决于你需要的精度。假设你
	# 需要角度的精度为1度，那么就需要180列。对于
	# p 来说最大的距离可能是图像的斜对角线的长度。
	# 对于1个像素的精度来说，行的数量可能为图像
	# 的对角线长度。

	# 我们拿100x100像素大小的图像来作为例子，假设
	# 在图像的中间有一条线。那么对于这条线上的第一个点，
	# 我们知道它的(x,y)的值。现在代入线性方程中，
	# 将θ的值赋值从0到180，然后检查p的值。对于每一个
	# (p,θ)组，将它的累加器在对应的(p,θ)块中加1。
	# 所以现在在累加器中，块(50，90) = 1.其为0。

	# 现在取线上的第二个值，然后对它作上述的操作。
	# 然后给对应的(p,θ)对应的值加1.这样一来，
	# （p,θ） = 2. 实际上所做的就是给这个(p,θ)增
	# 加值。我们继续这一过程。对于在线上的每一个点
	# 块(p,θ)将会被加1，同时其他的块有可能或者不能
	# 被加1. 这样一来，在最后的时候，块(p,θ)的值将
	# 会是最大的。所以说如果你在累加器中搜索最大的值，
	# 那么你会得到对应的块是(50,90)，也就是说，图像
	# 中存在一条线，它距离源点的距离为50，夹角为90度。
	# link:https://opencv-python-tutroals.readthedocs.io/en/latest/_images/houghlinesdemo.gif

	# 这就是霍夫变换是怎么工作的。很简单，可以使用numpy
	# 来自己实现。下面这副图像中表示了累加器的数据。
	# 最亮点的位置数据表示了在图像中可能对应的是一条
	# 线。
	#link：https://opencv-python-tutroals.readthedocs.io/en/latest/_images/houghlines2.jpg

# Hough Transform in OpenCV
	# 上面解释的内容全部被opencv的函数,cv2.HoughLines()包含。
	# 它简单的返回了一个数组包含(p,θ)的值。p的单位是像素，θ
	# 的单位是弧度。
	# 第一个参数是一个二值化的源图像，所以在霍夫变换之间，我们
	# 需要将图像做阈值化或者做canny边界检测。
	# 第二和第三个参数分别代表了p和θ的精度。
	# 第四个参数是阈值，它表示了被认为是一条线的最低累加值。
	# 记住累加的数值决定于线上的点的个数。所以这个值也表示了
	# 最低多长的线段会被检测到。

img = cv2.imread('sudoku.jpg')
img_o = img.copy()
cv2.imshow("original img", img_o)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize = 3)

lines = cv2.HoughLines(edges, 1, np.pi/180, 120)
for line in lines:
	print(line)
	rho, theta = line[0][0], line[0][1]
	a = np.cos(theta)
	b = np.sin(theta)
	x0 = a * rho
	y0 = b*rho
	x1 = int(x0 + 1000*(-b))
	y1 = int(y0 + 1000*(a))
	x2 = int(x0 - 1000*(-b))
	y2 = int(y0 - 1000*(a))

	cv2.line(img, (x1,y1), (x2,y2), (0,0,255),2)

cv2.imshow("original img", img_o)
cv2.imshow("gray img", gray)
cv2.imshow("edge  img", edges)
cv2.imshow("line img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


