# Traffic-Sign-Identification-YOLOv8
Traffic Sign Detection and Identification | using YOLOv8 and GTSRB
**Project Results and Overview**
This project is aimed at making a fast and accurate system to identify traffic signs which can aid in driving autonomous vehicles. 
Although I used yolov8n.pt the model is very accurate.


**Source code**

TrafficSignProject:
1) data.yaml: Configuration file for the dataset.
2) train_yolo.py: Script to train the YOLOv8 model.
3) convert_to_yolo.py: Script to preprocess and convert labels to YOLO format.
4) results/: Contains visualizations of predictions and performance metrics.
5) requirements.txt: Lists Python dependencies for the project.
   
**Performance Metrics**

![image](https://github.com/user-attachments/assets/63da220e-e539-4cfd-9e6a-3dfc280d92b2)

   
**Visualization of results**

Loss curve:
![image](https://github.com/user-attachments/assets/06d96ae1-f4e8-4eb8-97e5-231ecc7b9eec)
mAP curve:
![image](https://github.com/user-attachments/assets/03631435-3498-4db3-afeb-ae23b029ad1e)

**Installation and Use**

Step 1: Clone the repository
Step 2: Install the dependencies (found in the requirements.txt)
Step 3: Download the GTSRB dataset
Step 4: preprocess it by running convert_to_yolo.py
Step 5: Train the model by using the train_yolo.py
Step 6: Test the model with sample images from the test part of the dataset
predicted results will be stored in the runs/detect directory

**References and Documents**

1) https://arxiv.org/pdf/1506.02640 : You Only Look Once: Unified, Real-Time Object Detection by Joseph Redmon, Santosh Divvala, Ross Girshick, Ali Farhadi
2) https://docs.ultralytics.com/ : Ultralytics official documentation for step to step implementation
3) GTSRB dataset : https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign
   
**Issues and Contributions**

I had issues making sure the labels matched the images, you will find a spare csv file in your test images (if you downlaod dataset from the given link). I had to remove that before hand. 

Also there was the issue of the train images being in seperate 43 subfolders so i needed to join them into a new folder, flattening the unneccesary folder structure.

Since there are only 43 classes for the signs the identification is limited to that.

Under various conditions, like blurriness or bad lighting the performance of this model could reduce.

(To contribute, submit bug report or enhancements through issues tab)

**Future Work**

Improve the model by training it on a more diverse dataset (images under more environmental conditions).

Create more comprehensive classes.






**Final notes**
meaning of each class:
1) class0: speed limit 21
2) class1: speed limit 30
3) class2: speed limit 50
4) class3: speed limit 60
5) class4: speed limit 70
6) class5: speed limit 80
7) class6: end of speed limit 80
8) class7: speed limit 100
9) class8: speed limit 120
10) class9: no passing/overtake
11) class10: no passing/overtaking for vehicles over 3.5 tonnes
12) class11: priority (you have right of way at next intersection)
13) class12: priority road
14) class13: yield
15) class14: stop
16) class15: road closed
17) class16: vehicles over 3.5 tonnes prohibited
18) class17: Do not enter
19) class18: general danger
20) class19: curve left
21) class20: curve right
22) class21: double curve
23) class22: uneven road surface
24) class23: slipper when wet or dirty
25) class24: road narrows
26) class25: roadworks
27) class26: taffric signals ahead
28) class27; pedestrian crossing
29) class28: watch for children 
30) class29: bicycle crossing
31) class30: ice/snow
32) class31: wild animal crossing
33) class32: end of all restrictions
34) class33: turn right ahead
35) class34: turn left ahead
36) class35: ahead only
37) class36: ahead or turn right only
38) class37: ahead or turn left only
39) class38: pass by on right
40) class39: pass by on left
41) class40: roundabout
42) class41: end of no passing zone
43) class42: end of no passing zone for trucks



