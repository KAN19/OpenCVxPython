import cv2 as cv 

img = cv.imread('Image/Cat1.jpg') 
cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # Live videos
    capture.set(3, width)
    capture.set(4, height)

resize_image = rescaleFrame(img)
cv.imshow("", resize_image)

# Video capture
# capture = cv.VideoCapture('Video/video1.mp4')

# while True:
#     isTrue, frame = capture.read()

#     frame_resized = rescaleFrame(frame)

#     cv.imshow('Video', frame)
#     cv.imshow('Videoresized', frame_resized)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
cv.waitKey(0)