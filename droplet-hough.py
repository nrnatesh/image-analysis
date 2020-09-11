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
import csv
import sys
#from plantcv import plantcv as pcv

image_name = "/home/nrnatesh/shenlab/Droplet-organoid/image-analysis/input_images/T2.tif"
img = cv2.imread(image_name, 1)
img_orig = img.copy()
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.rcParams["figure.figsize"]= (16,9)
plt.imshow(img, cmap='gray')

#img = cv2.GaussianBlur(img, (21,21),  cv2.BORDER_DEFAULT)
#plt.rcParams["figure.figsize"]= (16,9)
#plt.imshow(img, cmap='gray')

all_circs = cv2.HoughCircles(img, 
                             cv2.HOUGH_GRADIENT, 
                             dp = 1, 
                             minDist = 100, 
                             param1= 30, param2 = 25,
                             minRadius = 50, maxRadius = 65)
all_circs_rounded = np.uint16(np.around(all_circs))

print(all_circs_rounded)
print(all_circs_rounded.shape)
print("I have found " + str(all_circs_rounded.shape[1]) + " circles.")

count = 1
for i in all_circs_rounded[0, :]:
    cv2.circle(img_orig, (i[0],i[1]),i[2],(50,200,200),5)
    cv2.circle(img_orig, (i[0],i[1]), 2, (255,0,0),3)
    cv2.putText(img_orig, "Droplet " + str(count), (i[0]-70,i[1]+30), cv2.FONT_HERSHEY_SIMPLEX,1.1,(255,0,0),2)
    count += 1
    
plt.rcParams["figure.figsize"] = (16,9)
plt.imshow(img_orig)
plt.show()

coord = []
for i in all_circs_rounded[0, :]:
    coord.append((i[0],i[1],i[2]))

with open('coordinates.csv', 'w') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(['x','y','r'])
    for row in coord:
        csv_out.writerow(row)
        
#for i in coord:
 #   test = cv2.circle(img, (i[0],i[1]),i[2],(0,0,255),2)
  #  cv2.imshow("test",test)
#cv2.waitKey(0)


#mask = np.zeros(img.shape, dtype = np.uint8)
#test = cv2.circle(img, (coord[0][0],coord[0][1]), coord[0][2], (0,0,255), -1)
#cv2.imshow("test", test)



