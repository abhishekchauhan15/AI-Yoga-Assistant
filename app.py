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
import win32api
import pyttsx3
import pythoncom
from time import sleep
import schedule
import time
import matplotlib.pyplot as plt
import gtts  
from playsound import playsound  

app=Flask(__name__)
#loding the model


# model = hub.load(r"C:\Users\welcome\Downloads\movenet_multipose_lightning_1.tar")
# https://tfhub.dev/google/tfjs-model/movenet/multipose/lightning/1
model = hub.load("https://tfhub.dev/google/movenet/multipose/lightning/1")
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

    

# def speech(text):
#     engine = pyttsx3.init() 
#     # engine.setProperty( "rate", 200 )
#     # engine.setProperty( "volume", 1.0 )
#     engine.say(text) 
#     # engine.runAndWait()



def compare_right_arm(right_arm):
    tadasan=[y for x, y in list(dataList[0].items()) if type(y) == int]
    
    # vrksana=[y for x, y in list(dataList[1].items()) if type(y) == int]
    # balasana=[y for x, y in list(dataList[2].items()) if type(y) == int]
    # trikonasana=[y for x, y in list(dataList[3].items()) if type(y) == int]
    # virabhadrasana=[y for x, y in list(dataList[4].items()) if type(y) == int]
    # adhomukha=[y for x, y in list(dataList[5].items()) if type(y) == int]
        
    if(right_arm<=tadasan[0]):
        acc=(right_arm/tadasan[0])*100
    else:
        acc=0
        
    if abs(tadasan[0]-right_arm)<=10:
    #  and tadasan[1]-left_arm<5 and tadasan[0]-right_leg<5 and tadasan[0]-left_leg<5:
        # sleep(10)
        print("Your right arm is accurate")
        # t1 = gtts.gTTS("Your right arm is accurate") 
        # t1.save("right_arm.mp3")    
        # playsound("right_arm.mp3")  

        # speech("Your right arm is accurate") 
    else:
        # sleep(10)
        print("Your right arm is not accurate")
        # speech("Right arm is not correct, try again")
        # t1 = gtts.gTTS("Your right arm is not accurate") 
        # t1.save("right_arm_no.mp3")    
        # playsound("right_arm_no.mp3")  

    return acc


def compare_left_arm(left_arm):
    # for index in range(len(dataList)):
            # for key in dataList[index]:

    tadasan=[y for x, y in list(dataList[0].items()) if type(y) == int]
        # vrksana=[y for x, y in list(dataList[1].items()) if type(y) == int]
        # balasana=[y for x, y in list(dataList[2].items()) if type(y) == int]
        # trikonasana=[y for x, y in list(dataList[3].items()) if type(y) == int]
        # virabhadrasana=[y for x, y in list(dataList[4].items()) if type(y) == int]
        # adhomukha=[y for x, y in list(dataList[5].items()) if type(y) == int]
        
    if(left_arm<=tadasan[1]):
            acc=(left_arm/tadasan[1])*100
    else:
        acc=0
        
        # if tadasan[1]-left_arm>0 and tadasan[1]-left_arm<50:
    if abs(tadasan[1]-left_arm)<=10:    
    #  and tadasan[1]-left_arm<5 and tadasan[0]-right_leg<5 and tadasan[0]-left_leg<5:
        print("Your left arm is accurate")
        # t1 = gtts.gTTS("Your left arm is accurate") 
        # t1.save("left_arm.mp3")    
        # playsound("left_arm.mp3")    
    else:
        print("Your left arm is not accurate , try again")
        # t1 = gtts.gTTS("Your left arm is not accurate , try again") 
        # t1.save("left_arm_no.mp3")    
        # playsound("left_arm_no.mp3")  
    
    return acc
    
    
def compare_right_leg(right_leg):
    tadasan=[y for x, y in list(dataList[0].items()) if type(y) == int]
        # vrksana=[y for x, y in list(dataList[1].items()) if type(y) == int]
        # balasana=[y for x, y in list(dataList[2].items()) if type(y) == int]
        # trikonasana=[y for x, y in list(dataList[3].items()) if type(y) == int]
        # virabhadrasana=[y for x, y in list(dataList[4].items()) if type(y) == int]
        # adhomukha=[y for x, y in list(dataList[5].items()) if type(y) == int]

    if(right_leg<=tadasan[2]):
        acc=(right_leg/tadasan[2])*100
    else:
        acc=0

    if abs(tadasan[2]-right_leg)<=10:
    #  and tadasan[1]-left_arm<5 and tadasan[0]-right_leg<5 and tadasan[0]-left_leg<5:
        
        print("Your right leg is accurate")
        # t1 = gtts.gTTS("Your right leg is accurate") 
        # t1.save("right_leg.mp3")    
        # playsound("right_leg.mp3") 
                 
    else:
        print("Your right leg is not accurate, try again") 
        # t1 = gtts.gTTS("Your right leg is not accurate, try again") 
        # t1.save("right_leg_no.mp3")    
        # playsound("right_leg_no.mp3") 

    return acc
        
       
def compare_left_leg(left_leg):
    # for index in range(len(dataList)):
            # for key in dataList[index]:

    tadasan=[y for x, y in list(dataList[0].items()) if type(y) == int]
        # vrksana=[y for x, y in list(dataList[1].items()) if type(y) == int]
        # balasana=[y for x, y in list(dataList[2].items()) if type(y) == int]
        # trikonasana=[y for x, y in list(dataList[3].items()) if type(y) == int]
        # virabhadrasana=[y for x, y in list(dataList[4].items()) if type(y) == int]
        # adhomukha=[y for x, y in list(dataList[5].items()) if type(y) == int]
    if(left_leg<=tadasan[3]):
        acc=(left_leg/tadasan[3])*100
    else:
        acc=0


    if abs(tadasan[3]-left_leg and left_leg<tadasan[3] )<=10:
    #  and tadasan[1]-left_arm<5 and tadasan[0]-right_leg<5 and tadasan[0]-left_leg<5:
       print("Your left leg is accurate") 
        # t1 = gtts.gTTS("Your left leg is accurate") 
        # t1.save("left_leg.mp3")    
        # playsound("left_leg.mp3") 
    else:
        print("Your left leg is not accurate, try again") 
        # t1 = gtts.gTTS("Your left leg is not accurate, try again") 
        # t1.save("left_leg_no.mp3")    
        # playsound("left_leg_no.mp3") 
    
    return acc


arr = np.array([])
    
def generate_frames(arr):
    count=0
    timeout=20
    timeout_start=time.time()
    while time.time()<timeout_start+timeout:
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
        
        if len(lmlist)!=0:
            
            #right arm
            RightArmAngle=int(detector.findAngle(frame,12,14,16))
            accuracy=compare_right_arm(RightArmAngle)
            # print("acc: ", accuracy)
            if (count<=16 and accuracy!=0):
                arr=np.append(arr, accuracy)
                count=count+1

            #left arm
            angle=int(detector.findAngle(frame,11,13,15))
            accuracy=compare_left_arm(angle)
            # print(accuracy)
            if (count<=16 and accuracy!=0):
                arr=np.append(arr, accuracy)
                count=count+1
            
            
            #right leg
            angle=int(detector.findAngle(frame,24,26,28))
            accuracy=compare_right_leg(angle)
            if (count<=16 and accuracy!=0):
                arr=np.append(arr, accuracy)
                count=count+1
           
            
            
            
            #left leg
            angle=int(detector.findAngle(frame,23,25,27))
            accuracy=compare_left_leg(angle)
            if (count<=16 and accuracy!=0):
                arr=np.append(arr, accuracy)
                count=count+1
            elif(count>16):
                print("entring")
                print("accuracy: ", accuracyCaluclation(arr))

                
                
        cv2.waitKey(1)
        ret,buffer=cv2.imencode('.jpg',frame)
        frame=buffer.tobytes()

        yield(b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        print('Original Array:', arr)
        x=range(1, len(arr)+1)
        y=arr
        plt.plot(x,y)



def accuracyCaluclation (arr):
    accArray = np.array([])
    sum=0
    f=0
    # print('Original Array:', arr)
    for j in range (0, len(arr)-1, 4):
        for i in range(j,j+4):
            print("arr[i]",arr[i])
            sum=sum+arr[i]
        accur=sum/4
        accArray=np.append(accArray,accur/4)
    
    return accArray




@app.route("/")
def home():
     return render_template("home.html")

@app.route('/tracks')
def tracks():
    return render_template('tracks.html')

@app.route('/yoga')
def yoga():
    return render_template('yoga.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/charts' )
def charts():
    accArray=accuracyCaluclation(arr)
    values = [12, 19, 3, 5, 2, 3]
    labels = ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
    colors = ['#ff0000','#0000ff','#ffffe0','#008000','#800080','#FFA500', '#FF2554', ]
    return render_template('charts.html', values=accArray, labels=labels, colors=colors)

@app.route('/video')


def video():
    return Response(generate_frames(arr), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(host = "127.0.0.1",debug=True)