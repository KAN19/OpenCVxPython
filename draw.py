import cv2 as cv
import numpy as np 

# width, height and color channel
blank = np.zeros((500,500, 3), dtype = 'uint8')
cv.imshow('blank', blank)

# # 1. Paint the image a certain color 
# # blank[:] = 0, 255, 0 
# # cv.imshow('green', blank)

# # 2. Draw a rectangle 
# # object, startpoint, endpoint, color, thickness
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=2)
# cv.imshow('rectangle', blank)

# # 3. Draw a circle 
# # object, dimension, radius, color, thickness
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
# cv.imshow('Circle', blank)

# # 4. Draw line 
# # Tuong tu Draw rectangle 

# 5. Write text 
cv.putText(blank, 'Hello', (225, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,255), 2)
cv.imshow('Text', blank)

cv.waitKey(0)