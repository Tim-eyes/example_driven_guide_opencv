import cv2
import numpy as np

img = cv2.imread("must_logo.png")
block=img[280:340,330:390]
img[273:333,100:160]=block 
cv2.imshow('img',img)
# cv2.imshow('block',block)
cv2.waitKey(0)

