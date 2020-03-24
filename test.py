from imagematt import spatial_domain
from imagematt import others
import numpy as np
import matplotlib.pyplot as plt # using for displaying the image
import matplotlib.image as mpimg # using for reading the image

img = mpimg.imread('sample.jpeg')
img = others.togray(img)

spatial_domain.negative(img)
spatial_domain.lg(img)
spatial_domain.powerlaw(img)

