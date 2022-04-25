import tensorflow as tf
import tensorflow_hub as hub
import cv2
from matplotlib import pyplot as plt
import numpy as np

# gpus=tf.config.experimental.list_physical_devices('GPU')
# for gpu in gpus:
#     tf.config.experimental.set_memory_growth(gpu,True)

#loding the model

model=hub.load('https://tfhub.dev/google/movenet/multipose/lightning/1')
movenet=model.signatures['serving_default']

#starting the webcam

cap=cv2.VideoCapture(2)
while cap.isOpened():
    ret, frame=cap.read()

    cv2.imshow('Yoga pose by user',frame)

    #for exiting the webcam

    if cv2.waitKey(10) & 0xFF==ord('q'):
        break;
cap.release()
cv2.destroyAllWindows()