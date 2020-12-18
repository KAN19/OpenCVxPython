import cv2 as cv
import numpy as np 

img = cv.imread('Image/Cat4.jpg')

cv.imshow("", img)

# Translation image
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimension = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat,dimension)


translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

# Rotation image
def Rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotatedImage = Rotate(img, 45)
cv.imshow('Rotated', rotatedImage)

# Resizing 
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resize', resized)

# Fliping 
# 1 : Horizonting
# 0: Vertical
# -1: Both
flip = cv.flip(img, 1)
cv.imshow('Flip', flip)

cv.waitKey(0)

