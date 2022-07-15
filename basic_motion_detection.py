import cv2
import numpy as np
cap=cv2.VideoCapture('vtest.avi')
_,frame1=cap.read()
_,frame2=cap.read()


while cap.isOpened():
    difference=cv2.absdiff(frame1,frame2)
    gray=cv2.cvtColor(difference,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    _,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated=cv2.dilate(thresh,None,iterations=3)
    contour,hierarchy=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    for contours in contour:
        (x,y,w,h)=cv2.boundingRect(contours)
        if cv2.contourArea(contours)<900:
            continue
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(255,255,0),3)
        cv2.putText(frame1,'Status: {}'.format('Movement'),(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),4)
    # cv2.drawContours(frame1,contour,-1,(255,255,0),3)
    cv2.imshow('feed',frame1)
    frame1=frame2
    _,frame2=cap.read()
    if cv2.waitKey(40)==27:
        break;

cap.release()
cv2.destroyAllWindows()