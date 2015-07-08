from PIL import Image
from pylab import *
from lib import sift


temp_folder = '../temp/'

im_name1 = '../DATA/climbing_1_small.jpg'
im_name2 = '../DATA/climbing_2_small.jpg'

im1 = array(Image.open(im_name1))#.convert('L'))
im2 = array(Image.open(im_name2))#.convert('L'))

sift_name1 = temp_folder + im_name1.split('/')[-1][:-4] + '.sift'
sift_name2 = temp_folder + im_name2.split('/')[-1][:-4] + '.sift'

sift.process_image(im_name1, sift_name1)
l1, d1 = sift.read_features_from_file(sift_name1)

sift.process_image(im_name2, sift_name2)
l2, d2 = sift.read_features_from_file(sift_name2)

print('starting matching')
matches = sift.match(d1, d2)
matches_twosided = sift.match_twosided(d1, d2)

figure()
sift.plot_matches(im1, im2, l1, l2, matches)

figure()
# gray()
sift.plot_matches(im1, im2, l1, l2, matches_twosided)#[:100])

show()
