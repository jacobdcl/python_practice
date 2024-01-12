import requests
import json

def find_attractions(latitude, longitude, radius, api_key):
    # Define the base URL for the Google Places API
    base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

    # Define the parameters for the search
    params = {
        "location": f"{latitude},{longitude}",
        "radius": radius,
        "type": "tourist_attraction",  # You may need to adjust the type or use the keyword parameter for more specific results
        "keyword": "waterfalls, rivers, trails, views, mountains, valleys, nature",
        "key": api_key
    }

    # Make a request to the Google Places API
    response = requests.get(base_url, params=params)
    results = response.json()

    # Parse the results and return a list of attractions
    attractions = []
    for place in results.get('results', []):
        name = place.get('name')
        location = place.get('geometry', {}).get('location')
        attractions.append({
            'name': name,
            'latitude': location.get('lat'),
            'longitude': location.get('lng')
        })

    return attractions

# Example usage
api_key = 'YOUR_API_KEY'  # Replace with your actual Google API key
latitude = 40.7128  # New York City's latitude, for example
longitude = -74.0060  # New York City's longitude, for example
radius = 10000  # Search within 10 kilometers

attractions = find_attractions(latitude, longitude, radius, api_key)
for attraction in attractions:
    print(json.dumps(attraction, indent=2))

