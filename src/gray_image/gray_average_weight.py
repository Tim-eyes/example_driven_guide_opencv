import cv2
import numpy as np

image=cv2.imread("must_logo.png")
row, col, channel = image.shape
image_gray = np.zeros((row, col))



for r in range(row):
    for l in range(col):
        image_gray[r, l] = 0.11 * image[r, l, 0]+ 0.59* image[r, l, 1] + 0.3*image[r, l, 2]


cv2.imshow("image_weight", image_gray.astype("uint8"))
cv2.waitKey(0)