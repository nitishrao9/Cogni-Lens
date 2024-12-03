from openvino.runtime import Core

class FaceDetector:
    def __init__(self, model_path="models/face-detection-0200.xml"):
        self.ie = Core()
        self.model = self.ie.read_model(model=model_path)
        self.compiled_model = self.ie.compile_model(model=self.model, device_name="CPU")
        self.input_layer = self.compiled_model.input(0)
        self.output_layer = self.compiled_model.output(0)

    def detect_faces(self, frame):
        # Preprocess frame (resize and convert to blob)
        resized_frame = cv2.resize(frame, (300, 300))
        input_blob = resized_frame.transpose(2, 0, 1)  # HWC to CHW
        input_blob = input_blob[np.newaxis, :]  # Add batch dimension

        # Perform inference
        results = self.compiled_model([input_blob])[self.output_layer]
        return results
