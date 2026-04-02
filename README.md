# Road Surface Damage Detection using YOLOv8 and OpenCV

## Project Overview

This project detects road surface damage regions from input road images using Computer Vision techniques based on YOLOv8 and OpenCV.

The system identifies damaged regions on roads and highlights them using bounding boxes.

This project was developed as part of the Computer Vision BYOP Course Project.

---

## Technologies Used

Python

OpenCV

YOLOv8 (Ultralytics)

NumPy

---

## Features

Detects road damage candidate regions

Draws bounding boxes on detected areas

Displays total number of detected damage regions

Works on any road surface image

Command-line execution supported

---

## Project Structure

detect.py → Main detection script

road.jpg → Sample test image

requirements.txt → Dependencies list

README.md → Documentation

---

## How to Run the Project

Step 1:

Install dependencies

pip install -r requirements.txt


Step 2:

Run detection

python detect.py --image road.jpg


---

## Sample Output

Bounding boxes appear around detected road surface damage candidate regions.

Console output displays:

Road Damage Regions detected: XX

---

## Limitations

The pretrained YOLOv8 model is used for general object detection.

Since pothole-specific datasets are limited, detected bounding boxes represent candidate road damage regions.

---

## Future Improvements

Train custom pothole detection dataset

Improve detection accuracy

Deploy real-time webcam detection

Integrate with smart transportation systems

---

## Author

Rahul Tiwari

Computer Vision BYOP Project

VIT Bhopal