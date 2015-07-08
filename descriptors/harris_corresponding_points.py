from PIL import Image
from pylab import *
import pickle
from lib import harris


temp_folder = '../temp/'

im_name_short = 'crans'
im1 = array(Image.open('../DATA/crans_1_small.jpg').convert('L'))
im2 = array(Image.open('../DATA/crans_2_small.jpg').convert('L'))

# im_name_short = 'sf_view'
# im1 = array(Image.open('../DATA/sf_view1.jpg').convert('L'))
# im2 = array(Image.open('../DATA/sf_view2.jpg').convert('L'))

try:
  with open(temp_folder + im_name_short + '_harris.pkl', 'rb') as f:
    filtered_coords1 = pickle.load(f)
    filtered_coords2 = pickle.load(f)
    matches = pickle.load(f)
  print('Using saved data')

except:
  wid = 5
  harris_im = harris.compute_harris_response(im1, 5)
  filtered_coords1 = harris.get_harris_points(harris_im, wid+1)
  d1 = harris.get_descriptors(im1, filtered_coords1, wid)

  harris_im = harris.compute_harris_response(im2, 5)
  filtered_coords2 = harris.get_harris_points(harris_im, wid+1)
  d2 = harris.get_descriptors(im2, filtered_coords2, wid)

  print('starting matching')
  matches = harris.match_twosided(d1, d2)

  with open(temp_folder + im_name_short + '_harris.pkl', 'wb') as f:
    pickle.dump(filtered_coords1, f)
    pickle.dump(filtered_coords2, f)
    pickle.dump(matches, f)

figure()
gray()
harris.plot_matches(im1, im2, filtered_coords1, filtered_coords2, matches)#[:100])
show()
