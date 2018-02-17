#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-17
# @Author  : Joe

import numpy as np
import cv2

# Converx Hull 凸包

# 凸包与轮廓近似相似，但不同，虽然有些情况下它们给出
# 的结果是一样的。函数cv2.convexHull()可以用来检测
# 一个曲线是否具有凸性缺陷，并能纠正缺陷。一般来说，
# 凸性曲线总是凸出来的，至少是平的。如果有地方凹进去
# 了就被叫做凸性缺陷。例如下图中的手，红色曲线显示了
# 手的凸包，凸性缺陷被双箭头标出来了。


# hull = cv2.covextHull(points[, hull[, clockwise[,returnPoints]]])
# 参数详细信息：
	# points: 传入的轮廓数据
	# hull: 返回值
	# clockwise: 方向标记。 如果是True，凸包为顺时针，
			#如果是是False，那么凸包是逆时针计算。
	# returnPoints: 默认的是True. 返回为轮廓数据中凸包的点列表
				# 如果是False，那么返回的就是轮廓数据中凸包所在的点的
				# 下标。

# hull = cv2.convexHull(cnt)
