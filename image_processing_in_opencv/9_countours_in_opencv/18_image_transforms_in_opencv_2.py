#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-27
# @Author  : Joe

import numpy as np
import cv2
from matplotlib import pyplot as plt 

# 现在我们得到了傅里叶变换的频域，那么
# 就可以在这个频域上进行一些操作，像：
# 高通滤波和重组图像，例如找到DFT的反向。
# 我们用一个大小为60x60的矩形来移除掉低
# 频的内容，然后进行反向移动 np.fft.ifftshift()
# 这样DC位置又移动到左上角了。接下来我们用
# np.ifft2()得到FFT的反向内容。其结果也是
# 复数。我们可以取它的绝对值。


img = cv2.imread('messi.jpg', 0)

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

rows, cols = img.shape
print(img.shape)
crow, ccol = int(rows/2), int(cols/2)
fshift[crow-30:crow+30, ccol-30:ccol+30] = 0
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_back)
plt.title('Result in JET'), plt.xticks([]), plt.yticks([])

plt.show()

# 结果显示了高通滤波是一个边缘检测算法。我们
# 已经在图像梯度章节中了解过了。这里还显示了
# 图像的低频内容。

# 如果你近距离的仔细看JET的结果图像，你会发现
# 一些缺点。它很像一些涟漪的波纹，我们称为振铃
# 现象。这种现象是因为我们采取了矩形的遮罩图。
# 从这里也可以得到矩形的遮罩图不适合对图像进行
# 模糊，较好的方式是采用高斯窗口。