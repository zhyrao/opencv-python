#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-02
# @Author  : Joe
# @Version : 

import numpy as np
import cv2

drawing = False  	# True if mouse if pressed (if button up then false)
draw_mode = True 	# if true, draw rectangle. press 'm' to change mode
ix, iy = -1, -1		# start point (when button just pressed)

# mouse callback func
def draw_stuff(event, x, y, flags, params):
	global ix,iy,drawing, draw_mode # make variable global

	if event == cv2.EVENT_LBUTTONDOWN:	# 鼠标被按下
		drawing = True
		ix, iy = x, y					# 记录当前位置
	elif event == cv2.EVENT_MOUSEMOVE:  # 鼠标拖拽
		if drawing == True:
			if draw_mode == True:		# 矩形
				cv2.rectangle(img, (ix, iy), (x,y), (0, 255, 0), -1)
			else:
				cv2.circle(img, (x,y), 5, (0,0,255), -1)
	elif event == cv2.EVENT_LBUTTONUP:
		drawing = False
		if draw_mode == True:
			cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
		else:
			cv2.circle(img, (x,y), 5, (0,0,255), -1)


# set up image and window
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('mouse')
cv2.setMouseCallback('mouse', draw_stuff)

while True:
	cv2.imshow('mouse', img)
	k = cv2.waitKey(1) & 0xFF
	if k == ord('m'):
		draw_mode = not draw_mode	# bool = !bool 改变绘制模式
	elif k == ord('q'):
		break

# do release
cv2.destroyAllWindows()