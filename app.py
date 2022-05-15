from flask import Flask,render_template,Response
from unittest import result
import numpy as np
import cv2
import time 
import PoseModule as pm
import tensorflow as tf
import tensorflow_hub as hub
from matplotlib import pyplot as plt
import data as data
# from threading import Timer
import win32api
import pyttsx3
import pythoncom
# import pywintypes
from time import sleep

app=Flask(__name__)


#loding the model

model = hub.load(r"C:\Users\welcome\Downloads\tf\movenet_multipose_lightning_1.tar")
# https://tfhub.dev/google/tfjs-model/movenet/multipose/lightning/1
# model = hub.load("https://tfhub.dev/google/movenet/multipose/lightning/1")
movenet = model.signatures['serving_default']


cap=cv2.VideoCapture(0)

detector=pm.PoseDetector()

dataList=data.AngleData
# print(dataList)


# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")


def make_1080p():
    cap.set(3, 1920)
    cap.set(4, 1080)

def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)

def make_480p():
    cap.set(3, 640)
    cap.set(4, 480)

def change_res(width, height):
    cap.set(3, width)
    cap.set(4, height)

    #drawing the keypoints

def draw_keypoints(frame, keypoints, confidence_threshold):
    y, x, c = frame.shape
    shaped = np.squeeze(np.multiply(keypoints, [y,x,1]))
    
    for kp in shaped:
        ky, kx, kp_conf = kp
        if kp_conf > confidence_threshold:
            cv2.circle(frame, (int(kx), int(ky)), 4, (0,255,0), -1) 

# drawing the edges

EDGES = {
    (0, 1): 'm',
    (0, 2): 'c',
    (1, 3): 'm',
    (2, 4): 'c',
    (0, 5): 'm',
    (0, 6): 'c',
    (5, 7): 'm',
    (7, 9): 'm',
    (6, 8): 'c',
    (8, 10): 'c',
    (5, 6): 'y',
    (5, 11): 'm',
    (6, 12): 'c',
    (11, 12): 'y',
    (11, 13): 'm',
    (13, 15): 'm',
    (12, 14): 'c',
    (14, 16): 'c'
}


# drawing the connections

def draw_connections(frame, keypoints, edges, confidence_threshold):
    y, x, c = frame.shape
    shaped = np.squeeze(np.multiply(keypoints, [y,x,1]))
    
    for edge, color in edges.items():
        p1, p2 = edge
        y1, x1, c1 = shaped[p1]
        y2, x2, c2 = shaped[p2]
        
        if (c1 > confidence_threshold) & (c2 > confidence_threshold):      
            cv2.line(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0,0,255), 2)
            
# looping through each person

def loop_through_people(frame, keypoints_with_scores, edges, confidence_threshold):
    for person in keypoints_with_scores:
        draw_connections(frame, person, edges, confidence_threshold)
        draw_keypoints(frame, person, confidence_threshold)

    

def speech(text):
    engine = pyttsx3.init() 
    engine.setProperty( "rate", 200 )
    engine.setProperty( "volume", 1.0 )
    engine.say(text) 
    engine.runAndWait()

def compare_right_arm(right_arm):
   
   
    # for index in range(len(dataList)):
            # for key in dataList[index]:

    tadasan=[y for x, y in list(dataList[0].items()) if type(y) == int]
    # vrksana=[y for x, y in list(dataList[1].items()) if type(y) == int]
    # balasana=[y for x, y in list(dataList[2].items()) if type(y) == int]
    # trikonasana=[y for x, y in list(dataList[3].items()) if type(y) == int]
    # virabhadrasana=[y for x, y in list(dataList[4].items()) if type(y) == int]
    # adhomukha=[y for x, y in list(dataList[5].items()) if type(y) == int]
        

        
    if abs(tadasan[0]-right_arm)<=10:
    #  and tadasan[1]-left_arm<5 and tadasan[0]-right_leg<5 and tadasan[0]-left_leg<5:
        sleep(10)
        speech("Your right arm is accurate") 
       
      
    else:
        sleep(10)
        speech("Right arm is not correct, try again")







def compare_left_arm(left_arm):
    # for index in range(len(dataList)):
            # for key in dataList[index]:

    tadasan=[y for x, y in list(dataList[0].items()) if type(y) == int]
        # vrksana=[y for x, y in list(dataList[1].items()) if type(y) == int]
        # balasana=[y for x, y in list(dataList[2].items()) if type(y) == int]
        # trikonasana=[y for x, y in list(dataList[3].items()) if type(y) == int]
        # virabhadrasana=[y for x, y in list(dataList[4].items()) if type(y) == int]
        # adhomukha=[y for x, y in list(dataList[5].items()) if type(y) == int]
        

        
        # if tadasan[1]-left_arm>0 and tadasan[1]-left_arm<50:
    if abs(tadasan[1]-left_arm)<=10:    
    #  and tadasan[1]-left_arm<5 and tadasan[0]-right_leg<5 and tadasan[0]-left_leg<5:
        sleep(10)
        
        speech("Your left arm is accurate") 
           
    else:
        sleep(10)
        
        speech("Your left arm is not accurate , try again")
    
    
    



def compare_right_leg(right_leg):
    tadasan=[y for x, y in list(dataList[0].items()) if type(y) == int]
        # vrksana=[y for x, y in list(dataList[1].items()) if type(y) == int]
        # balasana=[y for x, y in list(dataList[2].items()) if type(y) == int]
        # trikonasana=[y for x, y in list(dataList[3].items()) if type(y) == int]
        # virabhadrasana=[y for x, y in list(dataList[4].items()) if type(y) == int]
        # adhomukha=[y for x, y in list(dataList[5].items()) if type(y) == int]
        
    if abs(tadasan[2]-right_leg)<=10:
    #  and tadasan[1]-left_arm<5 and tadasan[0]-right_leg<5 and tadasan[0]-left_leg<5:
        sleep(10)
        speech("Your right leg is accurate")         
    else:
        sleep(10)
        speech("Your right leg is not accurate, try again") 
        
       




def compare_left_leg(left_leg):
    # for index in range(len(dataList)):
            # for key in dataList[index]:

    tadasan=[y for x, y in list(dataList[0].items()) if type(y) == int]
        # vrksana=[y for x, y in list(dataList[1].items()) if type(y) == int]
        # balasana=[y for x, y in list(dataList[2].items()) if type(y) == int]
        # trikonasana=[y for x, y in list(dataList[3].items()) if type(y) == int]
        # virabhadrasana=[y for x, y in list(dataList[4].items()) if type(y) == int]
        # adhomukha=[y for x, y in list(dataList[5].items()) if type(y) == int]
        

        
    if abs(tadasan[3]-left_leg)<=10:
    #  and tadasan[1]-left_arm<5 and tadasan[0]-right_leg<5 and tadasan[0]-left_leg<5:
       speech("Your left leg is accurate") 
     
    else:
        speech("Your left leg is not accurate, try again") 


   
        
    

 
def generate_frames():
    # timeout=800
    # timeout_start=time.time()
    # while time.time()<timeout_start+timeout:
    while True:
            
        ## read the camera frame
        
        success, frame = cap.read()
        frame = cv2.flip(frame, 1)

        #resize the image
        img=frame.copy()
         

        img =tf.image.resize_with_pad(tf.expand_dims(img, axis=0), 192,256)
        input_img=tf.cast(img, dtype=tf.int32)
            
        # detecting the image
        results=movenet(input_img)
        keypoints_with_scores=results['output_0'].numpy()[:,:,:51].reshape((6,17,3)) #finding the main keypoints that we need for detection
        
            #showing the keypoints on to the screen
        loop_through_people(frame, keypoints_with_scores, EDGES, 0.1)
        cv2.imshow('Users Yoga Pose', frame)

        

        # points detection 
        frame=detector.findPose(frame,False)
        lmlist=detector.getPosition(frame,False)

        # compare()
        # print(lmlist)
        
        if len(lmlist) !=0:
                
            #right arm
            angle=int(detector.findAngle(frame,12,14,16))
            # print("right_arm :", angle)
            # compare_right_arm(angle)
            
            
            
            #left arm
            angle=int(detector.findAngle(frame,11,13,15))
            # print("left_Arm :", angle)
            # compare_left_arm(angle)
        
            
            
            #right leg
            angle=int(detector.findAngle(frame,24,26,28))
            # print("right_leg :", angle)
            # compare_right_leg(angle)
            
            
            
            #left leg
            angle=int(detector.findAngle(frame,23,25,27))
            # print("left_leg :", angle)
            # compare_left_leg(angle)

                
                
            
        # cv2.imshow("Image", frame)
        cv2.waitKey(1) 

        ret,buffer=cv2.imencode('.jpg',frame)
        frame=buffer.tobytes()

        yield(b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


                     


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug=True)