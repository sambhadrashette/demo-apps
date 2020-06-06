import cv2
import numpy as np


# Thresholding

def thresholding():
    img = cv2.imread('images/set1/sudoku.png')
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
    re, threshold_1 = cv2.threshold(img_grey, 50, 255, cv2.THRESH_BINARY)
    cv2.imshow('img', img)
    cv2.imshow('img_new', threshold_1)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def adaptive_thresholding():
    img = cv2.imread('images/set1/sudoku.png')
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    threshold_1 = cv2.adaptiveThreshold(img_grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 33, 2)
    # threshold_1 = cv2.adaptiveThreshold(img_grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    threshold_2 = cv2.adaptiveThreshold(img_grey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    cv2.imshow('img', img)
    cv2.imshow('ADAPTIVE_THRESH_MEAN_C', threshold_1)
    cv2.imshow('ADAPTIVE_THRESH_GAUSSIAN_C', threshold_2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# thresholding()
adaptive_thresholding()
