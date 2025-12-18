import cv2
import numpy as np

img = cv2.imread('ALL/img/3.jpg')
cv2.imshow('行人',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#转灰度
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#高斯模糊
img_blur = cv2.GaussianBlur(img_gray,(5,5),0)

#边缘检测
img_edge = cv2.Canny(img_blur,100,200)

#缩放
resized=cv2.resize(img_edge,(500,500))

cv2.imshow('边缘检测',resized)
cv2.imshow("blur",img_blur)
cv2.imshow("img_edge",img_edge)
cv2.imshow("img_gray",img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()

