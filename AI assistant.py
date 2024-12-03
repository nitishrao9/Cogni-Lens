from openvino.runtime import Core
import numpy as np

# Define the safe zone (e.g., a 100-meter radius around a central point)
safe_zone_center = (40.7128, -74.0060)  # New York City coordinates
safe_zone_radius = 0.001  # Example radius in degrees (approx. 100 meters)

class LocationAI:
    def __init__(self):
        self.ie = Core()
        # Load a pre-trained model (for AI inference)
        self.model = self.ie.read_model("models/location-check-model.xml")  # Use the correct model path
        self.compiled_model = self.ie.compile_model(model=self.model, device_name="CPU")

    def is_within_safe_zone(self, latitude, longitude):
        # Check if the patient is within the safe zone using Euclidean distance in degrees
        distance = np.sqrt((latitude - safe_zone_center[0])**2 + (longitude - safe_zone_center[1])**2)
        return distance < safe_zone_radius

    def process_location(self, latitude, longitude):
        # Use AI (in a real-world scenario, this could involve complex models for tracking)
        if not self.is_within_safe_zone(latitude, longitude):
            print("Alert! Patient has left the safe zone!")
        else:
            print("Patient is within the safe zone.")

# Using the AI assistant to track location and check if within the safe zone
def location_monitoring_system():
    ai_assistant = LocationAI()
    
    smartwatch = SmartwatchLocation()

    while True:
        latitude, longitude = smartwatch.get_location()
        ai_assistant.process_location(latitude, longitude)
        time.sleep(5)

location_monitoring_system()
