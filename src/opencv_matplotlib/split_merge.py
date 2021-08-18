import cv2
import numpy as np
from matplotlib import pyplot as plot

img=cv2.imread("must_logo.png")
r,b,g=cv2.split(img)
img2=cv2.merge([b,g,r])

plot.subplot(121);plot.imshow(img)
plot.subplot(122);plot.imshow(img2)
plot.show()

cv2.imshow('rbg',img)
cv2.imshow('bgr',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()