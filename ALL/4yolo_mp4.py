import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    result = results[0]

    for box in result.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cls = int(box.cls[0])
        label = model.names[cls]
        conf = float(box.conf[0])

        cv2.rectangle(frame, (x1, y1),(x2, y2),(0,255,0),2)
        cv2.putText(frame, f"{label} {conf:.2f}",
                   (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)

    cv2.imshow("Video Detection", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
