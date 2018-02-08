#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-07 23:15:04
# @Author  : Joe
# @Version : 

import numpy as np
import cv2


# 2D Convolution (Image Filtering)
# 对于一维的信号，图像可以被各种各样的 低通滤波器(Low pass Filter, LPF)或者 高通过滤器(high pass Filter, HPF) 进行过滤。
# 通常 低通滤波器 过滤可以帮助除掉图像中的噪点或者能够模糊图像， 高通滤波器 可以帮助检测图像中的边缘轮廓
