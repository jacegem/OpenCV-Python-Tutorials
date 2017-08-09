import cv2

img = cv2.imread('rotate.jpg', 1)
rows, cols = img.shape[:2]

M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('Original', img)
cv2.imshow('warpAffine', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()