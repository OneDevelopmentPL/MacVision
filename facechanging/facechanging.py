import cv2
import numpy as np
from ultralytics import YOLO

# Download face models at https://huggingface.co/deepghs/yolo-face/tree/main
MODEL_PATH = "yolov8n-face.pt"
REPLACEMENT_IMG = "face.png"

USE_DEFAULT_SIZE = False
DRAW_BOX = True
TEXT_LABEL = "#MATA2040"

model = YOLO(MODEL_PATH)

src_face = cv2.imread(REPLACEMENT_IMG)
if src_face is None:
    src_face = cv2.imread("face.jpg")
assert src_face is not None, "Nie znaleziono face.png ani face.jpg"

cap = cv2.VideoCapture(0)
print("Uruchomiono face swapping. Naciśnij 'q' aby wyjść.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    for r in results:
        for box in r.boxes:
            coords = box.xyxy[0].cpu().numpy().astype(int)
            x1, y1, x2, y2 = coords

            if USE_DEFAULT_SIZE:
                w = src_face.shape[1]
                h = src_face.shape[0]
                nx1 = x1
                ny1 = y1
                nx2 = x1 + w
                ny2 = y1 + h
            else:
                w = x2 - x1
                h = y2 - y1
                nx1 = x1
                ny1 = y1
                nx2 = x2
                ny2 = y2

            nx2 = min(frame.shape[1], nx2)
            ny2 = min(frame.shape[0], ny2)

            face_resized = cv2.resize(src_face, (nx2 - nx1, ny2 - ny1))

            mask = 255 * np.ones(face_resized.shape, face_resized.dtype)

            center = ((nx1 + nx2) // 2, (ny1 + ny2) // 2)

            blended = cv2.seamlessClone(
                face_resized,
                frame,
                mask,
                center,
                cv2.NORMAL_CLONE
            )

            frame = blended

            if DRAW_BOX:
                cv2.rectangle(frame, (nx1, ny1), (nx2, ny2), (0, 255, 0), 2)

            cv2.putText(frame, TEXT_LABEL, (nx1, max(0, ny1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow("Face Swap", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()