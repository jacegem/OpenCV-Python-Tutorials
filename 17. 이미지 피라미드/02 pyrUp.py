import cv2

img = cv2.imread('small.jpg')
titles = ['orginal', 'level1', 'level2', 'level3']

images = []
images.append(img)

for i in range(3):
    img = cv2.pyrUp(img)
    images.append(img)

for i in range(4):
    cv2.imshow(titles[i], images[i])

cv2.waitKey(0)
cv2.destroyAllWindows()

