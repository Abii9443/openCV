import cv2
import numpy as np
img=cv2.imread('test_rp17.jpg',0)
gp=img.copy()
gaussian_pyramid=[gp]
# lr1=cv2.pyrDown(img)
# lr2=cv2.pyrDown(lr1)
# cv2.imshow('img',img)
# cv2.imshow('lr1',lr1)
# cv2.imshow('lr2',lr2)
for i in range(6):
    gp=cv2.pyrDown(gp)
    gaussian_pyramid.append(gp)
layer=gaussian_pyramid[5]
lp=[layer]
for i in range(5,0,-1):
    laplacian_pyramid=cv2.pyrUp(gaussian_pyramid[i])
    laplacian=cv2.subtract(gaussian_pyramid[i-1],laplacian_pyramid)
    lp.append(laplacian)
    cv2.imshow(str(i),lp[0])

cv2.imshow('original',img)
cv2.waitKey(0)
cv2.destroyAllWindows()