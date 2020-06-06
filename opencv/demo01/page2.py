import cv2
import numpy as np


capture = cv2.VideoCapture(0)
# capture = cv2.VideoCapture('http://192.168.0.101:4747/video')
# capture = cv2.VideoCapture('https://youtu.be/MCD5xGPsnHg')


index =0
while capture.isOpened():
    ret, frame = capture.read()
    frame_grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('camera_grey', frame_grey)
    cv2.imshow('camera', frame)

    # cv2.imwrite(f'temp_images/color/index_{index}.jpg', frame)
    # cv2.imwrite(f'temp_images/greyscale/index_{index}.jpg', frame_grey)
    index+=1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# cv2.waitKey(0)
cv2.destroyAllWindows()
capture.release()