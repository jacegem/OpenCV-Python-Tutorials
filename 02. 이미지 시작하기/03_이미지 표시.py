import cv2

# 컬러 이미지를 로드 합니다.
file = '01_model.jpg'
img = cv2.imread(file, cv2.IMREAD_COLOR)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
