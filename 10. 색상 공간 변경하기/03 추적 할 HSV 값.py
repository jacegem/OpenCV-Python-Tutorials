import cv2
import numpy as np

green = np.uint8([[[0, 255, 0]]])
hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
print(hsv_green)

# 출력 : [[[ 60 255 255]]]