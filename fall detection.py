import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense
from intel_extension_for_tensorflow import patch_tensorflow

patch_tensorflow()  # Optimize TensorFlow for Intel hardware

class FallDetectionWithHAR:
    def __init__(self, uci_dir="path_to_uci_har_dataset"):
        self.model = Sequential([
            LSTM(64, input_shape=(128, 3), return_sequences=True),
            LSTM(32),
            Dense(1, activation='sigmoid')
        ])
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        self.uci_dir = uci_dir

    def load_har_data(self):
        features = pd.read_csv(f"{self.uci_dir}/X_train.txt", delim_whitespace=True, header=None).values
        labels = pd.read_csv(f"{self.uci_dir}/y_train.txt", delim_whitespace=True, header=None).values
        return features.reshape(-1, 128, 3), labels

    def train_model(self, X_train, y_train):
        self.model.fit(X_train, y_train, epochs=10, batch_size=32)
        self.model.save("fall_detection_model.h5")

# Usage
uci_har_dir = "path_to_uci_har_dataset"
fall_detector = FallDetectionWithHAR(uci_dir=uci_har_dir)
X_train, y_train = fall_detector.load_har_data()
fall_detector.train_model(X_train, y_train)
