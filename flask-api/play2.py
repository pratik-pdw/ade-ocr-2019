import cv2
import numpy as np

img = cv2.imread("./uploads/Form.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = np.ones((1, 10), np.uint8)
morphed = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
imgwtl = cv2.add(gray, (255-morphed))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = np.ones((40, 1), np.uint8)
morphed = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
imgwt2 = cv2.add(gray, (255-morphed))

result = cv2.add(imgwtl, imgwt2)


kernel = np.ones((2, 2), np.uint8) 
  
# The first parameter is the original image, 
# kernel is the matrix with which image is  
# convolved and third parameter is the number  
# of iterations, which will determine how much  
# you want to erode/dilate a given image.  
img_erosion = cv2.erode(result, kernel, iterations=1) 
img_dilation = cv2.dilate(result, kernel, iterations=1) 
  
# cv2.imshow('Input', result) 
# cv2.imshow('Erosion', img_erosion) 
# cv2.imshow('Dilation', img_dilation) 

th = cv2.adaptiveThreshold(img_erosion, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow('original',result)
cv2.imwrite('Original.jpg', result)
cv2.imshow('Adaptive threshold',th)
cv2.imwrite('Thresh.jpg', th)

cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.imshow("Result", cv2.add(result, img_erosion))


# cv2.waitKey(0) 

# # cv2.imshow('removed', result)
# # cv2.waitKey(0)
# cv2.destroyAllWindows()
