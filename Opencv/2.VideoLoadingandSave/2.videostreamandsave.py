import numpy as np
import cv2

cap = cv2.VideoCapture(0)

#note here is the codec being used, and the output information defined before the while loop.
#to save video we need four chacter codec info
fourcc = cv2.VideoWriter_fourcc(*'MP4V')

#this is output file data with file name and video dimenssions
out = cv2.VideoWriter('output_file_name.mp4',fourcc, 20.0, (640,480))

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    #writing the frames of video to output file continuosly untill the while loop inttrupt using q or direct close
    #you can also write modified frame into out file like out.write(gray)
    out.write(frame)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
