import numpy as np
import cv2
import time 
import PoseModule as pm

cap=cv2.VideoCapture("Abhay_Trik.mp4")
img=cv2.imread("asan.jpg")
detector=pm.poseDetector()

while True:
    # success, img= cap.read()
    # img= cv2.resize(img,(1280,728))
    img=detector.findPose(img)

   
    cv2.imshow("Image", img)
    cv2.waitKey(1)