# -*- coding:utf-8 -*-
import numpy as np 
import cv2

# link: http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html#display-image
# use function cv2.imread() to read an image.
# cv2.imread(imgpath, flag)
# 这个函数用来读取一副图像，第一个参数是在这个工作目录下的图片或者是一张图片的完全路径
# 第二个参数是指出图片的读取方式
# cv2.IMREAD_COLOR : 默认的方式，除了透明通道舍去外，别的都留下来
# cv2.IMREAD_GRAYSCALE: 灰度图
# cv2.IMREAD_UNCHANGED: 所有图片的原始信息，包括透明通道

# 注意： 可以传递 1, 0, -1来代表这3中方式

# load an color image in grayscale
img = cv2.imread('logo.png', 0) # 确认图片存在

while True:
	cv2.imshow('gray', img) # show image with  a window named 'gray'

	# any key while trigger this
	if cv2.waitKey(0):
		break

# remeber to destroy windows.
cv2.destroyAllWindows()
