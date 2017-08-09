import cv2

image_file = 'ball_image.jpg'
img = cv2.imread(image_file)

px = img[100, 100]
print(px)

blue = img[100, 100, 0]
print(blue)

img[100, 100] = [255, 255, 255]
print(img[100, 100])
