from PIL import Image
from numpy import *
from scipy.ndimage import filters
from lib import rof
from scipy.misc import imsave

# Reminder: output files stored in '../temp/' folder, format: PDF


# create synthetic image with noise
im = zeros((500,500))
im[100:400, 100:400] = 128
im[200:300, 200:300] = 255
im = im + 30*random.standard_normal((500,500))

imsave('../temp/synth_noisy.pdf', im)

U, T = rof.denoise(im, im)
G = filters.gaussian_filter(im, 3)

# save the result
imsave('../temp/synth_rof.pdf', U)
imsave('../temp/synth_gaussian.pdf', G)
