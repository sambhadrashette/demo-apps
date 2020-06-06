import cv2
import numpy as np


# Arithmatic operations >>>>>>>>>>>>>> Scalar
def scalar_op_add():
    img = cv2.imread('images/set1/messi5.jpg')
    M = np.ones(img.shape, dtype=np.uint8) * 50
    img_addition = cv2.add(img, M)
    cv2.imshow('img', img)
    cv2.imshow('img_addition', img_addition)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def scalar_op_subtract():
    img = cv2.imread('images/set1/messi5.jpg')
    M = np.ones(img.shape, dtype=np.uint8) * 50
    img_subtract = cv2.subtract(img, M)
    cv2.imshow('img', img)
    cv2.imshow('img_subtract', img_subtract)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# scalar_op_add()
scalar_op_subtract()