%matplotlib inline #required on mac for histogram

import cv2 #opencv
import numpy as np #using nump for all calcs
import os #system misc like os.fopen()
import glob
from matplotlib import pyplot as plt #histogram


Vya=[]#if there are grey vehicles
Vno=[]#if there aren't any (collect data)

VnoPath=['banana.jpg' , 'curds.jpg', 'tomato.jpg', 'milindsSuziki.jpg', 'PenIsland.jpg', 'modi.jpg']
VyaPath=['blackAndWhiteCars','....']

#input images here
for path in VnoPath:
    newPath =os.path.join(path, "*.jpg") #this will catenate all the images into
                        #one so opencv knows what not to do
    for inflile in glob.glob(newPath):
        Vno.append(infile)#add no vehicles to the array

for path in VyaPath:
    newPath=os.path.join(path, "*.jpg")
    for infile in glob.glob(newPath)
        Vya.append(infile)#add yes vehicles to the array

def checkVehicl(yesList, noList):#pass Vya and Vno
    Vdata={}
    Vdata["numOfVeh"]= len(Vya)# to store the number of cars into a str
    #so we can use this later
    Vdata["numOfNotVeh"]=len(Vno)
    i=0
    while(i<=len(Vya))
        Vdata["ConvertedPics"]=(convertedInput[i], convertedInput[i++])


    testImg=cv2.imread(Vya[0])
        testImgShape=testImg.shape
        #find out the shape using opencv
        #if its a rectange we can use it directly, else we have to use
        #histograms to draw rectangles around images for analysis

    i=0
    while(i<=len(Vya)):
        Vdata["shapes"]= (testImgShape[i], testImgShape[i++])
        #saves all the shapes
    return Vdata

vehiInfo=checkVehicl(Vya, Vno)#call this for information

print("\nVehicle Information:\n", vehiInfo)


print("\n\nInformation is being generated. Press "S" key to STOP and EXIT\n")
#convert inputs to greyscale before testing calling checkVehicl()
while True:#while(1)
    inputImg= cv2.imread(img, 0)
    keyPress=cv2.waitKey(0)
    if(keyPress=83 or 115)
        print("\nThank you for pressing "S". Stopped.\n")
        break

    #set image to greyscale mode
    convertedInput=inputImg.cvtColor(img, cv2.COLOR_BGR2GRAY)
    for infile in glob.glob(newPath)
        Vdata.append(infile)
    return checkVehicl(Vya, Vno)

    #while input is true, keep calling the function to change color
