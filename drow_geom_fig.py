import cv2

cam=cv2.VideoCapture(0)
print(cam.isOpened());
while(cam.isOpened()):
    ret,frame=cam.read()
    frame=cv2.line(frame,(0,0),(255,255),(0,0,255),5)
    cv2.imshow('Line On image',frame)    
    #cv2.imshow('Live',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):    
        #cv2.destroyWindow('Live')
        #img=cv2.imread(frame,1)
        #
        #cv2.imshow('Line On image',frame)
        #cv2.waitKey(0)
        cv2.imwrite('LineImg.png',frame)
        break
cam.release()
cv2.destroyAllWindows()