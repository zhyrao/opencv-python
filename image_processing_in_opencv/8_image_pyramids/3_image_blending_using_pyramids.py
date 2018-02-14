#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-14
# @Author  : Joe

import numpy as np
import cv2


# 一个对图像金字塔的运用就是图像的混合。
# 例如， 在图像缝合中，需要将两幅图像缝合
# 在一起，但是由于两幅图像之间的不连续性，
# 看起来很难看。

# 在这种情况下，图像金字塔能够让你进行无缝的
# 拼接。

# 简单步骤：
	# 1. 读入苹果和橘子的图像
	# 2. 找到两幅图像的高斯金字塔（在这里，6）
	# 3. 从高斯金字塔图像中找到拉普拉斯金字塔
	# 4. 对左苹果、右橘子对应的拉普拉斯金字塔进行融合。
	# 5. 最后连接图像的金字塔，重构图像。

A = cv2.imread('apple.jpg')  
B = cv2.imread('orange.jpg')  
# generate Gaussian pyramid for A  
G = A.copy()  
gpA = [G]  
for i in np.arange(6):     #将苹果进行高斯金字塔处理，总共六级处理  
    G = cv2.pyrDown(G)  
    gpA.append(G)  
# generate Gaussian pyramid for B  
G = B.copy()  
gpB = [G]  
for i in np.arange(6):  # #将橘子进行高斯金字塔处理，总共六级处理  
    G = cv2.pyrDown(G)  
    gpB.append(G)  
# generate Laplacian Pyramid for A  
lpA = [gpA[5]]                 
for i in np.arange(5,0,-1):    #将苹果进行拉普拉斯金字塔处理，总共5级处理  
    GE = cv2.pyrUp(gpA[i])  
    L = cv2.subtract(gpA[i-1],GE)  
    lpA.append(L)  
# generate Laplacian Pyramid for B  
lpB = [gpB[5]]  
for i in np.arange(5,0,-1):    #将橘子进行拉普拉斯金字塔处理，总共5级处理  
    GE = cv2.pyrUp(gpB[i])  
    L = cv2.subtract(gpB[i-1],GE)  
    lpB.append(L)  
# Now add left and right halves of images in each level  
#numpy.hstack(tup)  
#Take a sequence of arrays and stack them horizontally  
#to make a single array.  
LS = []  
for la,lb in zip(lpA,lpB):  
    rows,cols,dpt = la.shape  
    ls = np.hstack((la[:,0:cols//2], lb[:,cols//2:]))    #将两个图像的矩阵的左半部分和右半部分拼接到一起  
    LS.append(ls)  
# now reconstruct  
ls_ = LS[0]   #这里LS[0]为高斯金字塔的最小图片  
for i in xrange(1,6):                        #第一次循环的图像为高斯金字塔的最小图片，依次通过拉普拉斯金字塔恢复到大图像  
    ls_ = cv2.pyrUp(ls_)  
    ls_ = cv2.add(ls_, LS[i])                #采用金字塔拼接方法的图像  
# image with direct connecting each half  
real = np.hstack((A[:,:cols/2],B[:,cols/2:]))   #直接的拼接  
cv2.imwrite('Pyramid_blending2.jpg',ls_)  
cv2.imwrite('Direct_blending.jpg',real)  