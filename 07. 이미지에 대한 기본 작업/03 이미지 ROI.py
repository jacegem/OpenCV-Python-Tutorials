import cv2

image_file = 'ball_image.jpg'
img = cv2.imread(image_file)

ball = img[0:113, 349:459]
img[100:213, 449:559] = ball

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
