import time
import numpy as np
from openvino.runtime import Core
from geopy.distance import geodesic
from smartwatch_location import SmartwatchLocation  # Smartwatch location tracking class

# Define the safe zone in India (New Delhi coordinates)
safe_zone_center = (28.6139, 77.2090)  # New Delhi coordinates
safe_zone_radius = 0.001  # Approximate radius of 100 meters (in degrees)

# AI Location Monitoring Class
class LocationAI:
    def __init__(self):
        self.ie = Core()
        # Load the pre-trained AI model for location checking (you need to have a valid model file)
        self.model = self.ie.read_model("models/location-check-model.xml")
        self.compiled_model = self.ie.compile_model(model=self.model, device_name="CPU")

    def is_within_safe_zone(self, latitude, longitude):
        # Calculate the distance using geodesic (better accuracy for real-world distances)
        distance = geodesic(safe_zone_center, (latitude, longitude)).meters
        return distance < safe_zone_radius

    def process_location(self, latitude, longitude):
        if not self.is_within_safe_zone(latitude, longitude):
            print("ALERT! Patient has left the safe zone!")
            # Code to alert family members or hospital (e.g., via SMS, email, or push notifications)
        else:
            print("Patient is within the safe zone.")
            # Optionally, send confirmation or keep monitoring

# Main system for tracking and AI-based location monitoring
def location_monitoring_system():
    ai_assistant = LocationAI()  # Instantiate AI location assistant
    smartwatch = SmartwatchLocation()  # Instantiate the smartwatch location tracking class

    while True:
        latitude, longitude = smartwatch.get_location()  # Get the current location from smartwatch
        print(f"Current Location: Latitude = {latitude}, Longitude = {longitude}")
        
        ai_assistant.process_location(latitude, longitude)  # Process the location with AI

        # Optional: Implement additional checks or logging if needed
        time.sleep(5)  # Update every 5 seconds

# Run the location monitoring system
location_monitoring_system()
