from PIL import Image
from pylab import *

figure()
gray()

im = array(Image.open('../DATA/empire.jpg').convert('L'))
print(int(im.min()), int(im.max()))
subplot(1, 4, 1)
imshow(im)
title('Original')

im2 = 255 - im # invert image
print(int(im2.min()), int(im2.max()))
subplot(1, 4, 2)
imshow(im2)
title('Invert')

im3 = (100.0 / 255) * im + 100 # clamp to interval 100...200
print(int(im3.min()), int(im3.max()))
subplot(1, 4, 3)
imshow(uint8(im3))
title('Clamp from 100 to 200')

im4 = 255.0 * (im / 255.0)**2 # squared
print(int(im4.min()), int(im4.max()))
# figure()
subplot(1, 4, 4)
imshow(uint8(im4))
title('Quadratic')

show()
