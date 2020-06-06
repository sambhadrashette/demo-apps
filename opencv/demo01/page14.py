import cv2
import numpy as np


# Contours

def fun1():
    img = cv2.imread('images/set2/someshapes.jpg')

    contours, hierarchy = cv2.findContours(cv2.Canny(img, 255, 255), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print(contours)
    # draw contours
    for contour in contours:
        cv2.drawContours(img, [contour], -1, (0, 0, 255), 2)
    cv2.imshow('img', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def fun2():
    img = cv2.imread('images/set2/someshapes.jpg')

    contours, hierarchy = cv2.findContours(cv2.Canny(img, 255, 255), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print(contours)
    # draw contours
    index = 0
    for contour in contours:
        cv2.drawContours(img, [contour], -1, (0, 0, 255), 2)
        (x, y, w, h) = cv2.boundingRect(contour)
        # Draw the bounding rect
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Crop the contour
        img_contour = img[y: y + h, x: x + w]
        cv2.imshow(f'shape {index + 1}', img_contour)
        index += 1

    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def fun3():
    img = cv2.imread('images/set2/someshapes.jpg')

    contours, hierarchy = cv2.findContours(cv2.Canny(img, 255, 255), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # draw contours
    index = 0
    for contour in contours:
        # Approximation of shape
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        edges = len(approx)
        index += 1
        shape = ''
        if edges == 3:
            shape = 'Triangle'
        if edges == 4:
            shape = 'Rectangle'
        if edges == 10:
            shape = 'Star'
        if edges > 10:
            shape = 'Circle'

        print(f'edges {edges}, index = {index + 1}, shape = {shape}')

    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def fun4():
    img = cv2.imread('images/set2/someshapes.jpg')

    contours, hierarchy = cv2.findContours(cv2.Canny(img, 255, 255), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # draw contours
    index = 0
    for contour in contours:
        # Approximation of shape
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        edges = len(approx)
        # find the contour moment
        moment = cv2.moments(contour)
        # center of contour
        cx = int(moment['m10'] / moment['m00'])
        cy = int(moment['m01'] / moment['m00'])

        index += 1
        shape = ''
        if edges == 3:
            shape = 'Triangle'
        if edges == 4:
            shape = 'Rectangle'
        if edges == 10:
            shape = 'Star'
        if edges > 10:
            shape = 'Circle'

        # add the label
        cv2.putText(img, shape, (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
        print(f'edges {edges}, index = {index + 1}, shape = {shape}')
        # highlight the contour
        cv2.drawContours(img, [contour], -1, (0, 0, 255), 2)

    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# fun1()
# fun2()
# fun3()
fun4()
