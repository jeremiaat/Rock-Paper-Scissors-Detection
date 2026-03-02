**Rock Paper Scissors Detection: YOLOv8 Performance Analysis**

This repository contains a comparative study of YOLOv8 architectures (Nano, Small, and Medium) for detecting hand gestures in a "Rock, Paper, Scissors" game. This project was completed as part of the Final Workshop Assignment.

**Model Comparison**
| Model       |   mAP50   |  mAP50–95 | Precision |   Recall  | Speed (ms) |  Size (MB) |
| ----------- | :-------: | :-------: | :-------: | :-------: | :--------: | :--------: |
| **YOLOv8n** | **0.943** |   0.742   |   0.910   | **0.933** | **2.2 ms** | **6.2 MB** |
| YOLOv8s     |   0.940   | **0.743** | **0.931** |   0.893   |   4.0 ms   |   22.5 MB  |
| YOLOv8m     |   0.934   |   0.736   |   0.916   |   0.888   |   9.2 ms   |   52.0 MB  |

The models were trained for 10 epochs using a batch size of 16 and an image size of 416.

**Analysis & Discussion**
1. Accuracy vs. Model Complexity

Surprisingly, YOLOv8n (Nano) achieved the highest mAP50 (0.943).
While larger models (Medium) are generally more capable, they often require more than 10 epochs to converge. The Nano model's simplicity allowed it to reach peak performance very quickly on this specific dataset.

2. Speed and Real-time Suitability

The YOLOv8n model is the clear winner for real-time applications.
With an inference speed of 2.2 ms (over 450 FPS), it provides zero-lag detection, which is essential for interactive games.

3. Precision vs. Recall

YOLOv8s showed the highest Precision (0.931), meaning it had the fewest false positives (it rarely guessed a gesture incorrectly).

YOLOv8n showed the highest Recall (0.933), meaning it was the best at finding every hand gesture in the frame, even if they were slightly blurry.

4. Conclusion

For a hand-gesture detection task like Rock-Paper-Scissors, bigger is not always better. The Nano model provides the best accuracy-to-speed ratio, making it the most efficient choice for deployment on edge devices or standard webcams.

🛠️ Installation & Usage
1. Setup Environment

(Add setup steps here.)

2. Run Evaluation

To replicate the comparison table above:

yolo detect val model=yolov8n.pt data=data.yaml
yolo detect val model=yolov8s.pt data=data.yaml
yolo detect val model=yolov8m.pt data=data.yaml
3. Run Real-Time Inference (Part 6)

To launch the live webcam demo using the best Nano model:

yolo detect predict model=yolov8n.pt source=0

