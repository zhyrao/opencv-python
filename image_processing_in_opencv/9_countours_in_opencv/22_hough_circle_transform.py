#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-03
# @Author  : Joe
# @Version : 

import numpy as np
import cv2


# Hough Circle Transform

# Goal 
	# 学习在一幅图像中用霍夫变换找到圆形
	# cv2.HoughCircle()

# Theory
	# 一个圆可以用数学公式表示为：
	# (x - X_center)² + （y - Y_center)² = r²
	# 其中(X_center, Y_center)是这个圆的圆形，r是
	# 这个圆的半径。从公式中可以看出，其中有3个参数，
	# 所以我们在霍夫变幻中需要3个累加器，但是这样来说
	# 是非常不效率的。 所以在OpenCV中使用比较取巧的
	# 方式， 霍夫梯度方法，它使用了边界的梯度信息。

	# 在这里是用的是cv2.HoughCircle()。它有很多的参数，
	# 在文档中提供了详细的解释。

img = cv2.imread('logo.png',0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()