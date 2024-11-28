import cv2
import numpy as np

image1 = cv2.imread("chess.jpg")
gray_   = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray_1 = cv2.bilateralFilter(gray_, 9, 75, 75)
# gray_2 = cv2.fastNlMeansDenoising(gray_, None, 30, 7, 21)

_, thresh_white = cv2.threshold(gray_1,185, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh_white, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
white_counter=0
for contour in contours:
     if cv2.contourArea(contour) > 100:
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(image1, (x, y), (x + w+2, y + h+13), (0, 0, 255), 1)
        cropped_piece = image1[y:y + h, x:x + w]
        
        filename = f"Chess pieces/white_piece_{white_counter}.jpg"
        cv2.imwrite(filename, cropped_piece)
        print(f"Saved: {filename}")
        white_counter += 1

_, thresh_black = cv2.threshold(gray_1,10, 255, cv2.THRESH_BINARY_INV)  
contours_black, _ = cv2.findContours(thresh_black, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
black_counter=0
for contour in contours_black:
    if cv2.contourArea(contour) > 200: 
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(image1, (x, y), (x + w + 5, y + h ), (0, 0, 255), 1)
        
        cropped_piece = image1[y:y + h, x:x + w]
        filename = f"Chess pieces/black_piece_{black_counter}.jpg"
        cv2.imwrite(filename, cropped_piece)
        print(f"Saved: {filename}")
        black_counter += 1

filename = f"Chess pieces/chess_with_rectangle.jpg"
cv2.imwrite(filename, image1)

cv2.imshow("Differences", image1)
# cv2.imshow("Differences", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
