#to show date and time in default camera
# Draw line or rectangle  in camera video

import cv2
import datetime
cap=cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3,1200)
cap.set(4,1200)

while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        # gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        font = cv2.FONT_HERSHEY_SIMPLEX
        text= 'Width: '+str(cap.get(3)) + 'Height:'+str(cap.get(4))
        datet=str(datetime.datetime.now())
        frame= cv2.rectangle(frame,(310,255),(510,130),(255,255,255),10)
        frame=cv2.putText(frame,datet,(10,50),font,2,(0,255,255),5,cv2.LINE_AA )
        cv2.imshow('frame',frame)



        if cv2.waitKey(1) & 0xFF == ord('q'):
            break;
    else:
        break;

cap.release()
cv2.destroyAllWindows()