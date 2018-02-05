#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-03 23:37:30
# @Author  : Joe
# @Version : 

import numpy as np
import cv2


# cv2.add()  	(src1, src2, dst, mask=None) → None
	# 可以直接用opencv的函数直接相加两张图片或者用numpy的 + ： res = img1 + img2
	# 注意两张图片必须有相同的depth和type，或者第二张图片只是左右scalar值

	# Note:
			# OenCV和numpy相加的结果是不一样的
			# OpenCV采用截取法： 值超过255的取值为255
			# numpy采用求余法； 两个值相加并且对256求余 
x = np.uint8([250])
y = np.uint8([10])

res_cv = cv2.add(x,y)
print(res_cv)

res_np = x + y
print(res_np)


#It will be more visible when you add two images. OpenCV function will provide a better result. So always better stick to OpenCV functions.

# cv2.addWeighted()		(src1, alpha, src2, beta, gamma, dst) → None
# src1:	第一张图片数组
# alpha: 第一张图片权重比例
# src2: 第二张图片
# beta: 第二张图片权重比例
# dst: 输出数组（保持和输入图片数组有一样的大小和通道数量）
# gamma: 对相加后数值的一个缩放量（scalar）
# dtype： 输出数组可选择的depth；如果两个输入图片数组用同样的depth，
		  #dtype可以设置为-1，这时候于src1.depth()相同

# 公式
		# ds(i) = saturate(src1(i) * alpha + src2(i) * beta + gamma)
