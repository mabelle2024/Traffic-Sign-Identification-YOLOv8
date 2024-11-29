from ultralytics import YOLO

# Load the trained model
model = YOLO('/content/runs/detect/train/weights/best.pt')  #replace with your correct path
# Predict on a specific test image
results = model.predict(source='/content/TrafficSignProject/TrafficSignProject/images/Test/00000.png', save=True) #replace with path of any test image
# Access the first result in the results list
results[0].show()  
