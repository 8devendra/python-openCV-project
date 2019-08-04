import cv2


cam=cv2.VideoCapture(0)                         #set cam module
print(cam.isOpened())
#while(cam.isOpened()):
while(cam.isOpened()):      #true
    ret,frame=cam.read()                        #read camera module
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #change colour to gray
    cv2.imshow('Frame',gray)                    #show cam module data to window(frame for color/gray for bw)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite('cam.png',frame)            #capture the image when exit
        break

cam.release()
cv2.destroyAllWindows()
