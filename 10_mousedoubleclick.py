#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-02
# @Author  : Joe
# @Version : 

import numpy as np
import cv2


# cv2.setMouseCallback() (windowName, onMouse, param=None) → None
# 步骤： 1. 创建一个回掉函数 2.绑定函数

# mouse callback func
def draw_circle(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDBLCLK:
		cv2.circle(img, (x,y), 100, (255,0,0), -1)


# create black image
img = np.zeros((512,512,3), np.uint8)
# 预先创建一个窗口
cv2.namedWindow('image')
# 将回掉函数绑定到该窗口中
cv2.setMouseCallback('image', draw_circle)

while 1:
	cv2.imshow("image", img)
	if cv2.waitKey(20) & 0xFF == 27:
		break


cv2.destroyAllWindows()