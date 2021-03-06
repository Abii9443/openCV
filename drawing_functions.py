import numpy as np
import cv2

# img=cv2.imread('test_road.jpg',1)
img=np.zeros([512,512,3],np.uint8)
img=cv2.line(img,(0,0),(255,255),(0,255,0),10)

img= cv2.arrowedLine(img,(0,255),(255,255),(255,0,0),10)

img=cv2.rectangle(img,(380,0),(520,150),(0,0,255),10)
img=cv2.circle(img,(450,70),60,(0,255,0),-1)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()