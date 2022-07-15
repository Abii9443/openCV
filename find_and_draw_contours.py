import  cv2
import numpy as np
img=cv2.imread('opencv-logo.png')
img=cv2.resize(img,(512,512))
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh=cv2.threshold(gray_img,127,255,0)
contour,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print('no of contour',str(len(contour)))
cv2.drawContours(img,contour,-1,(255,0,255),3)
cv2.imshow('img',img)
cv2.imshow('grey_img',gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()