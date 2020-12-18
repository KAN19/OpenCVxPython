import cv2 as cv
import numpy as np 

img = cv.imread('Image/Cat4.jpg')
cv.imshow("", img)

# The dimension of the mask has to be the same size as ......
# Attribute img.shape[:2] will take the width and height of the source image
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

mask = cv.circle(blank, (img.shape[1]//2 -30, img.shape[0]//2 - 60), 200, 255, -1)
cv.imshow('Mask', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked image', masked)

cv.waitKey(0)

