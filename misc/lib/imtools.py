from PIL import Image
from numpy import *


def get_imlist(path):
  """  Returns a list of filenames for
    all jpg images in a directory. """
  import os

  return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]
  
def imresize(image, size):
  """  Resize an image array using PIL. """
  pil_im = Image.fromarray(uint8(image))

  return array(pil_im.resize(size))

def histeq(image, number_bins=256):
  """  Histogram equalization of a grayscale image. """

  # get image histogram
  image_hist, bins = histogram(image.flatten(), number_bins, normed=True)
  cdf = image_hist.cumsum() # cumulative distribution function
  cdf = 255 * cdf / cdf[-1] # normalize

  # use linear interpolation of cdf to find new pixel values
  image2 = interp(image.flatten(), bins[:-1], cdf)

  return image2.reshape(image.shape), cdf

def compute_average(imlist):
  """  Compute the average of a list of images. """

  # open first image and make into array of type float
  averageim = array(Image.open(imlist[0]), 'f')

  for imname in imlist[1:]:
    try:
      averageim += array(Image.open(imname))
    except:
      print(imname + '...skipped')
  averageim /= len(imlist)

  # return average as uint8
  return array(averageim, 'uint8')
