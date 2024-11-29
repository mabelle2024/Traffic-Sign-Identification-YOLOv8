import os
import pandas as pd

# put paths to your dataset
train_csv = '/content/TrafficSignProject/Train.csv'  # replace this with the path to your training CSV
test_csv = '/content/TrafficSignProject/Test.csv'    # replace this with the path to your testing CSV
images_train_folder = '/content/TrafficSignProject/images/Train'  # replace with train image folder
images_test_folder = '/content/TrafficSignProject/images/Test'    # replace with test image folder
labels_train_folder = '/content/TrafficSignProject/labels/train'  
labels_test_folder = '/content/TrafficSignProject/labels/test'    


os.makedirs(labels_train_folder, exist_ok=True)
os.makedirs(labels_test_folder, exist_ok=True)

def convert_bbox_to_yolo_format(row, img_width, img_height):
  
    x1, y1, x2, y2 = row['Roi.X1'], row['Roi.Y1'], row['Roi.X2'], row['Roi.Y2']
    x_center = ((x1 + x2) / 2) / img_width
    y_center = ((y1 + y2) / 2) / img_height
    width = (x2 - x1) / img_width
    height = (y2 - y1) / img_height
    return x_center, y_center, width, height

def process_annotations(csv_file, images_folder, labels_folder):
    """
    Convert annotations from CSV to YOLO format.
    """
    df = pd.read_csv(csv_file)

    for _, row in df.iterrows():
        img_path = os.path.join(images_folder, row['Path'])
        if not os.path.exists(img_path):
            print(f"Image {img_path} not found. Skipping.")
            continue

        
        img_width, img_height = row['Width'], row['Height']
        
        
        bbox = convert_bbox_to_yolo_format(row, img_width, img_height)
        class_id = row['ClassId']
        
        
        label_file = os.path.join(labels_folder, os.path.splitext(row['Path'])[0] + '.txt')
        with open(label_file, 'a') as f:
            f.write(f"{class_id} " + " ".join([f"{x:.6f}" for x in bbox]) + "\n")


print("Processing training annotations...")
process_annotations(train_csv, images_train_folder, labels_train_folder)

print("Processing testing annotations...")
process_annotations(test_csv, images_test_folder, labels_test_folder)

print("Conversion to YOLO format complete!")

