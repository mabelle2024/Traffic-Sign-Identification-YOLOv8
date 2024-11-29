# Predict on all test images
model.predict(
    source='/content/TrafficSignProject/TrafficSignProject/images/Test',  # Path to test images folder
    save=True,  # Save predictions
    save_txt=True  # Save predictions as text files
)
