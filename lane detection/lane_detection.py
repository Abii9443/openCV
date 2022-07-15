import cv2
import numpy as np
import matplotlib.pyplot as plt
def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    # channel_count = img.shape[2]
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image
def draw_lines(img,lines):
    for line in lines:
        (x1,y1,x2,y2)=line[0]
        cv2.line(img,(x1,y1),(x2,y2),(255,0,255),6)
    return img
# img=cv2.imread('../test_road.jpg')
# img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
def process(img):
    print(img.shape)
    height=img.shape[0]
    width=img.shape[1]
    ROI=[(0,height),(width/2,height/2),(width,height)]


    gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edge=cv2.Canny(gray_image,70,200)
    crop_image=region_of_interest(edge,np.array([ROI],np.int32))
    lines=cv2.HoughLinesP(crop_image,6,np.pi/60,160,np.array([]),minLineLength=40,maxLineGap=25)
    f_image=draw_lines(img,lines)
    return  f_image
cap=cv2.VideoCapture('../test1.mp4')

while (cap.isOpened()):
    _,frame=cap.read()
    frame=process(frame)
    cv2.imshow('test_road',frame)
    if cv2.waitKey(1) &0xFF ==ord('q'):
        break
