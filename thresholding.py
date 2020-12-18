import cv2 as cv

img = cv.imread('Image/Cat3.jpg')
cv.imshow("", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding 
threshold, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

# Inverse
threshold, thresh_inv = cv.threshold(gray, 125, 255, cv.THRESH_BINARY_INV)
cv.imshow('Thresh', thresh_inv)



cv.waitKey(0)

