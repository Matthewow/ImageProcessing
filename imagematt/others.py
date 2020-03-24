"""
@author: WANG Zhao, Matthew
all copyright remained

the functions included in others
    |--- togray
    |--- power law
    |--- histogram equalization

    |--- average filter
    |--- max filter
    |--- min filter
    |--- median filter
    |--- laplacian filter
    |--- Sobel filter
"""
import numpy as np
import matplotlib.pyplot as plt


def togray(img):
    b = np.dot(img[..., :3], [1 / 3, 1 / 3, 1 / 3])
    b.astype(int)
    for i in range(0, np.shape(img)[0] - 1):
        for j in range(0, np.shape(img)[1] - 1):
            b[i][j] = int(b[i][j])
    return b


def showimg(img, img2, method):
    f = plt.figure()
    f.add_subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('original')
    f.add_subplot(1, 2, 2)
    plt.imshow(img2, cmap='gray')
    plt.title(method)
    plt.show(block=True)
