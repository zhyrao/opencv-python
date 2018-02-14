#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-14
# @Author  : Joe

import numpy as np
import cv2

# 拉普拉斯金字塔是通过高斯金字塔的到来。没有专门的接口函数。
# 拉普拉斯金字塔跟边界图像差不多，大多数的元素都是0。
# 常被用在图像压缩中。

