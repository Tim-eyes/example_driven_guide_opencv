import argparse
from PIL import Image
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path to the image")
args = vars(ap.parse_args())

arr = np.asarray(Image.open(args["image"]).convert('L')).astype('float')
depth = 10.
grad = np.gradient(arr)
grad_x, grad_y = grad
grad_x = grad_x * depth / 100.
grad_y = grad_y * depth / 100.
unit = np.sqrt(grad_x ** 2 + grad_y ** 2 + 1.)
unit_x = grad_x / unit
unit_y = grad_y / unit
unit_z = 1. / unit

vertical_angle = np.pi / 2.
azimuth_angle = np.pi / 4.

dx = np.cos(vertical_angle) * np.cos(azimuth_angle)
dy = np.sin(azimuth_angle) * np.cos(vertical_angle)
dz = np.sin(vertical_angle)

normal = 255 * (dx * unit_x + dy * unit_y + dz * unit_z)
normal = normal.clip(0, 255)

image = Image.fromarray(normal.astype("uint8"))
image.show()
print("OK")
