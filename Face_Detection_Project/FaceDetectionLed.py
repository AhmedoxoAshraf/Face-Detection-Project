import cv2 #imports opencv library used for computer vision and image & video processing

from cvzone.FaceDetectionModule import FaceDetector # from the cvzone library import the FaceDetection module 
# and from the FaceDetection module import FaceDetector class which will help in face detection

from cvzone.SerialModule import SerialObject # from the cvzone library import SerialModule
# form SerialModule import SerialObject class to connect to the arduino using serial port

########### to install libraries : in the terminal write "pip install (library name)" #######################

cap=cv2.VideoCapture(0) # opens camera and start taking frames from it and store them in Cap
detector = FaceDetector() # it will start the face detections from the frames
arduino=SerialObject('COM14') # it will start sending serial data to arduino through the port ('COM14')

while True: #infinte loop
    success,img = cap.read() # reads the frames that are stored in cap then stores them in (img)
    # (success) indicates if the frames are read successfuly or not

    img, bBoxs = detector.findFaces(img) # detect face in the frames inside (img)
    #  and put the face in a box and return the face with the box to (bBox)

    if bBoxs: # checks if a face is detected or not
        arduino.sendData([1,0]) # sends data to the arduino to turn on the first output
    else :
        arduino.sendData([0,1]) # sends data to the arduino to turn on the second output

    cv2.imshow("Ahmed Ashraf", img) # display the image in a window (face with box around it)

    cv2.waitKey(1) # wait for a key press for 1 millisecond 
 