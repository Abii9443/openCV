#thresholding mean it shows some gradient img with respect to the thresh value which is condition based approach
import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('gradient.png',0)

_,th1=cv2.threshold(img, 127,255,cv2.THRESH_BINARY) #upto 127 black after white
_,th2=cv2.threshold(img, 200,255,cv2.THRESH_BINARY_INV)
_,th3=cv2.threshold(img, 110,255,cv2.THRESH_TRUNC) #upto 110 it same as image after it remains same
_,th4=cv2.threshold(img, 127,255,cv2.THRESH_TOZERO) #upto 127 it will black after white
_,th5=cv2.threshold(img, 127,255,cv2.THRESH_TOZERO_INV)

title=['original img','THRESH_BINARY','THRESH_BINARY_INV','THRESH_TRUNC','THRESH_TOZERO','THRESH_TOZERO_INV']
images=[img,th1,th2,th3,th4,th5]
for i in range(6):
    plt.subplot(3,2,i+1),plt.imshow(images[i],'gray')
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])


#
# cv2.imshow('img',img)
# cv2.imshow('th1',th1)
# cv2.imshow('th2',th2)
# cv2.imshow('th3',th3)
# cv2.imshow('th4',th4)
# cv2.imshow('th5',th5)

#Adaptive thresholding - means the color of the image is more clean than traditional threhold
# img=cv2.imread('test_rp17.jpg',0)
# _,th=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# th1=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
# th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
# cv2.imshow('th',th)
# cv2.imshow('th1',th1)
# cv2.imshow('th2',th2)
#
#
plt.show()
# cv2.waitKey(0)
# cv2.destroyAllWindows()