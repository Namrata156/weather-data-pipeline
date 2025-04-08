import requests
import os
from dotenv import load_dotenv

# Load the .env file and get the API key
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

API_KEY = os.getenv("OWM_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q":city,
        "appid": API_KEY,
        "units": "metric" # For temperature in Celsius
    }

    try:
        response = requests.get(BASE_URL, params= params)
        response.raise_for_status() # Raise an error for bad status codes
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {city}: {e}")
        return None
    
def get_multiple_cities_weather(cities):
    weather_data = []

    for city in cities:
        data = get_weather(city)
        if data:
            weather_data.append(data)

    return weather_data

