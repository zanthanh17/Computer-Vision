from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

img_path = 'D:/computer vision/hinhanh/1.jpg'
img = Image.open(img_path)

#anh xam
gray_img = img.convert('L')

#chuyen anh xam ve mang
img_arr = np.array(gray_img)

#lam mo anh xam voi bo loc Gaussian
sigma1 = 0.5
blurred_img1 = ndimage.gaussian_filter(img_arr, sigma=0.5, mode = "constant")
blurred_img2= ndimage.gaussian_filter(img_arr, sigma=1, mode = "constant")
blurred_img3 = ndimage.gaussian_filter(img_arr, sigma=3, mode = "constant")

#hien thi anh
plt.subplot(2,2,1)
plt.imshow(gray_img, cmap = 'gray')
plt.title('Anh goc')

plt.subplot(2,2,2)
plt.imshow(blurred_img1, cmap = 'gray')
plt.title('sigma 0.5')

plt.subplot(2,2,3)
plt.imshow(blurred_img2, cmap = 'gray')
plt.title('sigma 1')

plt.subplot(2,2,4)
plt.imshow(blurred_img3, cmap = 'gray')
plt.title('sigma 3')
