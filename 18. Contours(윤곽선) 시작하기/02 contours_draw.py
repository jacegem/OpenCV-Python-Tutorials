import numpy as np
import cv2

im = cv2.imread('model.jpg')
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

img_all = cv2.drawContours(imgray, contours, -1, (0, 255, 0), 3)
img_4 = cv2.drawContours(imgray, contours, 3, (0, 255, 0), 3)

cnt = contours[4]
img_cnt = cv2.drawContours(imgray, [cnt], 0, (0, 255, 0), 3)

cv2.imshow('img_all', img_all)
cv2.imshow('img_4', img_4)
cv2.imshow('img_cnt', img_cnt)
cv2.waitKey(0)
cv2.destroyAllWindows()
