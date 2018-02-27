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

	# 对于一个正弦函数信号, x(t) = Asin(2π ft),
	# 我们可以认为 f 是信号的频率，如果在 f 的整个
	# 值域中，我们会看到在 f 位置有峰值。如果这个
	# 信号是从一个离散信号中采样的，我们会得到一
	# 个相同的频域，但是是一个周期性的，在[-π, π]
	# 或者[0, 2π]之间。你可以认为一幅图像是从两个
	# 方向采样的信号。所以通过在X和Y方向对图像进行
	# 傅里叶变换会得到这幅图像的频率表现。

	# 更直观的来说，对于正弦信号来说，如果振幅变动
	# 在短时间内非常快，那么就可以认为是一个高频信号。
	# 如果变动很慢，那么就是要给低频信号。我们可以
	# 将这个理念扩展到图像中。那么在图像中，哪里是
	# 振幅会激烈变化的呢？答案是在边界或者噪声的地方。
	# 所以我们可以认为，在一副图像中，噪声和边界是
	# 属于高频组件。如果内容在振幅上没有特别大的变
	# 化，那么认为它是属于低频组件的。
	

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