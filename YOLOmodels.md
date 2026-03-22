# YOLO v8 models

| Model       | Size     | Speed     | Accuracy    |
|------------|---------|----------|------------|
| yolov8n.pt | Smallest | Very fast | Mid        |
| yolov8s.pt | Small    | Fast      | Better     |
| yolov8m.pt | Mid      | ok        | Good       |
| yolov8l.pt | Big      | Slower    | The best   |

## How to change the model?

In `macvision.py` change:
`model = YOLO("modelhere.pt")`
Selected model will download on app start.