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

image = imread('../DATA/simple-dataset/building05.jpg')
image = mh.colors.rgb2gray(image)

gauss_filtered = []
standard_deviations = [8, 16, 32]
for sigma in standard_deviations:
  im = mh.gaussian_filter(image, sigma)
  gauss_filtered.append(im)

# Initial view
index = 0
f = Figure()
a = f.add_subplot(111)

a.imshow(gauss_filtered[index], cmap = cm.Greys_r)
a.set_title('Sigma = ' + str(2 ** (index + 3)))
#/\#/\#

# a tk.DrawingArea
canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)


# Use 'left' or 'right' arrow keys to change the view
def on_key_event(event):
  global index

  if event.key == 'right':
    index = (index + 1) % len(gauss_filtered)
    a.imshow(gauss_filtered[index], cmap = cm.Greys_r)
    a.set_title('Sigma = ' + str(standard_deviations[index]))
    f.canvas.draw()

  elif event.key == 'left':
    index = (index - 1) % len(gauss_filtered)
    a.imshow(gauss_filtered[index], cmap = cm.Greys_r)
    a.set_title('Sigma = ' + str(standard_deviations[index]))
    f.canvas.draw()

canvas.mpl_connect('key_press_event', on_key_event)

Tk.mainloop()
