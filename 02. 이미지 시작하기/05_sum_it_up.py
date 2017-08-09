import cv2

# Load an color image in grayscale
file = '01_model.jpg'
img = cv2.imread(file, 0)

cv2.imshow('image', img)
k = cv2.waitKey(0)
if k == 27:  # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):  # wait for 's' key to save and exit
    cv2.imwrite('05_sum_it_up_output.png', img)
    cv2.destroyAllWindows()
