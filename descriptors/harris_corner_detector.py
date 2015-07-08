from PIL import Image
from numpy import array
from lib import harris


im = array(Image.open('../DATA/empire.jpg').convert('L'))
harris_im = harris.compute_harris_response(im)
filtered_coords = harris.get_harris_points(harris_im, 6)
harris.plot_harris_points(im, filtered_coords)
