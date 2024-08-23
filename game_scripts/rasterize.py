import skimage as ski
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image
from matplotlib.patches import Circle
from random import randint

im = image.imread("ghost_face.jpg")
im = im[30:330,104:404]
# instead of doing this thresholding,
# i should have the probability of a 
# white dot be equal to the brightness 
# of the image
im = (im > np.max(im)/2).astype(int)
plt.imshow(im)
plt.show()

fig, ax = plt.subplots()
for i in range(300):
    circle_x = randint(0, 299)
    circle_y = randint(0, 299)
    if im[circle_x, circle_y] > np.max(im)/2:
        print('here') 
    circle = Circle((randint(0,300), randint(0,300)), 1)
    ax.add_patch(circle)




