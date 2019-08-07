import cv2
import numpy as np

def click_event(event,x,y,flags,param):
    if event== cv2.EVENT_LBUTTONDOWN:
        #points.append((x,y))
        points.append(x)
        points.append(y)
        font=cv2.FONT_HERSHEY_COMPLEX_SMALL #disp
        strXY=str(x)+','+str(y)             #disp
        cv2.putText(img,strXY,(x,y),font,1,(255,255,0),1)   #disp
        cv2.imshow('Image',img)     #disp
        if len(points) >=4:
            print('Move Image')
            #mov=img[points[-1],points[-2]]
            if len(points) >= 6:
                #img[points[-3],points[-4]]=mov
                print(points)
                print(points[-6])
                print(points[-5])
                print(points[-4])
                print(points[-3])
                print(points[-2])
                print(points[-1])
                

                #mov=img[points[-6]:points[-5],points[-4]:points[-3]]
                #mov = img[116 : 102 , 323 : 219]
                
                mov = img[100 : 100 , 200 : 200]
                #addX=points[-4]-points[-6]
                #addY=points[-3]-points[-5]

                #opOnNew Point
                #newX=addX+points[-2]
                #newY=addY+points[-1]

                #print('find diff : '+str(newX)+' '+str(newY))
                #img[points[-2]:points[-1],newX:newY]=mov
                #img[117 : 217 , 324 : 334] = mov
                img[300 : 300 , 400 : 400] = mov
                points.clear()
                cv2.imshow('Image',img)
                #npX=addX+points[-5]
                #npY=addY+points[-6]
                #print('add diff: '+str(npX)+' '+str(npY))
                
                #print(points)
                #print('new p6: '+str(npX)+'  '+str(npY))                
                


img=cv2.imread('LineImg.png',0)
cv2.imshow('Image',img)
#cv2.imshow('LineImg.png',img)
points=[]
cv2.setMouseCallback('Image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()





