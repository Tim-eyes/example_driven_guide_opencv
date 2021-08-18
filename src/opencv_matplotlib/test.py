import numpy as np
import cv2
from matplotlib import pyplot as plot

img=cv2.imread("must_logo.png")
plot.imshow(img,cmap="gray",interpolation="bicubic")
plot.xticks([]),plot.yticks([])
plot.show()