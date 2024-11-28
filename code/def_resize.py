import cv2

def resize(): 
    image1 = cv2.imread("1_1.jpg")
    image2 = cv2.imread("1_2.jpg")
    
    print(image1.shape)
    height, width = image1.shape[:2]
    
    image2 = cv2.resize(image2, (width, height))
    return image1, image2


