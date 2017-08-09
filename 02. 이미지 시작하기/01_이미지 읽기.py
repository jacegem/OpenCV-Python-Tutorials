import cv2

# Load an color image in grayscale
file = '01_model.jpg'
img = cv2.imread(file, 0)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
