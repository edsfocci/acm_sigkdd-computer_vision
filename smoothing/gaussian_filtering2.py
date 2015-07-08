import mahotas as mh
from imread import imread
from matplotlib import pyplot as plt

image = imread('../DATA/simple-dataset/building05.jpg')
image = mh.colors.rgb2gray(image)

standard_deviations = [8, 16, 32]

fig1 = plt.figure()

for i in range(3):
  im = mh.gaussian_filter(image, standard_deviations[i])

  a = fig1.add_subplot(1, 3, i+1)  # this line outputs images side-by-side
  plt.imshow(im)
  plt.gray()
  a.set_title('Sigma = ' + str(standard_deviations[i]))

plt.show()
