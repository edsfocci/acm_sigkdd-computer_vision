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
import numpy as np
import mahotas as mh

lenna = imread('../DATA/Lenna.png', as_grey=True)

views = []
view_titles = []

views.append(lenna)
view_titles.append('Lenna, grayscale')

salt = np.random.random(lenna.shape) > .975
pepper = np.random.random(lenna.shape) > .975

lenna = mh.stretch(lenna)
lenna = np.maximum(salt*170, lenna)
lenna = np.minimum(pepper*30 + lenna*(~pepper), lenna)

views.append(lenna)
view_titles.append('Lenna, salt & pepper')

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
