import cv2
from matplotlib import pyplot as plt

file = '01_model.jpg'
img = cv2.imread(file, 0)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
