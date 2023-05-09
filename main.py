import cv2
import numpy as np

img = cv2.imread(r'C:\Users\ibrahim\Desktop\manzara.jpg')

blue, green, red = cv2.split(img)

green.fill(0)

red = np.clip(red + 50, 0, 255)
blue = np.clip(blue + 50, 0, 255)

divided_img = cv2.merge((blue, green, red))

cv2.imshow('Divided Image', divided_img)
cv2.waitKey(0)

original_img = cv2.merge((blue, green, red))

cv2.imshow('Original Image', original_img)
cv2.waitKey(0)