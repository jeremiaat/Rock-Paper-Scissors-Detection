from ultralytics import YOLO

def main():
    models = ["yolov8n.pt", "yolov8s.pt", "yolov8m.pt"]

    for model_name in models:
        model = YOLO(model_name)
        model.train(
            data="data/rps/data.yaml",
            epochs=10,
            imgsz=416,
            batch=16,
            device=0,
            name=model_name.replace(".pt", ""),
            workers=4  # Added to prevent CPU bottleneck, you can adjust this
        )

if __name__ == '__main__':
    main()