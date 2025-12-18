import cv2
from ultralytics import YOLO
model = YOLO('yolov8n.pt')
img=cv2.imread('ALL/img/3.jpg')


#用yolol'o模型进行识别
results = model(img)

result=results[0]

#遍历检测框
for box in result.boxes:
    x1, y1, x2, y2 = map(int, box.xyxy[0])  # 坐标
    conf = float(box.conf[0])              # 置信度
    cls = int(box.cls[0])                  # 类别ID
    label = model.names[cls]               # 类别名字

    # 画框
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # 写文字
    cv2.putText(img, f"{label} {conf:.2f}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7, (0, 0, 255), 2)

# 显示结果
cv2.imshow("YOLO Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()