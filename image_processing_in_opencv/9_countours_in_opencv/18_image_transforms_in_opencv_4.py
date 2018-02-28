#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-28
# @Author  : Joe

import numpy as np
import cv2

# Performance Optimization of DFT
# DFT的性能优化

# 在离散傅里叶变换中，提高计算性能的途径有
# 关数组的大小。如果数组的大小尺寸是2的平方
# 数，那么计算速度将是最快的。如果数组的大小
# 是2,3,5的倍数，也会对计算速度有很大的提升。
# 所以如果你担心DFT的性能问题，那么在计算DFT
# 之前将数组的大小修改为这些性能快的大小尺寸。
# 在OpenCV中，你必须手动的给0.而在Numpy中
# 只需要指定FFT计算的新的尺寸，numpy会自动
# 帮你补0.

# 那么怎么才能找到这个优化尺寸呢？在OpenCV中
# cv2.getOptimalDFTSize()会得到这个结果。
# 它适应于cv2.dft和np.fft.fft2()。现在来看看
# 他们各自的性能：(IPYTHON)

img = cv2.imread('messi.jpg', 0)
rows, cols = img.shape

print(rows, cols)

nrows = cv2.getOptimalDFTSize(rows)
ncols = cv2.getOptimalDFTSize(cols)
print (nrows, ncols)

# 现在补0
nimg = np.zeros((nrows, ncols), np.uint8)
nimg[:rows, :cols] = img

# OR 
# right = ncols - cols
# bottom = nrows - rows
# bordertype = cv2.BORDER_CONSTANT
# nimg = cv2.copyMakeBorder(img, 0, bottom, 0, right, bordertype, value = 0)
e1 = cv2.getTickCount()
fft1 = np.fft.fft2(img)
e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()
print('Time : ' + str(time))

e1 = cv2.getTickCount()
fft2 = np.fft.fft2(img,[nrows,ncols])
e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()
print('Time : ' + str(time))

e1 = cv2.getTickCount()
dft1= cv2.dft(np.float32(img),flags=cv2.DFT_COMPLEX_OUTPUT)
e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()
print('Time : ' + str(time))

e1 = cv2.getTickCount()
dft2= cv2.dft(np.float32(nimg),flags=cv2.DFT_COMPLEX_OUTPUT)
e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()
print('Time : ' + str(time))

cv2.imshow('original', img)
cv2.imshow('optimal', nimg)

cv2.waitKey(0)
cv2.destroyAllWindows()