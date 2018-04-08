# -*- coding: utf-8 -*-
# @Date    : 2018-03-21
# @Author  : Joe

import numpy as np
import cv2 
import glob

# Camera Calibration
# Goal
	# 在本节中，
		# 我们将学习什么是相机扭曲，相机的内在和外在的参数等。
		# 我们将学习如何找到这些参数，如何校正图像等。

# Basics
	# 如今使用便宜的针孔相机会给图像造成很多的畸变。两个比较重要的
	# 畸变就是径向畸变和切向畸变。

	# 在径向畸变中，本来的直线会变成圆弧状。并且越接近中心位置，这
	# 个效果越严重。例如，在下面的图片中，可以看到已红色线标记的棋
	# 盘的边界。但是可以清楚的看到边界并不是直线因为它根本就不和红
	# 色直线对齐。所有期望直线的线都膨胀了。
	#link:https://docs.opencv.org/3.4.0/calib_radial.jpg

	# 这个扭曲可以被下面的方程表示：
		# x_distorted = x* (1 + k_1 * r^2 + k_2 * r^4 + k_3 * r^6)
		# y_distorted = y* (1 + k_1 * r^2 + k_2 * r^4 + k_3 * r^6)

	# 同样的，另外一个切向畸变产生的原因是图像产生镜片不是完美的平行
	# 于成像平面。所以有一些地方会比期望的看起来更近一点。
		# x_distorted = x + [2*p_1*x*y + p_2(r^2 + 2 * x^2)]
		# y_distorted = y + [p_1 * (r^2 + 2 * y^2) + 2 * p_2 * x * y]
	# 简单来说，我们需要找到5个参数，它们被称为扭曲系数：
		# Distortion coefficients = (k1,k2,p1,p2,k3)

	# 除了这个以为，我们还需要一些额外的信息，像相机的内在和外在参数。
	# 内在参数是相机特定的，它包含了焦长(f_x, f_y)、光点中心(C_x, C_y)
	# 等信息。内在参数也被称为相机矩阵。它仅仅依据与相机本身，所以一旦
	# 得到了这个信息就可以保存下来以便将来使用。它可以被3x3矩阵表示：
			#					|f_x 	0 	c_x|
			#   camera matrix 	=	|0           f_y    	c_y|
			# 					|0		0	     1|

	# 外在因素表示了旋转和平移，它们将一个3D点转换到一个2D坐标内。

	# 对于立体应用来说，这些扭曲需要首先被校正。为了找到所有的这些参数，
	# 我们需要提供一些已经良好定义了的图像作为模板（例如棋盘）。我们找到
	# 图像中的一些特别的点（期盼中的正方形交点）。我们知道它在真实世界中
	# 的坐标系，我们也知道它在图像中的坐标系。有了这些数据，在后台一些数
	# 学问题会被解决，这样就得到了扭曲系数。这就是所有的总结。为了得到更
	# 好的结果，我们需要至少10个测试模式。

# Code
	# 上面已经提到过了，我们需要至少10个测试模式来校准摄像机。OpenCV提供
	 # 了一些国际象棋棋盘的图像，我们可以利用这些图片。为了更好的理解，我
	 # 们只考虑棋盘的一张图片。摄像机校准中所需要的重要的数据集就是一系列
	 # 的真实世界中3D的点以及其对应的在图片中的2D的点。2D图像中的点可以从
	 # 图片中很容易的找到。（这些图像点就是在棋盘中两个黑色放开互联的地方）

	 # 那么怎么找到真实世界中的3D的点呢？这些图片是采用静止不动的相机拍摄，
	 # 然后棋盘放置在不同的地方和朝向的。所以我们需要知道(X,Y,Z)的值。但是
	 # 简单来说，我们可以说棋盘是保持在XY平面不动的，(所以Z一直=0)而摄像机
	 # 是相应的移动。这样的考虑可以帮助我们仅仅得到了X,Y的值。现在对于X,Y
	 # 值来说，我们可以简单的传入(0,0),(1,0),(2,0),....等表示点位置的值。
	 # 在这种情况下，我们得到的值将会是棋盘方块的缩放值。但是如果我们已经知
	 # 道方块的大小，（比如30mm），然后我们可以传入(0,0),(30,0),(60,0)..
	 # 等值，我们获得的结果也是mm单位的。（在现在的情况下，我们不知道方块的
	 # 大小，所以我们传入在某些条件下的方块大小）。

	 # 3D点被称为 object points（对象点）,2D图像点被称为image points(图像点)

# Setup
	# 所以要找到棋盘的模式，我们需要使用函数，cv.findChessboardCorners().
	# 我们当然也需要传入我们在查找的模式类型，如8x8方格，5x5方格等。在这个例
	# 子中，我们使用7x6方格。（通常棋盘有8x8个方块和7x7个内角点）。它将返回
	# 角点和标记值如果是True表示模式已经获得了。而这些角点将会被排序（从左到
	# 右，从上到下）。

	# see also
		# 这个函数也是不能在所有的图片中找到需要的模式。所以一个比较好的选择
		# 是这样做，启动相机然后在每帧中检查需要的模式。一旦获得了模式，找到
		# 角点并将角点存入一个列表中。也要在读入下一帧之前提供一些回馈值所以
		# 我们能判断棋盘是在不同的方向。继续这样的操作直到获得了所需要的那些
		# 好的模式。即使在我们现在的例子中，我们也不能确定在给予的14张图片中，
		# 有多少是很好的图片。所以我们需要读入所有的图片然后取那些较好的图片使用。

		# 除了棋盘以为，我们也可以使用环形格子，但是需要使用函数cv.findCirclesGrid()
		# 来找到模式。事实表明使用环形格子的时候不需要很多的图片。

# 一旦我们找到了角点，就可以使用cv.cornerSubPix()来提高他们的精确度。我们也
# 可以使用cv.drawChessboardCorners()来绘制模式。如下：

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like(0,0,0) (1,0,0)(2,0,0)...(6,5,0)
objp = np.zeros((6*7, 3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)

# arrays to store object points and 
# image points from all the images
objpoints =[] # 3d points in read world space
imgpoints =[] # 2d points in image space

images = glob.glob('*.jpg')

cameraInfo =[]

for fname in images:
	img = cv2.imread(fname)
	print(fname)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# find the chess board corners
	ret, corners = cv2.findChessboardCorners(gray, (7,6), None)

	# if found, add object points, image points(after refining them)
	if ret == True:
		objpoints.append(objp)
		corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
		imgpoints.append(corners)
		ret_1, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints,gray.shape[::-1],None,None)
		np.savez('B.npz', mtx=mtx,dist=dist,rvecs=rvecs,tvecs=tvecs)
		h,w = img.shape[:2]
		#print(img.shape[:2])
		newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))
		
		# undistort
		# 1. using cv.undistort()
		#dst = cv2.undistort(img,mtx,dist,None, newcameramtx)

		# 2. using remapping 
		mapx, mapy = cv2.initUndistortRectifyMap(mtx, dist, None, newcameramtx,(w,h), 5)
		dst = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)

		# crop the image
		x,y,w,h=roi
		print(roi)
		dst = dst[y:y+h,x:x+w]
		#print(dst.shape)
		# draw and display the corners
		cv2.drawChessboardCorners(img, (7,6), corners2, ret)
		if dst.shape[0] is not 0:
			cv2.imshow("dst",dst)
			cv2.imwrite('dst.png',dst)
		cv2.imshow('img',img)
		
		cv2.waitKey(5000)

cv2.destroyAllWindows()
