import argparse
from ultralytics import YOLO

def main():
    parser = argparse.ArgumentParser(description="Convert YOLO .pt model to ML model (.mlpackage)")
    parser.add_argument("--file", type=str, required=True, help="PATH TO .pt FILE")
    
    args = parser.parse_args()

    try:
        model = YOLO(args.file)
        
        print(f"Starting conversion for: {args.file}...")
        
        model.export(format="coreml", nms=True)
        
        print("\nSuccess! The model has been saved in the same directory as the source file.")
    except Exception as e:
        print(f"Conversion error: {e}")

if __name__ == "__main__":
    main()
