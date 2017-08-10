import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('model.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

size = 50
kernel = np.ones((size, size), np.float32) / (size * size)
dst = cv2.filter2D(img, -1, kernel)

cv2.imwrite('model_output.png', cv2.cvtColor(dst, cv2.COLOR_RGB2BGR))

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst), plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()
