'''
@author: WANG Zhao, Matthew
all copyright remained

the functions included in L2 spatial domain
    |--- negative
    |--- power law
    |--- histogram equalization

    |--- average filter
    |--- max filter
    |--- min filter
    |--- median filter
    |--- laplacian filter
    |--- Sobel filter
'''

from PIL import Image
import copy
import numpy as np
import math
from imagematt import others


def negative(img):
    img2 = copy.deepcopy(img)
    for i in range(0, np.shape(img)[0] - 1):
        for j in range(0, np.shape(img)[1] - 1):
            img2[i][j] = 255 - img[i][j]
    others.showimg(img, img2, 'negative')


def lg(img):
    img2 = copy.deepcopy(img)
    c = 255 / math.log(1 + np.amax(img))
    for i in range(0, np.shape(img)[0] - 1):
        for j in range(0, np.shape(img)[1] - 1):
            img2[i][j] = c * math.log(float(1 + img[i][j]), 10)
    others.showimg(img, img2, 'log')


def powerlaw(img, gamma = 0.5):
    img_float = np.float32(img)
    max_pixel = np.max(img_float)
    img_normalised = img_float/max_pixel
    gamma_corr = np.log(img_normalised)*gamma
    gamma_corrected = np.exp(gamma_corr)*255.0
    img2 = np.uint8(gamma_corrected)
    others.showimg(img, img2, 'Power-law with gamma ' + str(gamma))

