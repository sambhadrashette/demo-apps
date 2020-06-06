import cv2
import numpy as np


# convolution

def img_blurr():
    img = cv2.imread('images/set1/messi5.jpg')
    face = img[60:150, 190:280].copy()
    # create kernel
    kernel = np.ones((10, 10), dtype=np.float32) / 100
    blurred = cv2.filter2D(face, -1, kernel)
    img[60:150, 190:280] = blurred
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def img_blurr2():
    img = cv2.imread('images/set1/messi5.jpg')
    blurred = cv2.GaussianBlur(img, (9, 9), 0)
    cv2.imshow('img', img)
    cv2.imshow('blurred', blurred)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def img_sharpen():
    img = cv2.imread('images/set1/messi5.jpg')
    kernel = np.array([
        [-1, -1, -1],
        [-1, 9, -1],
        [-1, -1, -1]
    ])

    sharpened = cv2.filter2D(img, -1, kernel)
    cv2.imshow('img', img)
    cv2.imshow('shapen', sharpened)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# img_blurr()
# img_blurr2()

img_sharpen()
