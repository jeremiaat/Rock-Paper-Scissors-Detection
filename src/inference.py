import cv2
from ultralytics import YOLO

def run_live_demo():
    # Using Nano (yolov8n3) as it was the fastest and most accurate in your tests
    model = YOLO("runs/detect/yolov8n3/weights/best.pt")

    # Start webcam
    cap = cv2.VideoCapture(0)

    print("Press 'q' to quit the demo.")

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        # Run inference
        # stream=True is more efficient for real-time video
        results = model(frame, conf=0.5, stream=True)

        for r in results:
            annotated_frame = r.plot()
            cv2.imshow("Rock Paper Scissors - Live Detection", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_live_demo()