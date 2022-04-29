from unittest import result
import tensorflow as tf
import tensorflow_hub as hub
import cv2
from matplotlib import pyplot as plt
import numpy as np

#optional for GPU

# gpus=tf.config.experimental.list_physical_devices('GPU')
# for gpu in gpus:
#     tf.config.experimental.set_memory_growth(gpu,True)

#loding the model

model=hub.load("https://tfhub.dev/google/movenet/multipose/lightning/1")
movenet=model.signatures['serving_default']

#starting the webcam

cap = cv2.VideoCapture(0)

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
    

while (True):
    ret, frame = cap.read()

    #resize the image
    img=frame.copy()
    img =tf.image.resize_with_pad(tf.expand_dims(img, axis=0), 256,256)
    input_img=tf.cast(img, dtype=tf.int32)

    # detecting the image

    results=movenet(input_img)
    print(results)

    
    cv2.imshow('Frame', frame)

    
    if cv2.waitKey(20) & 0xff==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()