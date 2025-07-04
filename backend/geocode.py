import requests
import os

def get_coordinates(address):
    api_key = os.getenv("GEOCODING_API_KEY")
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"
    response = requests.get(url).json()
    location = response["results"][0]["geometry"]["location"]
    return location["lat"], location["lng"]