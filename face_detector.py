import cv2
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from openvino.runtime import Core
import numpy as np
import os
from PIL import Image

class FaceRecognitionWithLFW:
    def __init__(self, model_path="intel/face-detection-adas-0001.xml", lfw_dir="path_to_lfw"):
        self.ie = Core()
        self.model = self.ie.read_model(model=model_path)
        self.compiled_model = self.ie.compile_model(self.model, "CPU")
        self.input_layer = next(iter(self.compiled_model.inputs))
        self.output_layer = next(iter(self.compiled_model.outputs))
        self.lfw_dir = lfw_dir

    def load_lfw_data(self):
        images, labels = [], []
        for person_dir in os.listdir(self.lfw_dir):
            person_path = os.path.join(self.lfw_dir, person_dir)
            for img_file in os.listdir(person_path):
                img_path = os.path.join(person_path, img_file)
                image = Image.open(img_path).convert("RGB")
                images.append(np.array(image))
                labels.append(person_dir)
        return np.array(images), np.array(labels)

    def preprocess_data(self, images, labels):
        images = np.array([cv2.resize(img, (128, 128)) for img in images])
        le = LabelEncoder()
        labels = le.fit_transform(labels)
        return train_test_split(images, labels, test_size=0.2, random_state=42)

    def detect_faces(self, frame):
        input_blob = cv2.resize(frame, (672, 384))
        input_blob = input_blob.transpose((2, 0, 1)).reshape(1, 3, 384, 672)
        results = self.compiled_model([input_blob])[self.output_layer]
        faces = []
        for detection in results[0][0]:
            confidence = detection[2]
            if confidence > 0.5:
                xmin, ymin, xmax, ymax = (detection[3:7] * [frame.shape[1], frame.shape[0],
                                                            frame.shape[1], frame.shape[0]]).astype(int)
                faces.append({"coords": (xmin, ymin, xmax, ymax), "confidence": confidence})
        return faces

# Usage
lfw_dir = "path_to_lfw_dataset"
recognizer = FaceRecognitionWithLFW(lfw_dir=lfw_dir)
images, labels = recognizer.load_lfw_data()
X_train, X_test, y_train, y_test = recognizer.preprocess_data(images, labels)
