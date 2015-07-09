from PIL import Image
from pylab import *
from lib.imtools import get_imlist
import pickle


imlist = get_imlist('../DATA/a_thumbs')

im = array(Image.open(imlist[0])) # open one image to get size
m, n = im.shape[0:2] # get the size of the images

try:
  # open file and load
  with open('../temp/font_pca_modes.pkl', 'rb') as f:
    im_mean = pickle.load(f)
    V = pickle.load(f)

  # im_mean = loadtxt('../temp/font_pca_modes-im_mean.txt')
  # V = loadtxt('../temp/font_pca_modes-V.txt')

## Note: this part takes 20s to run on my laptop, made in year 2009
except:
  from lib import pca

  # im_number = len(imlist) # get the number of images

  # create matrix to store all flattened images
  im_matrix = array([array(Image.open(im)).flatten()
                for im in imlist], 'f')

  # perform PCA
  V, S, im_mean = pca.pca(im_matrix)

  ## Note: font_pca_modes.pkl takes up ~1.5 MB of space
  # open file and save
  with open('../temp/font_pca_modes.pkl', 'wb') as f:
    pickle.dump(im_mean, f)
    pickle.dump(V, f)

  ## Note: font_pca_modes-im_mean.txt takes up ~15 KB of space
  # savetxt('../temp/font_pca_modes-im_mean.txt', im_mean)
  ## Note: font_pca_modes-V.txt takes up ~9.5 MB of space
  # savetxt('../temp/font_pca_modes-V.txt', V)

# show some images (mean and 7 first modes)
figure()
gray()
subplot(2, 4, 1)
imshow(im_mean.reshape(m, n))
title('Original')
for i in range(7):
  subplot(2, 4, i+2)
  imshow(V[i].reshape(m, n))

show()
