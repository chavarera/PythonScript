import numpy as np
import cv2
img=cv2.imread('watch.jpg',cv2.IMREAD_COLOR)
px=img[127,127]
##now assign new values to selected pixelx
img[50,50]=[0,0,255]
#this will show the conversion of image to matrix data
print(px)

#to modify the color content of image
img[90:150,100:150]=[0,0,255] #img[100:150,100:150] these pixels in an image replaced with red color

#this is select area which one want to copy
select_watch=img[60:460,52:452]

#assign copied area pixels to new region of  image(ROI)
img[0:400,0:400]=select_watch

#to print out shape of and given image
print('Image shape:',img.shape)

#to print size of an image
print('Image size:',img.size)

#to print dtype of an image
print('dType:',img.dtype)


cv2.imshow('image title',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# read more tutorial here http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_basic_ops/py_basic_ops.html 
