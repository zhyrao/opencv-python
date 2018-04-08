#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-08
# @Author  : Joe

import numpy as np
import cv2
import glob


# Goal 
	# 在本节中，我们将利用calib3d模块在图像中创建一些3D效果。

# Basics
	# 这节将会是一个很小的章节。在上节的摄像机校正中，已经得到了
	# 相机的矩阵，扭曲的系数等。给定一副模式图像，我们可以利用上
	# 述的信息来计算它的姿势，或者物体在空间中是怎么样的，例如它
	# 的旋转，怎么展示的等。对于一个平面物体，我们可以假设 Z = 0,
	# 这样的话，问题现在就变成了相机是怎么放置的从而来得到我们的
	# 模式图像。所以如果我们知道这个物体在空间中的样子，我们可以
	# 绘制一些2D图标来模拟3D效果。我们来看看是怎么操作的。

	# 我们的问题就是，我们想在棋盘板的第一个角点上绘制3D坐标轴
	# （X,Y,Z轴）。X轴是蓝色，Y轴是绿色，Z轴是红色。所以在绘制
	# 结果中看来，Z轴应该是垂直与棋盘板的。

	# 首先，我们从上节内容中加载相机矩阵和扭曲系数。
# # load previously saved data
with np.load('B.npz') as X:
	mtx, dist, _,_ = [X[i] for i in ('mtx', 'dist', 'rvecs', 'tvecs')]

def draw(img, corners, imgpts):
	corner = tuple(corners[0].ravel())
	img = cv2.line(img, corner, tuple(imgpts[0].ravel()), (255,0,0), 5)
	img = cv2.line(img, corner, tuple(imgpts[1].ravel()), (0,255,0), 5)
	img = cv2.line(img, corner, tuple(imgpts[2].ravel()), (0,0,255), 5)
	return img

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
objp = np.zeros((6*7, 3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)

axis = np.float32([[3,0,0],[0,3,0],[0,0,-3]]).reshape(-1,3)

for fname in glob.glob('left*.jpg'):
	img = cv2.imread(fname)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	ret, corners = cv2.findChessboardCorners(gray, (7,6),None)

	if ret == True:
		corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
		# Find the rotation and translation vectors.
		ret,rvecs, tvecs = cv2.solvePnP(objp, corners2, mtx, dist)

		# project 3D points to image plane
		imgpts, jac = cv2.projectPoints(axis, rvecs, tvecs, mtx, dist)

		img = draw(img,corners2,imgpts)
		cv2.imshow('img',img)
		k = cv2.waitKey(0) & 0xFF
		if k == ord('s'):
			cv2.imwrite(fname[:6]+'.png', img)

cv2.destroyAllWindows()