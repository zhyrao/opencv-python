#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-18
# @Author  : Joe

import numpy as np
import cv2


# Contour Properties 轮廓的属性

# 在这里，我们了解一些经常使用的物体的属性
# 例如， Solidity, Equivalent Diameter,
# Mask Image, Mean Intensity等。
# 注意：Centroid,Area,Perimeter等也属于
# 这个类别，但是我们已经在前面了解过了。

# 1. Aspect Ratio 纵横比/宽高比
	# 对象的包围矩形的宽度对比高度的比例
	# Aspect Ratio = Width / Height

	# x,y,w,h = cv2.boundingRect(cnt)
	# aspect_ratio = float(w) / h

# 2. Extent
	# Extent是轮廓的面积对比物体的包围矩形面积
	# Extent = Object Area / Bounding Rectangle Area

	# area = cv2.contourArea(cnt)
	# x,y,w,h = cv2.boundingRect(cnt)
	# rect_area = w*n
	# extent = float(area) / rect_area

# 3. Solidity
	# Solidity 是轮廓面积对比凸包面积
	# solidity = Contour Area / Convex Hull Area

	# area = cv2.contourArea(cnt)
	# hull = cv2.convexHull(cnt)
	# hull_area = cv2.contourArea(hull)
	# solidity = float(area) / hull_area

# 4. Equivalent Diameter
	# 是轮廓的面积等于轮廓包围圆直径
	# Equivalent Diameter = sqrt（ 4 * Contour Area / π）

	# area = cv2.contourArea(cnt)
	# equi_diameter = np.sqrt(4*area/np.pi)

# 5. Orientation 方向
	# Orientation 是物体对象相对于直线的角度。 这个方法
	# 同时也返回了长轴和短轴的长度

	# (x,y), (Ma, ma), angle = cv2.fitEllipse(cnt)

# 6. Mask and Pixel Points 遮罩和像素点
	# 在某些情况下，我们需要组成物体对象的所有像素点

	# mask= np.zeros(imggray.shape, np.uint8)
	# cv2.drawContours(mask, [cnt], 0, 255, -1)
	# pixelPoints = np.transpos(np.nonzero(mask))
	# pixelPoints = cv2.findNonZero(mask)

# 7. Maximum Value, Minimum Value and their locaitions 最大最小值
	# 可以在mask里面找到这些值

	# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(imggray, mask = mask)

# 8. Mean Color or Mean Intensity 
# 平均颜色和灰度
	# 通过mask可以找到图像的平均颜色或者平均灰度

	# mean_val = cv2.mean(img, mask = mask)

# 9. Extreme Points 极点
	# 极点是指物体的最上、最下、最左、最右点

	# leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
	# rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
	# topmose = tuple(cnt[cnt[:,:,1].argmin()][0])
	# bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])