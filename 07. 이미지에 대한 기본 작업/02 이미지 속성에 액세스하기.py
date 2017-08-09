import cv2

image_file = 'ball_image.jpg'
img = cv2.imread(image_file)

print("shape:" + str(img.shape))
print("size:" + str(img.size))
print("dtype:" + str(img.dtype))
