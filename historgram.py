import cv2 as cv
import matplotlib.pyplot as plt 
import numpy as np 

img = cv.imread('Image/Cat4.jpg')
cv.imshow("", img)

# Create Mask
blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

# mask = cv.bitwise_and(gray, gray, mask=circle)
# cv.imshow('Masked', mask)

# GRayscale histogram
# mask = none if there isnt any mask
# gray_hist = cv.calcHist([gray], [0], circle, [256], [0,256])
# plt.figure() 
# plt.title('Grayscale histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels') 
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# Color Histogram 
mask = cv.bitwise_and(img, img, mask=circle)
cv.imshow('Mask', mask)

plt.figure()
plt.title('Color Scale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels') 
colors = ('b', 'g', 'r') 
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], circle, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)

