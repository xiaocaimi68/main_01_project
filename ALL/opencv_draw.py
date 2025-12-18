import cv2

img=cv2.imread('ALL/img/3.jpg')

#这一步就是以后你画 检测框、目标结果 的基础

#画矩形框架
cv2.rectangle(img,(50,50),(300,300),(0,255,0),2)

#加文字
cv2.putText(img,'object',(50,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

cv2.imshow('box',img)
cv2.waitKey(0)
cv2.destroyAllWindows()