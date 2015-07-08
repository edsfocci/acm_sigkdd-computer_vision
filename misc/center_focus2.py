from imread import imread
import mahotas as mh
import numpy as np
from matplotlib import pyplot as plt

im = imread('../DATA/Lenna.png')

fig1 = plt.figure()

a = fig1.add_subplot(1, 2, 1)
plt.imshow(im)
a.set_title('Lenna, original')

r,g,b = im.transpose(2,0,1)

r12 = mh.gaussian_filter(r, 12)
g12 = mh.gaussian_filter(g, 12)
b12 = mh.gaussian_filter(b, 12)
im12 = mh.as_rgb(r12, g12, b12)

h,w = r.shape # height and width
Y,X = np.mgrid[:h,:w]

Y = Y - h/2. # center at h/2
Y = Y / Y.max() # normalize to -1 .. +1
X = X - w/2.
X = X / X.max()

C = np.exp(-2. * (X**2 + Y**2))
# Normalize again to 0..1
C = C - C.min()
C = C / C.ptp()
C = C[:,:,None] # This adds a dummy third dimension to C

ringed = mh.stretch(im*C + (1-C)*im12)

a = fig1.add_subplot(1, 2, 2)
plt.imshow(ringed)
a.set_title('Lenna, center-focused')

plt.show()
