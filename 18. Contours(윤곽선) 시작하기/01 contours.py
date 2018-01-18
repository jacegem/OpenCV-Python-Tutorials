import numpy as np
import cv2

im = cv2.imread('test.jpg')
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow('imgray', imgray)
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
