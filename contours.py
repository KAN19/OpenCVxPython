import cv2 as cv
import numpy as np

import sys

img = cv.imread('Image/Cat4.jpg')
cv.imshow("", img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)

# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny', canny)

# Threshold: Look in iamge and try to binarize the image. If intensity of particular pixel is below 125
# ==> Set to 0 == Black; Else set to 255 == white  
ret, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY) 
cv.imshow('Thresh', thresh)

# 59:54 coi ky lai
contours, hierachies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')

# Draw contours on a blank 
# Source, contours, index, color, thickness
cv.drawContours(blank, contours, -1, (255, 255, 255), 2)
cv.imshow('Draw contours', blank)

cv.waitKey(0)

