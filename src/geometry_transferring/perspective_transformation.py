import cv2
import numpy as np
from matplotlib import pyplot as plot


img=cv2.imread('must_logo.png')
rows,cols,ch=img.shape
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M=cv2.getPerspectiveTransform(pts1,pts2)
dst=cv2.warpPerspective(img,M,(300,300))
plot.subplot(121),plot.imshow(img),plot.title('Input')
plot.subplot(122),plot.imshow(dst),plot.title('Output')
plot.show()