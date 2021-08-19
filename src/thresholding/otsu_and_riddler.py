from matplotlib import pyplot as plot
import argparse
import cv2
import numpy as np
import mahotas as mh

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

blurred = cv2.GaussianBlur(image, (5, 5), 0)

T = mh.otsu(blurred)
print("Otsu’s threshold: {}".format(T))

thresh = image.copy()
thresh[thresh > T]=255
thresh[thresh<255]=0
thresh=cv2.bitwise_not(thresh)
cv2.imshow("Otsu",thresh)

T = mh.rc(blurred)
print("Riddle-Calvard: {}".format(T))
thresh = image.copy()
thresh[thresh > T]=255
thresh[thresh<255]=0
thresh=cv2.bitwise_not(thresh)
cv2.imshow("Riddler-Calavard",thresh)
cv2.waitKey(0)