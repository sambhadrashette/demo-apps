import cv2
import numpy as np


def fun1():
    img = cv2.imread('images/set1/wrong_perspective.png')

    source_pts = np.float32([[35, 254], [345, 150], [290, 740], [630, 525]])
    dest_pts = np.float32([[0, 0], [400, 0], [0, 581], [400, 581]])
    M = cv2.getPerspectiveTransform(source_pts, dest_pts)

    # apply non affine transformation
    mod_img = cv2.warpPerspective(img, M, (400, 581))

    cv2.imshow('img', img)
    cv2.imshow('img_mod', mod_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def fun2():
    img = cv2.imread('images/set2/scan.jpg')
    source_pts = np.float32([[320, 15], [700, 215], [85, 610], [530, 780]])
    dest_pts = np.float32([[0, 0], [420, 0], [0, 594], [420, 594]])
    M = cv2.getPerspectiveTransform(source_pts, dest_pts)

    # apply non affine transformation
    mod_img = cv2.warpPerspective(img, M, (400, 581))

    cv2.imshow('img', img)
    cv2.imshow('img_mod', mod_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# fun1()
fun2()
