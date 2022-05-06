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
import math

app=Flask(__name__)

right_arm=-1
left_arm=-1
right_leg=-1
left_leg=-1



#loding the model

model=hub.load("https://tfhub.dev/google/movenet/multipose/lightning/1")
movenet=model.signatures['serving_default']


cap=cv2.VideoCapture(0)

detector=pm.PoseDetector()

dataList=data.AngleData




# print(dataList)


# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")


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



def compare():
    i=0
    for index in range(len(dataList)):
        # for key in dataList[index]:
        tadasan=[y for x, y in list(dataList[0].items()) if type(y) == int]
        vrksana=[y for x, y in list(dataList[1].items()) if type(y) == int]
        balasana=[y for x, y in list(dataList[2].items()) if type(y) == int]
        trikonasana=[y for x, y in list(dataList[3].items()) if type(y) == int]
        virabhadrasana=[y for x, y in list(dataList[4].items()) if type(y) == int]
        adhomukha=[y for x, y in list(dataList[5].items()) if type(y) == int]

        if tadasan[0]-right_arm<5 and tadasan[1]-left_arm<5 and tadasan[0]-right_leg<5 and tadasan[0]-left_leg<5:
            print('Pose is Accurate 😎')
        else:
            print('Try it again!!! 😐')
        
        
    

        
def generate_frames():
    while True:
            
        ## read the camera frame
        
        success, frame = cap.read()
        frame = cv2.flip(frame, 1)

        if not success:
            break
        else:
            #resize the image
            img=frame.copy()
            compare()

            img =tf.image.resize_with_pad(tf.expand_dims(img, axis=0), 192,256)
            input_img=tf.cast(img, dtype=tf.int32)
                
             # detecting the image
            results=movenet(input_img)
            keypoints_with_scores=results['output_0'].numpy()[:,:,:51].reshape((6,17,3)) #finding the main keypoints that we need for detection
            
             #showing the keypoints on to the screen
            loop_through_people(frame, keypoints_with_scores, EDGES, 0.1)
            cv2.imshow('Users Yoga Pose', frame)

            for index in range(len(dataList)):
                for key in dataList[index]:
                    print(dataList[index][key])

            # points detection 
            frame=detector.findPose(frame,False)
            lmlist=detector.getPosition(frame,False)
            # print(lmlist)
            if len(lmlist) !=0:
                #right arm
                right_arm= math.floor(detector.findAngle(frame,12,14,16))
                #left arm
                left_arm=math.floor(detector.findAngle(frame,11,13,15)) 
                #right leg
                right_leg=math.floor(detector.findAngle(frame,24,26,28)) 
                #left leg
                left_leg= math.floor(detector.findAngle(frame,23,25,27)) 

                

                
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
