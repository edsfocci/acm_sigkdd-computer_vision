import numpy as np
import cv2

### IMPORTANT!
# Remember you need press any key when any of the images windows are active
# to exit the program loop in cv2.imshow
# Otherwise it will hang in your terminal and will need to restart it


# Peppers image with heavy Gaussian noise
image = cv2.imread('../DATA/GaussianNoise.jpg')

# Lena image with salt & pepper noise
# image = cv2.imread('../DATA/Lenna_salt_pepper.png')

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Using averaging filter of various window sizes
averaging = np.hstack([
  cv2.blur(image, (3,3)),
  cv2.blur(image, (5,5)),
  cv2.blur(image, (7,7))
])
cv2.imshow("Averaged", averaging)

# Using Gaussian filter of various window sizes
gaussian = np.hstack([
  cv2.GaussianBlur(image, (3,3), 0),
  cv2.GaussianBlur(image, (5,5), 0),
  cv2.GaussianBlur(image, (7,7), 0)
])
cv2.imshow("Gaussian", gaussian)

# Using median filter of various window sizes
median = np.hstack([
  cv2.medianBlur(image, 3),
  cv2.medianBlur(image, 5),
  cv2.medianBlur(image, 7)
])
cv2.imshow("Median", median)

# Using bilateral filter of various window sizes
bilateral = np.hstack([
  cv2.bilateralFilter(image, 5, 21, 21),
  cv2.bilateralFilter(image, 7, 31, 31),
  cv2.bilateralFilter(image, 9, 41, 41)
])
cv2.imshow("Bilateral", bilateral)

# Part of code that waits for keypress (any key) to exit the program
cv2.waitKey(0)
