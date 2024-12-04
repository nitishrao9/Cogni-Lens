import cv2
import os
from display import Display
from face_detector import FaceDetector
from database import Database
from smartwatch_location import SmartwatchLocation  # Importing the updated location tracking module
from geopy.distance import geodesic  # For boundary check
import random
import time

# Camera class for video capture
class Camera:
    def __init__(self, source=0):
        self.capture = cv2.VideoCapture(source)

    def read_frame(self):
        ret, frame = self.capture.read()
        return frame if ret else None

    def release(self):
        self.capture.release()

def main():
    os.makedirs("unknown_faces", exist_ok=True)
    database = Database()  # Database connection
    face_detector = FaceDetector()  # Face detection instance
    display = Display(face_detector, database)  # Display instance to process frames
    camera = Camera()  # Camera instance

    # Integrating Smartwatch Location Tracking (updated with geolocation)
    smartwatch = SmartwatchLocation()  # Location tracking instance

    try:
        while True:
            frame = camera.read_frame()
            if frame is None:
                break

            # Get current location from smartwatch (simulated)
            current_location = smartwatch.get_location()
            print(f"Current Location: Latitude = {current_location[0]}, Longitude = {current_location[1]}")

            # Boundary check (out of safe zone)
            if smartwatch.is_out_of_bounds(current_location):
                print(f"ALERT: Patient is out of the safe zone! Coordinates: {current_location}")
            else:
                print(f"Patient is within the safe zone.")

            # Process the current frame for face detection
            processed_frame = display.process_frame(frame)

            # Show the processed frame with face recognition results
            cv2.imshow("Face Recognition", processed_frame)

            # Exit condition (press 'q' to quit)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            # Simulate a delay for tracking and processing
            time.sleep(1)
    finally:
        # Cleanup resources
        camera.release()
        cv2.destroyAllWindows()
        database.close()

if __name__ == "__main__":
    main()
