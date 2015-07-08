import mahotas as mh
from imread import imread
import numpy as np


image = imread('../DATA/simple-dataset/building05.jpg')
image = mh.colors.rgb2gray(image, dtype=np.uint8)

thresh = mh.thresholding.otsu(image)

#otsubin = (image <= thresh)
#otsubin = mh.close(otsubin, np.ones((15,15)))

otsubin = (image > thresh)
otsubin = mh.open(otsubin, np.ones((15,15)))

from matplotlib import pyplot as plt

plt.imshow(otsubin)
plt.gray()
plt.show()
