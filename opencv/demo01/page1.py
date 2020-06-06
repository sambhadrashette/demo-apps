import cv2
import numpy as np

img = cv2.imread('images/set1/messi5.jpg')

# convert image into greyscale
img_greyscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);

# save the img_greyscaled to disk
cv2.imwrite('/tmp/greyscaled_messi.jpg', img_greyscaled)


cv2.imshow('messi_greyscale', img_greyscaled)
cv2.imshow('messi', img)
cv2.waitKey(0)
cv2.destroyAllWindows()