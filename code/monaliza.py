import cv2
import numpy as np

image = cv2.imread("monaliza.jpg")

# gray_1 = cv2.bilateralFilter(image,20, 50, 75)
gray_1 = cv2.fastNlMeansDenoising(image, None, 7, 10, 21)

cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Original Image', 400, 600)
cv2.imshow("Original Image", gray_1)

cv2.waitKey(0)
cv2.destroyAllWindows()
