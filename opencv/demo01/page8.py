import cv2
import numpy as np


# convolution

def img_edges():
    img = cv2.imread('images/set1/messi5.jpg')
    img_edge = cv2.Canny(img, 255, 255)

    cv2.imshow('img', img)
    cv2.imshow('img_edges', img_edge)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def video_edges():
    capture = cv2.VideoCapture(0)
    while capture.isOpened():
        ret, frame = capture.read()

        img_edge = cv2.Canny(frame, 255, 255)
        cv2.imshow('camera_blurred', img_edge)
        cv2.imshow('camera', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
    capture.release()


# img_edges()
video_edges()
