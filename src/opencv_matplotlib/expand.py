import cv2
import numpy as np
from matplotlib import pyplot as plot

BLUE=[255,0,0]
img=cv2.imread('must_logo.png')

replicate = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)

plot.subplot(231),plot.imshow(img,'gray'),plot.title('ORIGINAL')
plot.subplot(232),plot.imshow(replicate,'gray'),plot.title('REPLICATE')
plot.subplot(233),plot.imshow(reflect,'gray'),plot.title('REFLECT')
plot.subplot(234),plot.imshow(reflect101,'gray'),plot.title('REFLECT_101')
plot.subplot(235),plot.imshow(wrap,'gray'),plot.title('WRAP')
plot.subplot(236),plot.imshow(constant,'gray'),plot.title('CONSTANT')

plot.show()