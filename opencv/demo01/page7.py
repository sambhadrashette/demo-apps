import cv2
import numpy as np


# Video Blurr and sharpen

capture = cv2.VideoCapture(0)

index =0
while capture.isOpened():
    ret, frame = capture.read()

    # frame_blurr= cv2.GaussianBlur(frame, (9, 9), 0)
    kernel = np.array([
        [-1, -1, -1],
        [-1, 9, -1],
        [-1, -1, -1]
    ])

    frame_blurr = cv2.filter2D(frame, -1, kernel)
    cv2.imshow('camera_blurred', frame_blurr)
    cv2.imshow('camera', frame)
    index+=1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# cv2.waitKey(0)
cv2.destroyAllWindows()
capture.release()