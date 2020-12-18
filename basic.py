import cv2 as cv

img = cv.imread('Image/Cat3.jpg')

cv.imshow("", img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray channel', gray)

# Blur 
# object, odd number, 
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow(' ', dilated)

# Eroding 
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Erode', eroded)

# Resize
# By default, the interpolation= cv.INTER_AREA, which is useful to reduce the pictures
# In case enlarging, use the cv.INTER_CUBIC (better but slower), or INTER_LINEAR
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('reszied', resized)

#Cropping
# Select the region of image
cropped = img[0:200, 200:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)

