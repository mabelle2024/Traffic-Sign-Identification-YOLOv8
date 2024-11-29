from ultralytics import YOLO

# Load the trained model
model = YOLO('/content/runs/detect/train/weights/best.pt')  # Update with correct path
# Predict on a specific test image
results = model.predict(source='/content/TrafficSignProject/TrafficSignProject/images/Test/00000.png', save=True)
# Access the first result in the results list
results[0].show()  # This displays the predicted image in Colab
