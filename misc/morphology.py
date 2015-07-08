from scipy.ndimage import measurements, morphology
import mahotas as mh
from PIL import Image
from pylab import *


# load image and threshold to make sure it is binary
im = array(Image.open('../DATA/ceramic-houses_t0.png').convert('L'))
im_list = [im]

thresh = mh.thresholding.otsu(im)
# thresh = mh.thresholding.rc(im)
print(thresh)
im = 1 * (im > thresh)
im_list.append(im)

labels, number_objects = measurements.label(im)
print('Number of objects:', number_objects)
im_list.append(labels)

# morphology - closing to count objects better
im_close = morphology.binary_closing(im, ones((9,5)), iterations=1)
im_list.append(im_close)

labels_close, number_objects_close = measurements.label(im_close)
print('Number of objects:', number_objects_close)
im_list.append(labels_close)

labels = ['Original', 'Original threshold',
  'Number of Objects: ' + str(number_objects),
  'Original after closing', 'Number of Objects: ' + str(number_objects_close)]

figure()
gray()
for i in range(len(im_list)):
  if i < 3:
    subplot(2, 3, i+1)
  else:
    subplot(2, 3, i+2)

  if i == 0:
    imshow(im_list[i])
  else:
    imshow(-im_list[i])
  title(labels[i])

show()
