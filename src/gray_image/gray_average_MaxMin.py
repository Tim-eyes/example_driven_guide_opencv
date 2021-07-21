import cv2
import numpy as np

image=cv2.imread("must_logo.png")
row, col, channel = image.shape
image_gray = np.zeros((row, col))

# I(x,y) = 0.5 * max(I_R(x,y), I_G(x,y), I_B(x,y))+ 0.5 * min(I_R(x,y), I_G(x,y), I_B(x,y))

for r in range(row):
    for l in range(col):
        image_gray[r, l] = 1 / 2 * max(image[r, l, 0], image[r, l, 1], image[r, l, 2]) + 1 / 2 * min(image[r, l, 0],  image[r, l, 1], image[r, l, 2])

cv2.imshow("image_maxmin", image_gray.astype("uint8"))
cv2.waitKey(0)
