import cv2
import numpy as np


def video_fun1():
    capture = cv2.VideoCapture(0)
    classfier = cv2.CascadeClassifier('haarcascades/haarcascade_frontalcatface.xml')
    while capture.isOpened():
        ret, frame = capture.read()
        frame_grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        eyes = classfier.detectMultiScale(frame_grey)

        for (x, y, w, h) in eyes:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 4)

        cv2.imshow('camera', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
    capture.release()


video_fun1()

# further learning : torch/keras/scikit
