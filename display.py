import cv2
import numpy as np
import os
import time

class Display:
    def __init__(self, face_detector, database):
        self.face_detector = face_detector
        self.database = database

    def process_frame(self, frame):
        detections = self.face_detector.detect_faces(frame)
        h, w = frame.shape[:2]

        for detection in detections[0][0]:
            confidence = detection[2]
            if confidence > 0.5:  # Consider detections with confidence > 0.5
                xmin, ymin, xmax, ymax = map(
                    int, detection[3:7] * np.array([w, h, w, h])
                )
                face = frame[ymin:ymax, xmin:xmax]

                # Placeholder for real face embedding
                face_embedding = "Simulated Face Embedding"

                # Check database for face
                person_info = self.database.find_person_by_face(face_embedding)
                if person_info:
                    text = f"{person_info['name']}, {person_info['age']}, {person_info['relationship']}"
                else:
                    os.makedirs("unknown_faces", exist_ok=True)
                    image_path = f"unknown_faces/face_{int(time.time())}.jpg"
                    cv2.imwrite(image_path, face)
                    name = input("Enter Name: ")
                    age = int(input("Enter Age: "))
                    relationship = input("Enter Relationship: ")
                    self.database.add_person(name, age, relationship, image_path)
                    text = f"New: {name}, {age}, {relationship}"

                cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
                cv2.putText(frame, text, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        return frame
