import cv2
import numpy as np

cap=cv2.VideoCapture(0)
    
while(1):

    # 
    ret,frame=cap.read()
    # HSV
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    # color threshold 
    # >>> green=np.uint8([[[0,255,0]]])   !!!                
    # >>> hsv_green=cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
    # scn (the number of channels of the source)
    # 
    # three '[' -> cvArray，cvMat，IplImage
    
    # blue threshold
    lower_blue=np.array([110,50,50])
    upper_blue=np.array([130,255,255])
    # mask module
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    # and_operator
    res=cv2.bitwise_and(frame,frame,mask=mask)
    # 
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k=cv2.waitKey(5)&0xFF
    if k==27:
        break

cv2.destroyAllWindows()