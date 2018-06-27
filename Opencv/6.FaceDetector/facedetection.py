import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier('face.xml')
eye_cascade = cv2.CascadeClassifier('eye.xml')
smile_cascade=cv2.CascadeClassifier('smile.xml')

cap=cv2.VideoCapture(0)
while(True):
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    
    # Detects faces of different sizes in the input image
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    
    for (x,y,w,h) in faces:
        print(x,y,w,h)
        #print(f) # print face found data
        
        #this will draw a green rectangle on face
        cv2.rectangle(img,(x,y),(x+h,y+w),(0,255,0),2)
        font=cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,'Person found',(x,y+w+30),font,1,(0,127,255),2,cv2.LINE_AA)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=img[y:y+h,x:x+w]

        #Detect eyes of different sizes in the input image
        eyes=eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            print('eyes',ex,ey,ew,eh)
            cv2.rectangle(roi_color,(ex,ey),(ex+eh,ey+ew),(0,0,255),2)


        smiles=smile_cascade.detectMultiScale(roi_gray)

        for s in smiles:
            print('i know you are now smiling')

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #show modified image
    cv2.imshow('image',img)
cap.release()
cv2.destroyAllWindows()
    
