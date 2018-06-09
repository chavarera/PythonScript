import cv2 # oopen cv import
import numpy as np
from matplotlib import pyplot as plt # matplotlib for image showing

#to read images use cv2.imread('imagepath',imagescale)
'''
-1:unchanged
0:grayscale
1:color

you can either use 0,-1,1 or IMREAD_GRAYSCALE,cv2.IMREAD_COLOR,cv2.IMREAD_UNCHANGED
'''
img = cv2.imread('watch.jpg',0)

# plot image on matplot using plt.imgshow(img)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis

# if you want to save image after all modification you can use cv2.imwrite('image name',img)
cv2.imwrite('watchgray.png',img)

#show Image in plot
plt.show()
