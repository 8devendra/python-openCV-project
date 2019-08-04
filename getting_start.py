import cv2

img=cv2.imread("bridge.png",-1)
cv2.imshow('Bridge',img)
k=cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k== ord('y'):
    cv2.imwrite('bridge_copy.png',img)
    cv2.destroyAllWindows()
     
    
