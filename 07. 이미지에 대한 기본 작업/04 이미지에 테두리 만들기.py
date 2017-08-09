import cv2
from matplotlib import pyplot as plt

BLUE = [255, 0, 0]

image_file = 'opencv-logo-white.png'
img1 = cv2.imread(image_file)

pixel = 100

replicate = cv2.copyMakeBorder(img1, pixel, pixel, pixel, pixel, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1, pixel, pixel, pixel, pixel, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1, pixel, pixel, pixel, pixel, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1, pixel, pixel, pixel, pixel, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img1, pixel, pixel, pixel, pixel, cv2.BORDER_CONSTANT, value=BLUE)

plt.subplot(231), plt.imshow(img1, 'gray'), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')

plt.show()
