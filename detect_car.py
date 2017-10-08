
#  Author- vaibhav sushn


import numpy as np
import cv2
import RPi.GPIO as GPIO
import time
import thread

#Setting the GPIOs
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)

GPIO.setup(10,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.output(3,False)
GPIO.output(5,False)
GPIO.output(7,False)
GPIO.output(11,False)
GPIO.output(13,False)
GPIO.output(15,False)
GPIO.output(8,False)
GPIO.output(10,False)
GPIO.output(12,False)
GPIO.output(19,False)
GPIO.output(21,False)
GPIO.output(23,False)


a=1
b=1
c=1
d=1


def timeralg();
	while(1):
	c1=a
	c2=bs
	c3=c
	c4=d
	print 'count c1=',c1
	print 'count c2=',c2
	print 'count c3=',c3
	print 'count c4=',c4
	t=[4,4,4,6,6,20,24,28,32,36,40]#delay determining array

	for y in range(0,4):
		if ((c1>=c2)and(c1>=c3)and(c1>=c4)):
			print 'timer1 on for '
			x=t[c1]
			print x
			c1=0
			GPIO.outpu(21,True)#RED4
			GPIO.output(5,False)#RED1
			GPIO.output(13,True)#RED2
			GPIO.output(7,True)#GREEN1
			GPIO.output(12,True)#RED3
			time.sleep(x)
			GPIO.output(7,False)#GREEN1OFF
			GPIO.outpu(3,True)#YELLOW1
			time.sleep(3)
			GPIO.output(5,True)#RED1
			elif ((c2>=c1)and(c2>=c3)and(c2>=c4)):
				print 'time2 on for '
				x=t[c2]
				print x
				c2=0
				GPIO.outpu(21,True)#RED4
				GPIO.output(5,True)#RED1
				GPIO.output(13,False)#RED2
				GPIO.output(12,True)#RED3
				GPIO.output(11,True)#GREEN2
				time.sleep(x)
				GPIO.output(11,False)#GREEN2
				GPIO.outpu(15,True)#YELLOW2
				time.sleep(3)
				GPIO.output(15,False)#YELLOW2
				GPIO.output(13,True)#

			elif ((c3>=c1)and(c3>=c2)and(c3>=c4)):
				print 'timer3 on for '
				x=t[c3]
				print x
				c3=0
				GPIO.outpu(21,True)#RED4
				GPIO.output(5,True)#RED1
				GPIO.output(13,True)#RED2
				GPIO.output(12,False)#RED3
				GPIO.output(8,True)#GREEN3
				time.sleep(x)
				GPIO.output(8,False)#GREEN3
				GPIO.outpu(10,True)#YELLOW3
				time.sleep(3)
				GPIO.output(10,False)#YELLOW3
				GPIO.output(12,True)#RED3

			elif ((c4>=c1)and(c4>=c2)and(c4>=c3)):
				print 'timer4 on for '
				x=t[c4]
				print x
				c4=0
				GPIO.outpu(21,False)#RED4
				GPIO.output(5,True)#RED1
				GPIO.output(13,True)#RED2
				GPIO.output(12,True)#RED3
				GPIO.output(19,True)#GREEN4
				time.sleep(x)
				GPIO.output(19,False)#GREEN4
				GPIO.outpu(23,True)#YELLOW4
				time.sleep(3)
				GPIO.output(23,False)#YELLOW4
				GPIO.output(21,True)#RED4

###################################################### Cardetection algortihm ###########################################################
def cardetection(imgscbg,imgscfg):
    #bg_scale=cv2.resize(image_background,(200,100))
        #fg_scale=cv2.resize(image_foreground,(200,100))
        #Scaled the images
    sub=cv2.subtract(imgscfg,imgscbg)
    gray_image=cv2.cvtColor(sub,cv2.COLOR_BGR2GRAY)
        #creating trackbar
    cv2.createTrackbar('thresholdg','Threshold',100,255,nothing)
        #getting trackbar postion
    t1tb = cv2.getTrackbarPos('thresholdg','Threshold')
        #exptal value for threshold =110
    ret,thresholdg = cv2.threshold(gray_image,25,255,cv2.THRESH_BINARY)#Found the threshold value with the help of trackbar

        #Create kernel for morphological operation
    kernel1 = np.ones((3,3),np.uint8)
        #Opening Operation
    opening = cv2.morphologyEx(thresholdg, cv2.MORPH_OPEN, kernel1)
      #Closing Operation
    kernel2 = np.ones((51,51),np.uint8)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel2)

        #Finding Contours
        #copy the image
    copy_thresh=closing
    contours, hierarchy = cv2.findContours(copy_thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    clen=len(contours)
    #print clen
    c_count=0
    for l in range (1,clen):
        area=cv2.contourArea(contours[l])
        #print area  #for getting the area threshold
        if(area>1000):
            c_count=c_count+1
            x,y,w,h = cv2.boundingRect(contours[l])
            cv2.rectangle(imgcopy,(x,y),(x+w,y+h),(01,255,0),2)
    return c_count
    cv2.imshow('Detected cars',imgcopy)

############################################# Started timgalgorihtm as a new thread ######################################################
thread.start_new_thread(timeralg,())

################################################### main thread ####################################################################
while(1):
	cap=c2.VideoCapture(0)
	cap.set(3,320)
	cap.set(4,240)
	ret,frame=cap.read()
	imgscfg=frame
	cap.release()
	imgscbg=cv2.imread('Back0.jpg')#Load Background image
	imgcopy=imgscfg
	vehicle0=cardetection(imgscbg,imgscfg)#Call detection function
	a=vehicle0
	if (a==0):
		a=1
	#C2
	cap=c2.VideoCapture(1)
	cap.set(3,320)
	cap.set(4,240)
	ret,frame=cap.read()
	imgscfg=frame
	cap.release()
	imgscbg=cv2.imread('Back1.jpg')#Load Background image
	imgcopy=imgscfg
	vehicle1=cardetection(imgscbg,imgscfg)#Call detection function
	b=vehicle1
	if (b==0):
		b=1

	#C3
	cap=c2.VideoCapture(2)
	cap.set(3,320)
	cap.set(4,240)
	ret,frame=cap.read()
	imgscfg=frame
	cap.release()
	imgscbg=cv2.imread('Back2.jpg')#Load Background image
	imgcopy=imgscfg
	vehicle2=cardetection(imgscbg,imgscfg)#Call detection function
	c=vehicle2
	if (c==0):
		c=1
	#C4
	cap=c2.VideoCapture(3)
	cap.set(3,320)
	cap.set(4,240)
	ret,frame=cap.read()
	imgscfg=frame
	cap.release()
	imgscbg=cv2.imread('Back3.jpg')#Load Background image
	imgcopy=imgscfg
	vehicle3=cardetection(imgscbg,imgscfg)#Call detection function
	d=vehicle3
	if (d==0):
		d=1
