from PIL import Image
from pylab import *
from lib import imtools

figure()
gray()

im = array(Image.open('../DATA/AquaTermi_lowcontrast.JPG').convert('L'))
subplot(2, 2, 1)
hist(im.flatten(), 128)
subplot(2, 2, 3)
imshow(im)
title('Original')

im2, cdf = imtools.histeq(im)
subplot(2, 2, 2)
hist(im2.flatten(), 128)
subplot(2, 2, 4)
imshow(uint8(im2))
title('Histogram Equalization')

show()
