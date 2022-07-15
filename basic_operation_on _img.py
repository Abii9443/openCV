#This file contails how to split, add image, add weight to the image,merge,roi
import numpy as np
import cv2
#to find coordiantes of an image

# def click_event(event,x,y,flags,param):
#     if event==cv2.EVENT_LBUTTONDOWN:
#         print(x,' , ',y)
#         text=cv2.FONT_HERSHEY_SIMPLEX
#         strxy=str(x)+' , '+ str(y)
#         cv2.putText(img,strxy,(x,y),text,1,(255,255,0),1)
#         cv2.imshow('image',img)

img=cv2.imread('test_rp17.jpg')
img2=cv2.imread('test_road.jpg')
img=cv2.resize(img,(512,512))
img2=cv2.resize(img2,(512,512))
b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))
# pic=img[174:51,389:398]
# img[164:45,200:156]= pic
# cv2.rectangle(img,(76,16),(158,183),(0,255,255),4)
# dst=cv2.add(img,img2)
dst=cv2.addWeighted(img,0.8,img2,0.2,0)
cv2.imshow('image',dst)

# cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()