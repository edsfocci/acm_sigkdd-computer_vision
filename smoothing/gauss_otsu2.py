import mahotas as mh
from imread import imread
import numpy as np
from matplotlib import pyplot as plt

image = imread('../DATA/simple-dataset/building05.jpg')
image = mh.colors.rgb2gray(image, dtype=np.uint8)

thresh = mh.thresholding.otsu(image)

otsubin = (image > thresh)
otsubin = mh.open(otsubin, np.ones((15,15)))

standard_deviations = [8, 16, 32]

fig1 = plt.figure()

a = fig1.add_subplot(1, 4, 1)
plt.imshow(otsubin)
plt.gray()
a.set_title('Otsu w/ open')

for i in range(3):
  im = mh.gaussian_filter(image, standard_deviations[i])

  a = fig1.add_subplot(1, 4, i+2)  # this line outputs images side-by-side
  plt.imshow(im > thresh)
  plt.gray()
  a.set_title('Sigma = ' + str(standard_deviations[i]))

plt.show()
