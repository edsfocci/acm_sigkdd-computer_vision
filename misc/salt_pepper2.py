from imread import imread
import numpy as np
import mahotas as mh
from matplotlib import pyplot as plt

lenna = imread('../DATA/Lenna.png', as_grey=True)

fig1 = plt.figure()

a = fig1.add_subplot(1, 2, 1)
plt.imshow(lenna)
plt.gray()
a.set_title('Lenna, grayscale')

salt = np.random.random(lenna.shape) > .975
pepper = np.random.random(lenna.shape) > .975

lenna = mh.stretch(lenna)
lenna = np.maximum(salt*170, lenna)
lenna = np.minimum(pepper*30 + lenna*(~pepper), lenna)

a = fig1.add_subplot(1, 2, 2)
plt.imshow(lenna)
a.set_title('Lenna, salt & pepper')

plt.show()
