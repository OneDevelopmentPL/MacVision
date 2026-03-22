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
6. Place the face image in the `facechanging` folder.
7. Edit `facechanging.py` file and fill the settings.
<br>Example:
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
python3 facechanging.py
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

## Tested models by me:
*Tested on Mac mini M4 16GB RAM*
<br>yolov8n -> very fast (30-50FPS)
<br>yolov8s -> not tested
<br>yolov8m -> mid (15-20FPS)
<br>yolov8l -> bad (5-10FPS)

## How to convert `.PT` to `.MLPACKAGE`?
What is `.mlpackage`?
<br>`.mlpackage` is a modern model container format introduced by Apple, designed to replace the older `.mlmodel` for use with the Core ML framework. It is specifically optimized for Apple Silicon (M1, M2, M3, M4) and serves as the primary bridge to unlock the full power of the Neural Engine (ANE).

1. Download packages via pip
```bash
pip install ultralytics coremltools
```
2. Type this command into a terminal (make sure it is MacVision root directory)
```bash
python3 pt2ml.py --file youtyolofile.pt
```
3. Change in `macvision.py`:
```python
model = YOLO("file.mlpackage")
```
READY TO USE!

## HAVE FUN USING THIS PROJECT!

## Project is licensed under MIT LICENSE
More [here](LICENSE)!

## Authors
OneDevelopment
