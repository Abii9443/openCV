import cv2
import numpy as np

img=np.zeros([512,512,3],np.uint8)
img= cv2.rectangle(img,(76,16),(158,183),(255,255,255),-1)
img2=np.zeros([512,512,3],np.uint8)
img2= cv2.rectangle(img2,(76,16),(450,130),(255,255,255),-1)

# bitAnd=cv2.bitwise_and(img,img2)

# bitOr=cv2.bitwise_or(img,img2)
bitExor=cv2.bitwise_xor(img,img2)

cv2.imshow('image',img)
cv2.imshow('image1',img2)
# cv2.imshow('bitand',bitAnd)
cv2.imshow('bitand',bitExor)
cv2.waitKey(0)
cv2.destroyAllWindows()