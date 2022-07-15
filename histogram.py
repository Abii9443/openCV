import cv2
import numpy as np
from matplotlib import pyplot as plt
# img=np.zeros([200,200],np.uint8)
# cv2.rectangle(img,(0,100),(200,200),(255),-1)
# cv2.rectangle(img,(0,50),(100,100),(255),-1)
img=cv2.imread('test_rp17.jpg',1)
# b,g,r=cv2.split(img)
# cv2.imshow('img',img)
# plt.hist(img.ravel(),255,[0,255])
# plt.hist(b.ravel(),255,[0,255])
# plt.hist(g.ravel(),255,[0,255])
# plt.hist(r.ravel(),255,[0,255])

hist=cv2.calcHist([img],[1],None,[256],[0,256])
# cv2.imshow('img',hist)
plt.plot(hist)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()