import cv2
from ultralytics import YOLO

# Download models in Releases tab on github.com/OneDevelopmentPL/MacVision/releases
model = YOLO("yolov8s.pt")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    r = results[0]

    for box in r.boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        cls = int(box.cls[0])          
        label = model.names[cls]        
        conf = box.conf[0]             

        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0,255,0), 2)

        text = f"{label} {conf:.2f}"
        cv2.putText(frame, text, (int(x1), int(y1)-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

    cv2.imshow("Detekcja", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
