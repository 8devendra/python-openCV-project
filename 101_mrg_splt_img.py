import cv2
import numpy as np

img=cv2.imread('LineImg.png')
print(img.shape)
print(img.size)
print(img.dtype)

b,g,r=cv2.split(img)
print(img)
//print(b+' '+g+' '+r)
img=cv2.merge((b,g,r))
cv2.imshow('ColourImage', img)

cv2.waitKey(0)
cv2.destroyAllWindows()