#morphological transformation are simple operation based on the shape of the image and it performed only in binary image
import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('smarties.png',0)
_,mask=cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)
kernal=np.ones([5,5],np.uint8)
dilation=cv2.dilate(mask,kernal,iterations=2)
erosion=cv2.erode(mask,kernal,iterations=1)
opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal)
close=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal)
mg=cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernal)
th=cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernal)

title=['images','mask','dilation','erosion','opening','closing','mg','th']
image=[img,mask,dilation,erosion,opening,close,mg,th]

for i in range(len(image)):
    plt.subplot(2,4,i+1),plt.imshow(image[i],'gray')
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])

plt.show()




# cv2.imshow('img',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()