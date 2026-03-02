from ultralytics import YOLO

def evaluate_models():
    # Paths to your specific 'best' weights from the terminal runs
    model_paths = {
        "YOLOv8n": "runs/detect/yolov8n3/weights/best.pt",
        "YOLOv8s": "runs/detect/yolov8s/weights/best.pt",
        "YOLOv8m": "runs/detect/yolov8m2/weights/best.pt"
    }
    
    print(f"{'Model':<10} | {'mAP50':<8} | {'mAP50-95':<10} | {'Precision':<10} | {'Recall':<8}")
    print("-" * 55)

    for name, path in model_paths.items():
        try:
            model = YOLO(path)
            # Validate on the validation set defined in data.yaml
            results = model.val(data="data/rps/data.yaml", imgsz=416, plots=False)
            
            # Extract metrics
            map50 = results.box.map50
            map95 = results.box.map
            prec = results.box.mp
            recall = results.box.mr
            
            print(f"{name:<10} | {map50:<8.3f} | {map95:<10.3f} | {prec:<10.3f} | {recall:<8.3f}")
        except Exception as e:
            print(f"Could not evaluate {name}: {e}")

if __name__ == "__main__":
    evaluate_models()