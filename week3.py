import cv2

#reading images from main folder
img = cv2.imread('orange.jpg')
cv2.imshow('Its an Orange', img)

cv2.waitKey(0)
