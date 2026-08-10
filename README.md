# Face Recognition Attendance System

A real-time face recognition-based attendance system developed using Python and computer vision techniques. The system uses a webcam to detect and recognize registered individuals and automatically records their attendance with the date and time.

## Project Overview

Manual attendance marking can be time-consuming and prone to errors. This project provides an automated attendance solution by recognizing faces through a webcam and recording the attendance of recognized individuals in a CSV file.

## Features

- Real-time face detection using a webcam
- Face recognition of registered individuals
- Automatic attendance marking
- Records date and time of attendance
- Stores attendance records in CSV format
- Displays the recognized person's name on the video feed
- Detects unknown/unregistered faces

## Technologies Used

- Python
- OpenCV
- face_recognition
- NumPy
- CSV
- DateTime

## Project Files

- `main.py` – Main Python program for face detection, recognition, and attendance marking
- `README.md` – Project documentation
- `LICENSE` – Project license
- `2024-06-25.csv` – Attendance record
- `dheeraj.jpg` – Registered face image
- `rohith.jpg` – Registered face image
- `goutham.jpg` – Registered face image
- `jeevan.jpg` – Registered face image

## How It Works

1. The system loads the registered users' photographs.
2. Face encodings are generated from the registered photographs.
3. The webcam captures the live video feed.
4. Faces detected in the video are compared with the registered face encodings.
5. When a registered person is recognized, their name is displayed.
6. The attendance is recorded with the date and time in a CSV file.

## Team Members

- **Dheeraj Rohith J**
- **Goutham N**
- **Jeevan Prasad S**

## Project Type

Academic Project

## Domain

Artificial Intelligence / Computer Vision

## Key Outcome

Developed an automated attendance system using real-time face recognition, reducing the need for manual attendance marking and maintaining timestamp-based attendance records.

## Future Enhancements

- Develop a graphical user interface
- Add database integration
- Create an attendance dashboard
- Improve recognition accuracy under different lighting conditions
- Deploy the system as a web-based application
