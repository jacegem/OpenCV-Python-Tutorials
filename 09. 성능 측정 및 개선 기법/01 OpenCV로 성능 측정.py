import cv2

img1 = cv2.imread('model.jpg')

e1 = cv2.getTickCount()
for i in range(5, 49, 2):
    img2 = cv2.medianBlur(img1, i)
e2 = cv2.getTickCount()
t = (e2 - e1) / cv2.getTickFrequency()

cv2.imshow('Original', img1)
cv2.imshow('Blur', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(t)


# 결과: 2.5564403101561437