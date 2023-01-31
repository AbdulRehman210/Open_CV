import cv2  as cv

#reading image by providing path

img = cv.imread('./Pictures/cheem.jpg')

#displaying the image
#where first parameter is image window name

cv.imshow('Picture',img)

#using 0 (miliseconds) as parameter for displaying picture untill any key pressed

cv.waitKey(0)