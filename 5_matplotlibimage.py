#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-02
# @Author  : Joe

import numpy as np
import cv2
from matplotlib import pyplot as plt 

img = cv2.imread('logo.jpg', 1)

# NOTE: opencv load image as BGR mode but matplotlib show an image as RGB mode 
# so we need to convert color to right mode then show it
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
#plt.xticks([]),plt.yticks([]) # to hide tick values on X and y axis
plt.show()