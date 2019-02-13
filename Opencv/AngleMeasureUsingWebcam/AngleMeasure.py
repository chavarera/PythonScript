####################################
# File name : AngleMeasure.py      #
# Author    : Ravishankar Chavare  #
# Date created: 13/02/2019         #
# Python Version: 3.7              #
####################################

'''
This program is Created using opencv,numpy and math libraries
To measure the angle between Two Red and Blue Colored Objects

Following Steps Are Used

1.Import Required libraries
2.Create A class and two method (run,AreaDefine)
3.Initialize the Camera(Webcam using the cv.VideoCapture(0))
4.get Height and Width of Image Capture using(cv.CAP_PROP_FRAME_HEIGHT,cv.CAP_PROP_FRAME_Width)
5.Now Create 4-5 blank images using np(1.HSV,2.Red Color combination,3.Another red Combination,4.Blue Color Combination)
6.Now read The Every Frame Using While Loop
7.Convert normal Image To hsv image using cv.cvtColor(img,cv.COLOR_BGR2HSV)
8.now define Threshold values lower and upper color range for both red and blue (you can use multiple combination and the add it using cv.add(img,img2))
9.Now Findout moments for both color(this is the area of an selected object)
10.Find out he area(Example:area=redmoment["m00"])
10.noise in the video so ignore objects with small areas by condtioning the area
11.now Find out the center of area by substarcting the m00 from moment['m10'] andmoment['m01'](x1,y1 will get Here) 
12.Do 11 Step For blue object also(you will find it x2,y2)
13.Draw lines using points
14.Now measure angle using math function

and put the text on Image

'''

#------Required Lib-------
import cv2 as cv
import math
import numpy as np


#-------------------------

class Angle:
    def __init__(self):
        #From Video File
        #self.capture=cv.VideoCapture("redobj.mp4")
        #Live Streaming
        self.capture=cv.VideoCapture(0)
        
    def AreaDefine(self,moments1,area1,img,font):
        #x and y coordinates of the center of the object is found by dividing the 1,0 and 0,1 moments by the area
        x1=int(moments1['m10']/area1)
        y1=int(moments1['m01']/area1)

        #draw circle
        cv.circle(img,(x1,y1),2,(0,255,0),20)

        #write x and y position
        cv.putText(img,str(x1)+","+str(y1),(x1,y1+20),font, 1,(255,255,255)) #Draw the text
        return x1,y1
    def run(self):
        #Initialize Basics
        #font=
        font=cv.FONT_HERSHEY_SIMPLEX

        #Frame Height and Width
        frame_height = int(self.capture.get(cv.CAP_PROP_FRAME_HEIGHT))
        frame_width = int(self.capture.get(cv.CAP_PROP_FRAME_WIDTH))


        #Now create Blank 4 images with numpy Zeros
        hsv_img=np.zeros((frame_height,frame_width,3),dtype=np.uint8)#create blank image
        threshold_img1 = np.zeros((frame_height, frame_width, 1), dtype=np.uint8)
        threshold_img1a = np.zeros((frame_height, frame_width, 1), dtype=np.uint8)
        threshold_img2 = np.zeros((frame_height, frame_width, 1), dtype=np.uint8)

        
        #Frame Count Start From 0
        i=0

        #Now time to Detect Every Frame using infinite loop

        while True:
            #Get the Ret and image from Camera
            ret,img=self.capture.read()

            #opencv Read Image into BGR Color Channel Now convert it into hsv_img
            hsv_img=cv.cvtColor(img,cv.COLOR_BGR2HSV)
            
            '''--------------------------Red Color Object -------------------------------------------'''
            #Now define lowerthreeshold and higher threeshold to detect color ranges
            #1(Red Part Limit)For Red (h and s value max upto 250 and v max value upto 180)
            lower_red=(165,145,100)
            higher_red=(250,210,160)
            cv.inRange(hsv_img,lower_red,higher_red,threshold_img1)
            
            #2(Red Part Limit)red again you can also pass the value to get Inrange Function directly
            cv.inRange(hsv_img,(0,145,100),(10,210,160),threshold_img1a)
            
            #Now add Both Limits
            cv.add(threshold_img1,threshold_img1a)
            '''----------------------------------------------------------------------------------'''

            '''------------------------Blue Color Objects-------------'''
            lower_blue=(105,180,40)
            higher_blue=(120,260,100)

            cv.inRange(hsv_img,lower_blue,higher_blue,threshold_img2)
            '''-------------------------------------------------------'''

            '''-------Now find moments of object using cv2-----------------'''
            redmoment=cv.moments(threshold_img1)
            bluemoment=cv.moments(threshold_img2)

            # Moments area stored in dictionary and key is 'm00'
            area1=redmoment["m00"]
            area2=bluemoment["m00"]
            x1,y1,x2,y2=(1,2,3,4)
            coord_list=[x1,y1,x2,y2]
            for x in coord_list:
                x=0
                
            '''-------------This is Code for Slecteting red area center and writing its ----------------'''
            #there can be noise in the video so ignore objects with small areas
            if (area1 >200000):
                x1,y1=self.AreaDefine(redmoment,area1,img,font)
                
            '''------------------------------------------------------------------------------------------'''
            '''-------------This is Code for Slecteting Blue area center and writing its ----------------'''
            if (area2 >100000):
                x2,y2=self.AreaDefine(bluemoment,area2,img,font)
            '''------------------------------------------------------------------------------------------'''
            
            #Draw Lines using above points the point values are updated
            if(x1!=1 and y1!=2 and x2!=3 and y2!=4):
                cv.line(img,(x1,y1),(x2,y2),(0,0,255),10)
                cv.line(img,(x1,y1),(int(frame_height/2), int(frame_width/2)),(100,100,100,100),4,cv.LINE_AA)
                cv.line(img,(x2,y2),(int(frame_height/2), int(frame_width/2)),(00,100,100,100),4,cv.LINE_AA)
                
                #Calculate Angle
                x1=float(x1)
                y1=float(y1)
                x2=float(x2)
                y2=float(y2)
                try:
                    angle = int(math.atan((y1-y2)/(x2-x1))*180/math.pi)
                    cv.putText(img,str(angle),(200,200),font, 1,(255,255,255)) #Draw the text
                except:
                    pass
            '''Now Code '''
            #Printing Normal Video Stream
            cv.imshow("Current Video",img)
            
            #If You Press Escape Then It Will Exit From Loop
            '''27-Ascii Keyboard value of Esc key
            113-Ascii keyboard value of Q key
            You Can use both (Q and Esc) To Quit the Window'''
            c = cv.waitKey(7) % 0x100
            if c == 27 or c == 113:
                break
        #This Will Close the Window of running cv 
        cv.destroyAllWindows()
            
if __name__=="__main__":
    t = Angle()
    t.run()    
