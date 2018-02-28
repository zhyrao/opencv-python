#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-28
# @Author  : Joe

import numpy as np
import cv2
from matplotlib import pyplot as plt 

# OpenCV提供了方程cv2.dft() 和cv2.idft()。其
# 返回结果跟numpy的一样，但是带有两个通道。第一个
# 通道是实数的结果，第二个通道里是虚数的结果。在
# 计算之前，输入源图像应转换为np.float32格式。

img = cv2.imread('messi.jpg', 0)

dft = cv2.dft(np.float32(img), flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0], dft_shift[:,:,1]))

# plt.subplot(121),plt.imshow(img, cmap = 'gray')
# plt.title('Input Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
# plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
# plt.show()

# Note: 你也可以使用cv2.cartToPolar()直接得到magnitude和phase

# 现在我们在逆向离散傅里叶变换。在上一节中，我们创建了
# 高通滤波HPF，这一次，我们将使用低通滤波LPF来演示怎么
# 去除图像中的高频率内容。这个操作实际上模糊了图像。这里
# 我们创建了一副遮罩图，其中低频的值为1，高频的值为0

rows, cols = img.shape
crow, ccol = int(rows/2), int(cols/2)

# 创建遮罩图，中心为1，其他为0
mask = np.zeros((rows, cols,2), np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = 1

# 应用遮罩图并且逆向离散傅里叶变换
print(dft_shift.shape, mask.shape)
fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back  = cv2.magnitude(img_back[:,:,0], img_back[:,:,1])

plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_back, cmap = 'gray')
plt.title('Inverse DFT'), plt.xticks([]), plt.yticks([])
plt.show()