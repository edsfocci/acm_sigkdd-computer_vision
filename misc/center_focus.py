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
from imread import imread
import mahotas as mh
import numpy as np

im = imread('../DATA/Lenna.png')

views = []
view_titles = []

views.append(im)
view_titles.append('Lenna, original')

r,g,b = im.transpose(2,0,1)

r12 = mh.gaussian_filter(r, 12)
g12 = mh.gaussian_filter(g, 12)
b12 = mh.gaussian_filter(b, 12)
im12 = mh.as_rgb(r12, g12, b12)

h,w = r.shape # height and width
Y,X = np.mgrid[:h,:w]

Y = Y - h/2. # center at h/2
Y = Y / Y.max() # normalize to -1 .. +1
X = X - w/2.
X = X / X.max()

C = np.exp(-2. * (X**2 + Y**2))
# Normalize again to 0..1
C = C - C.min()
C = C / C.ptp()
C = C[:,:,None] # This adds a dummy third dimension to C

ringed = mh.stretch(im*C + (1-C)*im12)

views.append(ringed)
view_titles.append('Lenna, center-focused')

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
