from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler

import sys
if sys.version_info[0] < 3:
  import Tkinter as Tk
else:
  import tkinter as Tk

root = Tk.Tk()

#\/#\/#
from matplotlib.figure import Figure
import matplotlib.cm as cm
import mahotas as mh
from imread import imread
import numpy as np

image = imread('../DATA/simple-dataset/building05.jpg')
image_uint8 = mh.colors.rgb2gray(image, dtype=np.uint8)
image_float = mh.colors.rgb2gray(image)
#print(image_uint8)
#print(image_float)

thresh = mh.thresholding.otsu(image)

otsubin = (image_uint8 > thresh)
otsubin = mh.open(otsubin, np.ones((15,15)))

views = []
view_titles = []

views.append(otsubin)
view_titles.append('Otsu w/ open')

for sigma in (8, 16, 32):
  im = mh.gaussian_filter(image_uint8, sigma)
#  print(im)
  views.append(im > thresh)
  view_titles.append('Sigma = ' + str(sigma))

# Initial view
index = 0
f = Figure()
a = f.add_subplot(111)

a.imshow(views[index], cmap = cm.Greys_r)
a.set_title(view_titles[index])
#/\#/\#

# a tk.DrawingArea
canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)


# Use 'left' or 'right' arrow keys to change the view
def on_key_event(event):
  global index

  if event.key == 'right':
    index = (index + 1) % len(views)
    a.imshow(views[index], cmap = cm.Greys_r)
    a.set_title(view_titles[index])
    f.canvas.draw()

  elif event.key == 'left':
    index = (index - 1) % len(views)
    a.imshow(views[index], cmap = cm.Greys_r)
    a.set_title(view_titles[index])
    f.canvas.draw()

canvas.mpl_connect('key_press_event', on_key_event)

Tk.mainloop()
