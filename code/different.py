import cv2
import numpy as np
import def_resize

image_correct,image_incorrect = def_resize.resize()

gray_correct   = cv2.cvtColor(image_correct, cv2.COLOR_BGR2GRAY)
gray_incorrect = cv2.cvtColor(image_incorrect, cv2.COLOR_BGR2GRAY)

difference = cv2.absdiff(gray_correct , gray_incorrect)

_, thresh = cv2.threshold(difference, 10, 255, cv2.THRESH_BINARY)


contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
     if cv2.contourArea(contour) > 100:
         (x, y, w, h) = cv2.boundingRect(contour)
         cv2.rectangle(image_incorrect, (x, y), (x + w, y + h), (0, 0, 255), 1)

cv2.imshow("Differences", image_incorrect)

cv2.waitKey(0)
cv2.destroyAllWindows()
