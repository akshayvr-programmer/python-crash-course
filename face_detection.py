

import cv2
from random import randrange
face_detection_algo = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
webcam = cv2.VideoCapture(0)
cv2.waitKey(2000)

while True:
    succesful_img_read, frame = webcam.read()
    grayscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_coordinates = face_detection_algo.detectMultiScale(grayscale_img)

    for(x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y),(x+w, y+h), (randrange(256), randrange(256), randrange(256)), 2)

        cv2.imshow('Face', frame)
        cv2.waitKey(1)
