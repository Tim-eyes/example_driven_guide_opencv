from matplotlib import pyplot as plot
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)


hist = cv2.calcHist([image], [0], None, [256], [0, 256])

plot.figure()
plot.title("Grayscale Histogram")
plot.xlabel("Bins")
plot.ylabel("# of Pixels")
plot.plot(hist)
plot.xlim([0, 256])
plot.show()
cv2.waitKey(0)
