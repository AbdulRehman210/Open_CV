import cv2 as cv

img = cv.imread('./Pictures/cheem.jpg')

#resizing the image 200x200
reSizedImage= cv.resize(img,(200,200))

cv.imshow('Picture',reSizedImage)

cv.waitKey(0)