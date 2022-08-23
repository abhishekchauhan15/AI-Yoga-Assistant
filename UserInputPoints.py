import numpy as np
import cv2
import time 
import PoseModule as pm

cap=cv2.VideoCapture(0)

detector=pm.PoseDetector()
while True:
    success, img= cap.read()
    img= cv2.resize(img,(1280,728))
    # img=cv2.imread("asan.jpg")
    img=detector.findPose(img,False)
    lmlist=detector.getPosition(img,False)
    # print(lmlist)
    if len(lmlist) !=0:
        #right arm
        detector.findAngle(img,12,14,16)
        #left arm
        # detector.findAngle(img,11,13,15)
   
    cv2.imshow("Image", img)
    cv2.waitKey(1)