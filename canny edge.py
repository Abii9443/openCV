#detect wide range of edges in images
#5 steps
#Noise reduction
# Gradient calculation
#Non-maximum suppression
#Double threshold
#Edge tracking hysteresis
import cv2
import numpy as np
from matplotlib import pyplot as plt
def nothing(x):
    pass

cv2.namedWindow('Track')

cv2.createTrackbar('th1','Track',10,400,nothing)
cv2.createTrackbar('th2','Track',10,400,nothing)



while (1):
    img = cv2.imread('test_rp17.jpg', 0)
    pos_th1 = cv2.getTrackbarPos('th1', 'Track')
    pos_th2 = cv2.getTrackbarPos('th2', 'Track')
    edge=cv2.Canny(img,pos_th1,pos_th2)
    cv2.imshow('img',edge)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break;

title=['images','canny']
image=[img,edge]

for i in range(len(image)):
    plt.subplot(1,2,i+1),plt.imshow(image[i],'gray')
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])

