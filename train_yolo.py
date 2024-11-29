from ultralytics import YOLO


model = YOLO('yolov8n.pt')  # Use yolov8n (Nano) for minimal resource usage

# Training the model
model.train(
    data='/content/TrafficSignProject/TrafficSignProject/data.yaml',  # put your path to the data.yaml
    epochs=10,         # Number of epochs (adjust as needed)
    imgsz=416,         # Image size (lower for faster training)
    batch=8,           # Batch size (lower for reduced GPU usage)
    device=0           # Use GPU (0), or 'cpu' if GPU is unavailable
)
