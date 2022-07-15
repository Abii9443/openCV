#Here these code purpose is to detect the image in both uploading image and video by using hue
import cv2
import numpy as np
def nothing(x):
    pass

cap=cv2.VideoCapture(0)

cv2.namedWindow("Tracking")
cv2.createTrackbar('LH','Tracking',0,255,nothing)
cv2.createTrackbar('LS','Tracking',0,255,nothing)
cv2.createTrackbar('LV','Tracking',0,255,nothing)
cv2.createTrackbar('UH','Tracking',255,255,nothing)
cv2.createTrackbar('US','Tracking',255,255,nothing)
cv2.createTrackbar('UV','Tracking',255,255,nothing)
while True:
    # img=cv2.imread('smarties.png',1)
    _,img=cap.read()
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    LH=cv2.getTrackbarPos('LH','Tracking')
    LS=cv2.getTrackbarPos('LS','Tracking')
    LV=cv2.getTrackbarPos('LV','Tracking')
    UH=cv2.getTrackbarPos('UH','Tracking')
    US=cv2.getTrackbarPos('US','Tracking')
    UV=cv2.getTrackbarPos('UV','Tracking')

    l_b=np.array([LH,LS,LV])
    u_b=np.array([UH,US,UV])
    mask=cv2.inRange(hsv,l_b,u_b)
    res=cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow('img',img)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    key=cv2.waitKey(1)
    if key==27:
        break

cap.release()
cv2.destroyAllWindows()