import numpy as np
import cv2

'''this will start webcam for recording where 0 means that you are using inbuilt webcam
when you have multiple webcam connected to system you can assign here as 0,1 or 2
'''
cap = cv2.VideoCapture(0)

#this is simple infinite loop for video capture
while(True):
    #this will continuosly adding frames
    ret, frame = cap.read()

    #open cv support blue green red(BGR) format
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #show the video stream 
    cv2.imshow('frame',gray)
    '''
    cv2.waitKey(1):when you press 1 key then it will show last captured frame
    0xFF == ord('q'):this will help us to quit the window
    '''
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release() #release the webcam
cv2.destroyAllWindows()#close all the frames windows
