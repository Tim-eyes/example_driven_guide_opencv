import cv2
import numpy as np
from matplotlib import pyplot as plot


img=cv2.imread('must_logo.png')
rows,cols,ch=img.shape
pts1=np.float32([[50,50],[200,50],[50,200]])
pts2=np.float32([[10,100],[200,50],[100,250]])
M=cv2.getAffineTransform(pts1,pts2)
dst=cv2.warpAffine(img,M,(300,300))
plot.subplot(121),plot.imshow(img),plot.title('Input')
plot.subplot(122),plot.imshow(dst),plot.title('Output')
plot.show()