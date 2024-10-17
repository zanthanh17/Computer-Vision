import cv2
import numpy as np


path = 'D:/computer vision/hinhanh/1.jpg'
img = cv2.imread(path)



#tach mau
# b,g,r = cv2.split(img)
# cv2.imshow('Red', r)
# cv2.imshow('Green', g)
# cv2.imshow('Blu', b)
# cv2.waitKey(15000)
# cv2.destroyAllWindows()

#chuyen anh sang mau xam
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray_img)
cv2.waitKey(15000)
cv2.destroyAllWindows()
