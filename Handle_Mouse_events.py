import cv2
import numpy as np

# event=[i for i in dir(cv2) if 'EVENT' in i] #for getting mouse events
# print(event)

# to know the co ordinates of the image by using mouse left and right click

# def click_event(event,x,y):
#     if event==cv2.EVENT_LBUTTONDOWN:
#         print(x,' , ',y)
#         text=cv2.FONT_HERSHEY_SIMPLEX
#         strxy=str(x)+' , '+ str(y)
#         cv2.putText(img,strxy,(x,y),text,1,(255,255,0),4)
#         cv2.imshow('image',img)
#     if event==cv2.EVENT_RBUTTONDOWN:
#         blue=img[y,x,0]
#         green=img[y,x,1]
#         red=img[y,x,2]
#         text = cv2.FONT_HERSHEY_SIMPLEX
#         strxy = str(blue) + ' , ' + str(green) + ' , '+str(red)
#         cv2.putText(img, strxy, (x, y), text, 1, (0, 255, 255), 4)
#         cv2.imshow('image', img)

# to connect the points with the line using mouse events

# def click_event(event,x,y,flags,param):
#     if event==cv2.EVENT_LBUTTONDOWN:
#         cv2.circle(img,(x,y),5,(255,0,255),-1)
#         points.append((x,y))
#         if len(points)>=2:
#             cv2.line(img,points[-1],points[-2],(0,0,255),10)
#         cv2.imshow('image',img)

#Zoom the color of the image in another window

def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        blue = img[x,y, 0]
        green=img[x,y,1]
        red=img[x,y,2]
        cv2.circle(img,(x,y),5,(0,0,255),-1)
        mycolorimage=np.zeros([512,512,3],np.uint8)
        mycolorimage[:] = [blue,green,red]

        cv2.imshow('image',mycolorimage)

# img=np.zeros([512,512,3],np.uint8)
img=cv2.imread('test_rp17.jpg',1)
cv2.imshow('image',img)
points=[]
cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
