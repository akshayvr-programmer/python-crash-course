  
import cv2

car_algorithm = cv2.CascadeClassifier('cars.xml')
pedestrian_algorithm = cv2.CascadeClassifier('pedestrian_algo.xml')
car = cv2.VideoCapture('video.mp4')
key = cv2.waitKey(2000)
while True:

    successful_frame_read, frame = car.read()
    gray_Scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    car_coordinates = car_algorithm.detectMultiScale(gray_Scale)
    pedestrian_coordinates = pedestrian_algorithm.detectMultiScale(gray_Scale)

    for(x, y, w, h) in car_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0 , 0 ,256), 1)
        cv2.imshow('car', frame)
        cv2.waitKey(5)
        for(x, y, w, h) in pedestrian_coordinates:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.imshow('car', frame)
            cv2.waitKey(1)
        if key==81 or key==74:
            break
