#smoothening means blurred the image
import sys

import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('test_rp17.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
kernal=np.ones([5,5],np.float32)/25
dst=cv2.filter2D(img,-1,kernal)
blur=cv2.blur(img,(5,5))
gblur=cv2.GaussianBlur(img,(5,5),0) # random assignt weights in x and y direction
median=cv2.medianBlur(img,5) # assignemnt weightsd based on the median to the neighbour pixels
bilaterl_blur=cv2.bilateralFilter(img,9,75,75) #best filter to detect the edge
title=['images','convolute img','blur','gaussian blur','median','bilateral']
image=[img,dst,blur,gblur,median,bilaterl_blur]

for i in range(len(image)):
    plt.subplot(2,3,i+1),plt.imshow(image[i],'gray')
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])

plt.show()

