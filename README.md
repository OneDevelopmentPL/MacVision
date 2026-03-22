# MacVision
What is MacVision? MacVision is a python project made for object detection with pre-trained YOLO models.
This repo also includes face changing system using YOLO-face. It detects faces, changes them with face image.

## Quick Start (for MacVision)
1. Clone this repo

```bash
git clone https://github.com/OneDevelopmentPL/MacVision.git
cd MacVision
```
2. Create a virtual env.

```bash
python3 -m venv .venv
source .venv/bin/activate
```
3. Install pip packages

```bash
pip3 install -r requirements.txt
```

4. Run
```bash
python3 macvision.py
```
To quit press `q`.

## Quick Start (for face changing system)
```bash
git clone https://github.com/OneDevelopmentPL/MacVision.git
cd MacVision/facechanging
```
2. Create a virtual env.

```bash
python3 -m venv .venv
source .venv/bin/activate
```
3. Install pip packages
```bash
pip3 install -r requirements_face.txt
```
4. Download -face models (some are in Release tab, but if model disappoints, you can download different model [here](https://huggingface.co/deepghs/yolo-face/tree/main))
5. Place the model in the `facechanging` folder.
6. Place the face image in the `facechanging`.
7. Edit `facechanging.py` file and fill the settings:
Example:
```python
[...]

MODEL_PATH = "yolov8n-face.pt"
REPLACEMENT_IMG = "face.png"

USE_DEFAULT_SIZE = False
DRAW_BOX = True
TEXT_LABEL = "Face"

[...]
```
8. Run the file
```bash
python3 facechanging.pt
```

Quit pressing `q` button.

## YOLO V8 Models

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
