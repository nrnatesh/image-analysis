#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 19:06:25 2020

@author: nrnatesh
"""

import cv2
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

image_name = "/home/nrnatesh/shenlab/Droplet-organoid/image-analysis/input_images/T2.tif"
img = cv2.imread(image_name, 1)
img_org = img.copy()
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.rcParams["figure.figsize"]= (16,9)
plt.imshow(img, cmap='gray')

img = cv2.GaussianBlur(img, (21,21),  cv2.BORDER_DEFAULT)