import cv2
import numpy as np
import os

img=cv2.imread('must_logo.png')

#res=cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_CUBIC)


height,width=img.shape[:2]
res=cv2.resize(img,(int(0.5*width),int(0.5*height)),interpolation=cv2.INTER_CUBIC)

cv2.imshow('res',res)
cv2.imshow('img',img)

cv2.waitKey(0)        
cv2.destroyAllWindows()