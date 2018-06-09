import numpy as np
import cv2

img = cv2.imread('watch.jpg',cv2.IMREAD_COLOR)

#Draw Line
'''
To draw simple line on image 5 element to cv2.line
1.img object
2.starting point like (0,0)
3.ending point(150,150)
4.color in form of 255 value(open cv support BGR format (255,0,0)->blue,(0,255,0)->Green,(0,0,255)->red,(0,0,0)->black,(255,255,255)->white)
5.the width of an line to be drawn
'''

cv2.line(img,(0,0),(150,150),(0,0,255),10)


#Draw Reactangle
'''
1.img
2.starting postion
3.ending position
4.color
5.width
'''
cv2.rectangle(img,(15,15),(200,150),(0,255,0))


#Draw Circle
'''
TO draw circle
1.img
2.center of circle
3.radious
4.color
5.1->without fill
  -1->solid fill

'''
cv2.circle(img,(100,63),55,(255,0,0),1)


#Draw Text on Image
'''
1.img
2.Text to show
3.origin of text
4.font
5.fontscale
6.color
7.text thickness
8.line
'''
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'This is Tutorial',(0,100),font,1,(0,0,0),2,cv2.LINE_AA)

#Show the modified image
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
