import cv2
import numpy as np

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

img = cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, (255, 0, 0), -1)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
