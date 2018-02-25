#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-25
# @Author  : Joe
# @Version : 

import numpy as np
import cv2
from matplotlib import pyplot as plt 

# Fourier Transform 傅里叶变换

# Goal 目标
	# 用OpenCV得到图像的傅里叶变换。
	# 使用Numpy提供的FFT进行优化
	# 傅里叶变换的一些应用

# Theory 理论
	# 傅里叶变换是用来分析各种滤波中的频率特性。
	# 对于图像来说，二维离散傅里叶变换来用于找到
	# 频域。一个更换速度的算法叫做快速傅里叶变换
	# （FFT)，用来计算DFT（二维离散傅里叶变换）。
	

# Numpy中的傅里叶变换
	# 首先我们来看看怎么使用numpy来计算傅里叶变
	# 换。Numpy有一个叫做FFT的包，其中提供了函数
	# np.fft.fft2()来计算傅里叶变换，返回一个复
	# 杂的数组。第一个参数是一个灰度图的图像源。
	# 第二个参数是可选的，这个参数决定了返回数组
	# 的大小。如果这个大小大于源图像的大小，那么
	# 原图像中的空白部分全部为0，然后再进行傅里
	# 叶变换。如果这个大小小于原图像的大小，那么
	# 原图像将被裁减。如果没有传入参数，那么这个
	# 默认为原图像的大小。

	# 当得到结果后，零频率的元素将在左上角。如果
	# 想要将它放到中心，那么就需要将整个结果在上
	# 下两个方向移动N/2个位置。这个可以简单的通过
	# numpy的函数np.fft.fftshit()来完成。一旦得
	# 到了傅里叶变换，那么就可以得到幅度谱。

img = cv2.imread('messi.jpg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()