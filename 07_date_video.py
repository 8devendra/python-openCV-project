import cv2
import datetime

cap=cv2.VideoCapture(0)
w=str(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h=str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(w)
print(h)
##you can set size of cam win
#set(cv2.CAP_PROP_FRAME_WEIDTH,202)

while(cap.isOpened()):
    ret, frame=cap.read()
    if ret == True:
        font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        dat=str(datetime.datetime.now())
        text=w + 'X' + h + '  ' + dat
        frame=cv2.putText(frame,text,(10,50),font,1,(0,255,255),1,cv2.LINE_AA)      #write text on frame
        cv2.imshow('frme',frame)
        if cv2.waitKey(1) & 0XFF==ord('q'):
            break
        elif cv2.waitKey(1) & 0XFF==ord('y'):
            cv2.imwrite('videoCapWtDate.png',frame)
            break
    else:
        break
    
cap.release()
cv2.destroyAllWindows()