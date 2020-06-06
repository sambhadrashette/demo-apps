import cv2
import numpy as np


# bitwise operation

# Img inverted
def img_bitwise_not():
    img = cv2.imread('images/set1/messi5.jpg')
    img_not = cv2.bitwise_not(img)
    cv2.imshow('img', img)
    cv2.imshow('img_not', img_not)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img_bitwise_not()