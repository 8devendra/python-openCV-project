import cv2


img1=cv2.imread('cam.png')
img2=cv2.imread('bridge.png')

img1=cv2.resize(img1, (512,512))
img2=cv2.resize(img2, (512,512))

dest=cv2.add(img1,img2)
cv2.imshow('Marge Image',dest)
cv2.waitKey(0)
cv2.destroyAllWindows()

