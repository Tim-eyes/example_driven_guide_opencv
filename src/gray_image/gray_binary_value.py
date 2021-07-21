import cv2
import numpy as np

image = cv2.imread("must_logo.png")
row, col, channel = image.shape
image_gray = np.zeros((row, col))

for r in range(row):
    for l in range(col):
        image_gray[r, l] = 1 / 2 * max(image[r, l, 0], image[r, l, 1], image[r, l, 2]) + 1 / 2 * min(image[r, l, 0],  image[r, l, 1], image[r, l, 2])

image_binary = np.zeros_like(image_gray)

threshold = 100
for r in range(row):
    for l in range(col):
        if image_gray[r, l] >= threshold:
            image_binary[r, l] = 255
        else:
            image_binary[r, l] = 0

cv2.imshow("image_binary", image_binary.astype("uint8"))
cv2.waitKey(0)