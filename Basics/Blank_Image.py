import cv2 as cv
import numpy as np

#setting dimensions of new picture
blankImg = np.zeros((600,600,3),dtype='uint8')

#setting color for picture pixels
#in entire page color white
blankImg[:] = 255,255,255

#showing up new Image
cv.imshow('Blank Image',blankImg)



cv.waitKey(0)