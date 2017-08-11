import cv2

img = cv2.imread('large.jpg')
titles = ['orginal', 'level1', 'level2', 'level3']

images = []
images.append(img)

for i in range(3):
    img = cv2.pyrDown(img)
    images.append(img)

for i in range(3):
    resize = cv2.resize(images[i]
                        , dsize=(images[i+1].shape[1], images[i+1].shape[0])
                        , interpolation=cv2.INTER_CUBIC)
    images[i] = cv2.subtract(resize, images[i+1])
    cv2.imshow(titles[i], images[i])

cv2.waitKey(0)
cv2.destroyAllWindows()

