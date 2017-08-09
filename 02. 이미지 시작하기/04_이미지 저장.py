import cv2

# 컬러 이미지를 로드 합니다.
file = '01_model.jpg'
img = cv2.imread(file, cv2.IMREAD_COLOR)

cv2.imwrite('04_image_write_output.png', img)
