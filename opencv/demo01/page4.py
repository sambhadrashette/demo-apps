import cv2 as cv
import numpy as np


def img_split():
    img = cv.imread('images/set1/messi5.jpg')

    # split the image

    (b, g, r) = cv.split(img)

    img_merged = cv.merge([b, g, r])
    img_b = cv.merge([b + 100, g, r])
    img_g = cv.merge([b, g + 100, r])
    img_r = cv.merge([b, g, r + 100])

    cv.imshow('canvas', img)
    cv.imshow('canvas_merged', img_merged)
    cv.imshow('canvas_b', img_b)
    cv.imshow('canvas_g', img_g)
    cv.imshow('canvas_r', img_r)
    # cv.imshow('blue', b)
    # cv.imshow('green', g)
    # cv.imshow('red', r)
    cv.waitKey(0)
    cv.destroyAllWindows()


def img_crop():
    img = cv.imread('images/set1/messi5.jpg')

    # split the image
    cropped = img[50:150, 200:270]

    cv.imshow('canvas', cropped)
    cv.waitKey(0)
    cv.destroyAllWindows()


def img_resize(width, height):
    img = cv.imread('images/set1/messi5.jpg')

    # split the image
    (h, w, ch) = img.shape
    scaled_img = cv.resize(img, (w * width, h * height))

    cv.imshow(f'canvas_scaled_{height}', scaled_img)
    cv.imshow('canvas', img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def img_rotate():
    img = cv.imread('images/set1/messi5.jpg')

    # split the image
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    t = cv.getRotationMatrix2D(center, 45, 1)

    img_rotated = cv.warpAffine(img, t, (w, h))
    cv.imshow('canvas', img)
    cv.imshow('canvas_rotated', img_rotated)
    cv.waitKey(0)
    cv.destroyAllWindows()


def img_translate():
    img = cv.imread('images/set1/messi5.jpg')

    # split the image
    (h, w, r) = img.shape
    # center = (w // 2, h // 2)
    t = np.float32([[1, 0, 100], [0, 1, 100]])

    img_rotated = cv.warpAffine(img, t, (w, h))
    cv.imshow('canvas', img)
    cv.imshow('canvas_rotated', img_rotated)
    cv.waitKey(0)
    cv.destroyAllWindows()


# img_crop()
# img_resize(2, 2)
# img_rotate()

img_translate()