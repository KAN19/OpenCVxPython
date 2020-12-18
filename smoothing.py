import cv2 as cv

img = cv.imread('Image/Cat4.jpg')
cv.imshow("", img)

# Averaging 
average = cv.blur(img, (3,3))
cv.imshow('average', average)

#Gaussian blur 
# Object, width&height of small table, sigmaX
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian', gauss)

# Median blur 
median = cv.medianBlur(img, 3)
cv.imshow('Median', median)

# Bilateral blur
# object, diameter, sigmaColor, sigmaSpaces
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)

