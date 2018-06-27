import cv2
import numpy as np
##Simple read image
img=cv2.imread('bookpage.jpg')


##convert image to grayscale
grayscale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#NOrmal Threshold
'''
A binary threshold is a simple "either or" threshold, where the pixels are either 255 or 0.
parameter
1.image (img)
2.threshold(We are choosing 10, because this is a low-light picture, so we choose a low number. Normally something about 125-150 would probably work best)
3.maximum value we are choosing
4.type of threshold (cv2.THRESH_BINARY)
'''
retval,threshold=cv2.threshold(grayscale,12,255,cv2.THRESH_BINARY)

#Adaptive Threshold
'''
parameter
1.image(grayscale normally)
2.maximum value
3.type of threshold (2 diffrennt type one is ADAPTIVE_THRESH_GAUSSIAN_C and second one is THRESH_BINARY)
'''
th=cv2.adaptiveThreshold(grayscale,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
cv2.imshow('original image',img)
cv2.imshow('threshold image',th)
cv2.imwrite('output1.jpg',th)
cv2.waitKey(0)
cv2.destroyAllWindows()
