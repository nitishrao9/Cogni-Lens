import random
import time

# Simulate the GPS coordinates of a smartwatch
class SmartwatchLocation:
    def __init__(self):
        self.latitude = 40.7128  # Example latitude (New York City)
        self.longitude = -74.0060  # Example longitude (New York City)
    
    def get_location(self):
        # Simulating movement by changing the coordinates
        self.latitude += random.uniform(-0.01, 0.01)
        self.longitude += random.uniform(-0.01, 0.01)
        
        return (self.latitude, self.longitude)

# Simulate reading location data
def track_patient_location():
    smartwatch = SmartwatchLocation()

    while True:
        current_location = smartwatch.get_location()
        print(f"Current Location: Latitude = {current_location[0]}, Longitude = {current_location[1]}")
        
        # Simulate delay (e.g., update every 5 seconds)
        time.sleep(5)

# Start tracking
track_patient_location()
