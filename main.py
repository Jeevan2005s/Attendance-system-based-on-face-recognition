import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

# start camera
video_capture = cv2.VideoCapture(0)

# Load faces
try:
    dheeraj_image = face_recognition.load_image_file(r"C:\STUFF\PROJECT\mini project\photos\dheeraj.jpg")
    dheeraj_encoding = face_recognition.face_encodings(dheeraj_image)[0]
    
    hari_image = face_recognition.load_image_file(r"C:\STUFF\PROJECT\mini project\photos\Hariharan.jpg")
    hari_encoding = face_recognition.face_encodings(hari_image)[0]

    hema_image = face_recognition.load_image_file(r"C:\STUFF\PROJECT\mini project\photos\hemananthan.jpg")
    hema_encoding = face_recognition.face_encodings(hema_image)[0]

    perumal_image = face_recognition.load_image_file(r"C:\STUFF\PROJECT\mini project\photos\perumal.jpg")
    perumal_encoding = face_recognition.face_encodings(perumal_image)[0]

    known_face_encodings = [dheeraj_encoding, hari_encoding, hema_encoding, perumal_encoding]
    known_face_names = ["dheeraj","Hari", "Hemananthan", "Ganesh"]
except Exception as e:
    print(f"Error loading images: {e}")
    exit()

# List of students
students = known_face_names.copy()

#  current date and time
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

# Open CSV file to store attendance
with open(f"{current_date}.csv", "w+", newline="") as f:
    lnwriter = csv.writer(f)

    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Error: Failed to grab frame.")
            break

        # Resize frame for faster processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Recognize faces
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for face_encoding, face_location in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distance)

            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                if name in students:
                    students.remove(name)
                    current_time = datetime.now().strftime("%H:%M:%S")
                    lnwriter.writerow([name, current_time])

                # Draw a box around the face and label it with the name
                top, right, bottom, left = [v * 4 for v in face_location]
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name + " present", (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
            else:
                # For unrecognized faces, label them as "Unknown"
                top, right, bottom, left = [v * 4 for v in face_location]
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, "Unknown", (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        cv2.imshow("Camera", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

# Release webcam and close windows
video_capture.release()
cv2.destroyAllWindows()
