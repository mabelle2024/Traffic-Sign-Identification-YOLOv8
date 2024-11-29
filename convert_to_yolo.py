import pandas as pd
import os


train_csv = r'C:/Users/M/Desktop/TrafficSignProject/Train.csv'  #replace with your path to train.csv
test_csv = r'C:/Users/M/Desktop/TrafficSignProject/Test.csv'    #replace with your path to test.csv
images_train_folder = r'C:/Users/M/Desktop/TrafficSignProject/images/train' #replace with you path to train images
images_test_folder = r'C:/Users/M/Desktop/TrafficSignProject/images/test' #replace with your path to tet images
labels_train_folder = r'C:/Users/M/Desktop/TrafficSignProject/labels/train' #replace with your path to train labels
labels_test_folder = r'C:/Users/M/Desktop/TrafficSignProject/labels/test' #replace with your path to test labels


os.makedirs(labels_train_folder, exist_ok=True)
os.makedirs(labels_test_folder, exist_ok=True)


def convert_to_yolo(row, image_width, image_height):
    x1, y1, x2, y2 = row['Roi.X1'], row['Roi.Y1'], row['Roi.X2'], row['Roi.Y2']
    x_center = (x1 + x2) / 2 / image_width
    y_center = (y1 + y2) / 2 / image_height
    box_width = (x2 - x1) / image_width
    box_height = (y2 - y1) / image_height
    return f"{row['ClassId']} {x_center} {y_center} {box_width} {box_height}\n"

# Process a DataFrame and save annotations
def process_annotations(csv_file, images_folder, labels_folder):
    df = pd.read_csv(csv_file)
    for _, row in df.iterrows():
        
        image_name = row['Path'].split('/')[-1] 
        label_file_path = os.path.join(labels_folder, image_name.replace('.png', '.txt'))

        image_width = row['Width']
        image_height = row['Height']

        annotation = convert_to_yolo(row, image_width, image_height)

       
        with open(label_file_path, 'w') as f:
            f.write(annotation)
        print(f"Processed {image_name} -> {label_file_path}")


process_annotations(train_csv, images_train_folder, labels_train_folder)
process_annotations(test_csv, images_test_folder, labels_test_folder)

print("Annotation conversion complete!")

