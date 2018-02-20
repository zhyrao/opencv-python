#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-20
# @Author  : Joe

import numpy as np
import cv2


# Point Polygon Test
# 来找到一个点距离一个轮廓物体的最短距离。
# 返回一个距离，如果是负值，表示这个点在轮廓
# 的外部，如果是正值，表示这个点在轮廓的
# 内部

dist = cv2.pointPolygonTest(cnt,(50,50),True)

# 在这个函数中，第三个参数是 measureDist.
# 如果是True, 则返回带有符号的距离。 如果是
# False，则返回是否在轮廓的内部、外部或者在
# 轮廓上（ +1, -1, 0）

	# 注意
	# 如果不需要找到确定的距离， 那么第三个参数
	# 最好传入False。 这样是因为如果是距离的话，
	# 需要耗时来计算。 这样的话，能够提升 2-3 倍
	# 的速度