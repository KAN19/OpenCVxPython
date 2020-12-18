import cv2 as cv 
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('rectangle', rectangle)
cv.imshow('circle', circle)

# bitwise AND
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('And', bitwise_and)

# bitwise OR
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('OR', bitwise_or)

# bitwise XOR
# Non-intersecting region 
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('XOR', bitwise_xor)

# bitwise NOT 
# Inverse the binary color 
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Not', bitwise_not)

cv.waitKey(0)