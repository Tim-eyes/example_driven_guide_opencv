import cv2
import numpy as np

image = cv2.imread("must_logo.png", 0)

row, col = image.shape

image_inverse = np.zeros_like(image)

for r in range(row):
    for l in range(col):
        image_inverse[r, l] = 255 - image[r, l]

cv2.imshow("image", image)
cv2.imshow("image_inverse", image_inverse)
cv2.waitKey()