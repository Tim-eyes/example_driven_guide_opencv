import argparse
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_gray_inv = 255-image_gray
image_blur = cv2.GaussianBlur(image_gray_inv, (21, 21), 0)
image_blend1 = cv2.divide(image_gray, 255-image_blur, scale=256)
image_blend2 = 255-cv2.divide(255-image_gray, 255-image_blur, scale=256)

# cv2.imshow("Original", image)
# cv2.imshow("Gray", image_gray)
cv2.imshow("Inv", image_gray_inv)
cv2.imshow("Blur", image_blur)
cv2.imshow("Blend1", image_blend1)
cv2.imshow("Blend2", image_blend2)

cv2.waitKey(0)
cv2.destroyAllWindows()
