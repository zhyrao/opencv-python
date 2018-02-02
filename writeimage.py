# _*_ coding:utf-8_*_
import numpy as np 
import cv2

# cv2.imwrite()     #para1 file name    #para2 image information
#  save an image. 


# read as grayscale
img = cv2.imread('logo.jpg', 0) 

cv2.imwrite('gray.jpg', img)