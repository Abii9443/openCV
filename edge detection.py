#using laplacian the image is pretty much detected but the combination of both sobelx and sobel y will make  an accurate level of detection in the image
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('sudoku.png')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
lap=cv2.Laplacian(img,cv2.CV_64F,ksize=3)
lap=np.uint8(np.absolute(lap))
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0)
sobely=cv2.Sobel(img,cv2.CV_64F,0,1)

sobelx=np.uint8(np.absolute(sobelx))
sobely=np.uint8(np.absolute(sobely))
sobel_combine=cv2.bitwise_or(sobelx,sobely)
title=['images','laplacian','sobelx','sobely','combine']
image=[img,lap,sobelx,sobely,sobel_combine]

for i in range(len(image)):
    plt.subplot(2,3,i+1),plt.imshow(image[i],'gray')
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])

plt.show()