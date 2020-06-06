import cv2 as cv
import numpy as np


def draw_lines():
    img = np.zeros((400, 400, 3), dtype=np.uint8)
    cv.line(img, (20, 20), (150, 20), (0, 0, 255), cv.LINE_4)
    cv.line(img, (20, 50), (150, 50), (0, 255, 0), cv.LINE_8)
    cv.line(img, (20, 80), (150, 80), (255, 0, 0), cv.LINE_AA)

    cv.imshow('canvas', img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def draw_arrows():
    img = np.zeros((400, 400, 3), dtype=np.uint8)
    # draw arraows
    cv.arrowedLine(img, (20, 20), (150, 20), (0, 0, 255), cv.LINE_4)
    cv.arrowedLine(img, (20, 50), (150, 50), (0, 255, 0), cv.LINE_8)
    cv.arrowedLine(img, (20, 80), (150, 80), (255, 0, 0), cv.LINE_AA)

    cv.imshow('canvas', img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def draw_rect():
    img = np.zeros((400, 400, 3), dtype=np.uint8)
    # draw arraows
    cv.rectangle(img, (20, 20), (150, 150), (0, 0, 255), cv.LINE_4)
    cv.rectangle(img, (160, 160), (250, 250), (0, 255, 255), -1)

    cv.imshow('canvas', img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def draw_circles():
    img = np.zeros((400, 400, 3), dtype=np.uint8)
    # draw arraows
    cv.circle(img, (100, 100), 50, (0, 0, 255), cv.LINE_4)
    cv.circle(img, (180, 180), 50, (0, 255, 255), -1)

    cv.imshow('canvas', img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def draw_texts():
    img = np.zeros((400, 400, 3), dtype=np.uint8)
    # draw arraows
    cv.putText(img, 'Welcome to OpenCV', (20, 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv.LINE_4)
    cv.putText(img, 'Welcome to OpenCV', (20, 80), cv.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 2, cv.LINE_4)
    cv.putText(img, 'Welcome to OpenCV', (20, 120), cv.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 2, cv.LINE_4)
    cv.putText(img, 'Welcome to OpenCV', (20, 180), cv.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (0, 255, 255), 2, cv.LINE_4)

    cv.imshow('canvas', img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def highlight_face():
    img = cv.imread(f'images/set1/messi5.jpg')
    cv.rectangle(img, (190, 60), (280, 150), (0, 0, 255), cv.LINE_4)

    cv.imshow('messi', img)
    cv.waitKey(0)
    cv.destroyAllWindows()


# draw_lines()
# draw_arrows()
# draw_rect()
highlight_face()
# draw_circles()
# draw_texts()
