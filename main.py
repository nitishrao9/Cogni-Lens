import cv2
import os
from display import Display
from face_detector import FaceDetector
from database import Database

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
    database = Database()
    face_detector = FaceDetector()
    display = Display(face_detector, database)
    camera = Camera()

    try:
        while True:
            frame = camera.read_frame()
            if frame is None:
                break
            processed_frame = display.process_frame(frame)
            cv2.imshow("Face Recognition", processed_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        camera.release()
        cv2.destroyAllWindows()
        database.close()

if __name__ == "__main__":
    main()
