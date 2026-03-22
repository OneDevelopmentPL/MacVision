import cv2
from ultralytics import YOLO

# ładujemy pretrenowany model YOLOv8
model = YOLO("yolov8s.pt")

# otwieramy kamerę (0 = domyślna)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # robimy predykcję
    results = model(frame)

    # wynik to lista z jednym elementem
    r = results[0]

    # r.boxes ma bounding boxy
    for box in r.boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        cls = int(box.cls[0])           # indeks klasy
        label = model.names[cls]        # np. 'person'
        conf = box.conf[0]              # pewność

        # rysuj prostokąt
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0,255,0), 2)

        # tekst z nazwą + confidence
        text = f"{label} {conf:.2f}"
        cv2.putText(frame, text, (int(x1), int(y1)-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

    # pokaż
    cv2.imshow("Detekcja", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()