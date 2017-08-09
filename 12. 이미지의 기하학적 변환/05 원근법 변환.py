import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sudoku.jpg')
rows, cols, ch = img.shape[:3]

# pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
pts1 = np.float32([[101, 131], [500, 114], [66, 504], [544, 489]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(img, M, (300, 300))

plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()
