import cv2
import numpy as np


# morphological transformation

def dilation():
    img = cv2.imread('images/set2/opencv_inv.png')

    kernel = np.ones((5, 5), np.uint8)
    img_dilated = cv2.dilate(img, kernel)
    cv2.imshow('img', img)
    cv2.imshow('img_dilated', img_dilated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def erosion():
    img = cv2.imread('images/set2/opencv.png')

    kernel = np.ones((5, 5), np.uint8)
    img_erode = cv2.erode(img, kernel)
    cv2.imshow('img', img)
    cv2.imshow('img_erode', img_erode)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# dilation()
erosion()
