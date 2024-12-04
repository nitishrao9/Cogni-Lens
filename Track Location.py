import random
import time
import requests
from geopy.distance import geodesic
from intel_extension_for_pytorch import optimize  # For potential ML extensions

# Class to handle geolocation and safe zone checks
class SmartwatchLocation:
    def __init__(self, api_url="https://nominatim.openstreetmap.org/search", safe_zone_coords=(40.7128, -74.0060)):
        self.latitude = safe_zone_coords[0]  # Starting latitude (e.g., NYC)
        self.longitude = safe_zone_coords[1]  # Starting longitude (e.g., NYC)
        self.api_url = api_url
        self.safe_zone_coords = safe_zone_coords  # Define safe zone center
        self.safe_radius = 500  # Safe zone radius in meters

    def get_location(self):
        # Simulate random movement
        self.latitude += random.uniform(-0.01, 0.01)
        self.longitude += random.uniform(-0.01, 0.01)
        return self.latitude, self.longitude

    def fetch_coordinates(self, location_name):
        # Optional: Fetch coordinates for dynamic location setup
        params = {"q": location_name, "format": "json"}
        response = requests.get(self.api_url, params=params)
        if response.status_code == 200:
            data = response.json()
            if data:
                lat = float(data[0]["lat"])
                lon = float(data[0]["lon"])
                return lat, lon
        return None

    def is_out_of_bounds(self, current_coords):
        # Check if the current location is outside the safe zone
        distance = geodesic(self.safe_zone_coords, current_coords).meters
        return distance > self.safe_radius

# Main function to simulate smartwatch tracking
def track_patient_location():
    smartwatch = SmartwatchLocation()

    print("Tracking patient location...\n")
    while True:
        current_location = smartwatch.get_location()

        # Boundary check
        if smartwatch.is_out_of_bounds(current_location):
            print(f"ALERT: Patient is out of the safe zone! Coordinates: {current_location}")
        else:
            print(f"Current Location: Latitude = {current_location[0]}, Longitude = {current_location[1]}. Inside safe zone.")

        # Simulate delay (e.g., update every 5 seconds)
        time.sleep(5)

# Optimizing geolocation processing with Intel Toolkit
@optimize
def optimized_tracking():
    track_patient_location()

# Start tracking
optimized_tracking()
