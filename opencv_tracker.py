#trackbar in opencv means we can change color like brightness of the picture or convert img to gary scale by using switch
import cv2
import numpy as np
def nothing(x):
    print(x)
# img=np.zeros([512,512,3],np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('CP','image',10,400,nothing)
# cv2.createTrackbar('G','image',0,255,nothing)
# cv2.createTrackbar('R','image',0,255,nothing)

switch='color/gray'
cv2.createTrackbar(switch,'image',0,1,nothing)

while(1):
    img = cv2.imread('test_rp17.jpg', 1)
    pos=cv2.getTrackbarPos('CP','image')
    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,str(pos),(50,150),font,4,(0,0,255),3)
    k=cv2.waitKey(1) & 0xFF
    if k==27:
        break;
    # b=cv2.getTrackbarPos('B','image')
    # g=cv2.getTrackbarPos('G','image')
    # r=cv2.getTrackbarPos('R','image')
    s=cv2.getTrackbarPos(switch,'image')

    if s==0:
        pass
    else:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img=cv2.imshow('image',img)
cv2.destroyAllWindows()