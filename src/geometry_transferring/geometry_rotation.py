import cv2
import numpy as np


img=cv2.imread('must_logo.png')
rows,cols=img.shape[:2]

# first parameter -- point , second parameter -- angle, third parameter --scale factor
M=cv2.getRotationMatrix2D((cols/2,rows/2),45,0.6)
# third paramete -- size
dst=cv2.warpAffine(img,M,(2*cols,2*rows))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()