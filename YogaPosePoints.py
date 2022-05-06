import numpy as np
import cv2
import time 
import PoseModule as pm

cap=cv2.VideoCapture(0)

detector=pm.PoseDetector()

while True:
    # success, img= cap.read()
    # img= cv2.resize(img,(1280,728))
    img=cv2.imread("images/tadasan.jpg")
    # img=cv2.imread("images/vrksana.jpg")
    # img=cv2.imread("images/trikonasana.jpg")
    # img=cv2.imread("images/virabhadrasana.jpg")
    # img=cv2.imread("images/adho_mukha.jpeg")
    # img=cv2.imread("images/balasana.jpg")
    img=detector.findPose(img,False)
    lmlist=detector.getPosition(img,False)
    # print(lmlist)
    if len(lmlist) !=0:
        #right arm
        right_arm=detector.findAngle(img,12,14,16)
        #left arm
        left_arm=detector.findAngle(img,11,13,15)
        #right leg
        right_leg=detector.findAngle(img,24,26,28)
        #left leg
        left_leg=detector.findAngle(img,23,25,27)

     #storing the angle data of 6 yoga poses   
    AngleData = [{'Name': 'tadasan', 'right_arm': 201, 'left_arm': 162, 'right_leg':177,'left_leg':182},
    {'Name': 'vrksana', 'right_arm': 207, 'left_arm': 158, 'right_leg':180,'left_leg':329},
    {'Name': 'balasana', 'right_arm': 155, 'left_arm': 167, 'right_leg':337,'left_leg':335},
    {'Name': 'trikonasana', 'right_arm': 181, 'left_arm': 184, 'right_leg':176,'left_leg':182},
    {'Name': 'virabhadrasana', 'right_arm': 167, 'left_arm': 166, 'right_leg':273,'left_leg':178},
    {'Name': 'adhomukha', 'right_arm': 176, 'left_arm': 171, 'right_leg':177,'left_leg':179}]

   
    cv2.imshow("Image", img)
    cv2.waitKey(1)

    
