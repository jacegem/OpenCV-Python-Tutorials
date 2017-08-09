import cv2
from matplotlib import pyplot as plt

img = cv2.imread('beach.jpg')

res1 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

height, width = img.shape[:2]
res2 = cv2.resize(img, (int(0.5 * width), int(0.5 * height)), interpolation=cv2.INTER_CUBIC)

plt.subplot(1, 2, 1), plt.imshow(cv2.cvtColor(res1, cv2.COLOR_BGR2RGB)), plt.title('res1')
plt.subplot(1, 2, 2), plt.imshow(cv2.cvtColor(res2, cv2.COLOR_BGR2RGB)), plt.title('res2')
plt.show()
