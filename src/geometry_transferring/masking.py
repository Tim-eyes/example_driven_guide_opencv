import argparse
import numpy as np
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

mask = np.zeros(image.shape[:2], dtype = "uint8")
(x, y) = (image.shape[1] // 2, image.shape[0] // 2)
cv2.rectangle(mask, (x - 75, y - 75), (x + 75 , y + 75), 255,-1)
cv2.imshow("Mask", mask)

masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Mask Applied to Image", masked)

# mask = np.zeros(image.shape[:2], dtype = "uint8")
# cv2.circle(mask, (x, y), 100, 255, -1)
# masked = cv2.bitwise_and(image, image, mask = mask)
# cv2.imshow("Mask", mask)
# cv2.imshow("Mask Applied to Image", masked)

cv2.waitKey(0)