from PIL import Image
from pylab import *
from lib import sift


temp_folder = '../temp/'

im_name1 = '../DATA/crans_1_small.jpg'
im_name2 = '../DATA/crans_2_small.jpg'

# im_name1 = '../DATA/sf_view1.jpg'
# im_name2 = '../DATA/sf_view2.jpg'

im1 = array(Image.open(im_name1))#.convert('L'))
im2 = array(Image.open(im_name2))#.convert('L'))

sift_name1 = temp_folder + im_name1.split('/')[-1][:-4] + '.sift'
sift_name2 = temp_folder + im_name2.split('/')[-1][:-4] + '.sift'

sift.process_image(im_name1, sift_name1)
l1, d1 = sift.read_features_from_file(sift_name1)

sift.process_image(im_name2, sift_name2)
l2, d2 = sift.read_features_from_file(sift_name2)

print('starting matching')
matches = sift.match_twosided(d1, d2)

figure()
# gray()
sift.plot_matches(im1, im2, l1, l2, matches)#[:100])
show()
