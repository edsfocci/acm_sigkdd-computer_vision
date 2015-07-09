from PIL import Image
from pylab import *
from lib import rof


im = array(Image.open('../DATA/empire.jpg').convert('L'))
im_list = [im]
U, T = rof.denoise(im, im)
im_list.append(U)

labels = ['Original', 'ROF']

from scipy.ndimage.filters import gaussian_filter

standard_deviations = [2, 3]
for sigma in standard_deviations:
  im_list.append(gaussian_filter(im, sigma))
  labels.append('sigma = ' + str(sigma))

figure()
gray()
imshow(U)
axis('equal')
axis('off')

for i in range(len(im_list)):
  subplot(1, len(im_list), i+1)
  imshow(im_list[i])
  title(labels[i])

show()
