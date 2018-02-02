# _*_ coding:UTF-8 _*_
import numpy as np 
import cv2

# cv2.imshow()  
#  para1: window name (string)
#  para2: 想要显示的图片 the image want to show on the window

# cv2.waitKey()
# 键盘绑定的函数。参数是一个毫秒数。 它将等待指定的毫秒时间键盘事件。在这个特定时间按下任何键，程序将继续
# 如果传入0，它将无限制的等待键盘的敲击。
# 也可以设置为特定的键盘码

# cv2.destroyAllWindows()
# 销毁我们创建的所有的窗口

# cv2.destroyWindow()
#  销毁指定名称的窗口 

# cv2.namedWindow(winname[, flags]) → None
# cv2.namedWindow()  #para1: window name  #para2: flag 窗口属性
# 先创建一个窗口，后面再加载图片
#  CV_WINDOW_NORMAL  可以设置窗口大小
#  CV_WINDOW_AUTOSIZE   默认大小为图片的大小
#  CV_WINDOW_OPENGL   窗口支持OPENGL

img = cv2.imread('logo.jpg', 1)
cv2.imshow('image', img)

cv2.namedWindow('resize',cv2.WINDOW_NORMAL)
cv2.imshow('resize', img)

cv2.waitKey(0)
cv2.destroyWindow('image')
cv2.destroyAllWindows()
