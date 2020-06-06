#import the openCV libmport
import cv2
import numpy as np

img = cv2.imread('images/set1/messi5.jpg')
print(type(img))
print(f'shape: {img.shape}')
(h,w, channel) = img.shape

cv2.imshow('messi', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


