import numpy as np
import cv2

### IMPORTANT!
# Remember to press any key when the images are active to exit
# Otherwise it will hang in your terminal and will need to restart it


image = cv2.imread('../DATA/GaussianNoise.jpg')
# image = cv2.imread('../DATA/Lenna_salt_pepper.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

averaging = np.hstack([
  cv2.blur(image, (3,3)),
  cv2.blur(image, (5,5)),
  cv2.blur(image, (7,7))
])

cv2.imshow("Averaged", averaging)

gaussian = np.hstack([
  cv2.GaussianBlur(image, (3,3), 0),
  cv2.GaussianBlur(image, (5,5), 0),
  cv2.GaussianBlur(image, (7,7), 0)
])

cv2.imshow("Gaussian", gaussian)

median = np.hstack([
  cv2.medianBlur(image, 3),
  cv2.medianBlur(image, 5),
  cv2.medianBlur(image, 7)
])

cv2.imshow("Median", median)

bilateral = np.hstack([
  cv2.bilateralFilter(image, 5, 21, 21),
  cv2.bilateralFilter(image, 7, 31, 31),
  cv2.bilateralFilter(image, 9, 41, 41)
])

cv2.imshow("Bilateral", bilateral)

cv2.waitKey(0)
