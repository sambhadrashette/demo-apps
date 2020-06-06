import cv2
import numpy as np


# Blending images
def img_blend():
    img1 = cv2.imread('images/set1/messi5.jpg')
    img2 = cv2.imread('images/set1/opencv-logo-white.png')
    # get width and height from img1
    (h, w, ch) = img1.shape

    img2 = cv2.resize(img2, (w, h))
    # img_blended = cv2.add(img1, img2);
    img_blended = cv2.addWeighted(img1, 0.8, img2, 0.2, 0.5)
    cv2.imshow('img1', img1)
    cv2.imshow('img2', img2)
    cv2.imshow('img_blended', img_blended)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def video_blend():
    capture = cv2.VideoCapture(0)
    while capture.isOpened():
        ret, frame = capture.read()
        img2 = cv2.imread('images/set1/opencv-logo-white.png')
        # get width and height from img1
        (h, w, ch) = frame.shape

        img2 = cv2.resize(img2, (w, h))
        img_blended = cv2.addWeighted(frame, 0.8, img2, 0.2, 0.5)

        cv2.imshow('img_blended', img_blended)
        cv2.imshow('camera', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
    capture.release()


# video_blend()
img_blend()