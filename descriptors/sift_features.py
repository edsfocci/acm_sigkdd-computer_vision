from PIL import Image
from pylab import *
from lib import sift


im_name = '../DATA/empire.jpg'
im1 = array(Image.open(im_name).convert('L'))
sift.process_image(im_name, '../temp/empire.sift')
l1, d1 = sift.read_features_from_file('../temp/empire.sift')

figure()
gray()
sift.plot_features(im1, l1, circle=True)
show()
