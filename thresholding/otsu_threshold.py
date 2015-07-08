import mahotas as mh
from imread import imread
import numpy as np


image = imread('../DATA/simple-dataset/building05.jpg')
image = mh.colors.rgb2gray(image, dtype=np.uint8)

thresh = mh.thresholding.otsu(image)
print(thresh)

from matplotlib import pyplot as plt

plt.imshow(image > thresh)
plt.gray()
plt.show()
