# Predict on all test images
model.predict(
    source='/content/TrafficSignProject/images/Test',  # Path to test your images folder
    save=True,  
    save_txt=True  
)
