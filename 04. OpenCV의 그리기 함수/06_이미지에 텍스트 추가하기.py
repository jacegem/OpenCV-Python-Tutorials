import cv2
import numpy as np

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Hello OpenCV!!!', (10, 500), font, 2, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
