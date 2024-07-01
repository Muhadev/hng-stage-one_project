import requests
import os

def get_weather(city):
    api_key = os.getenv('WEATHER_API_KEY')
    base_url = "http://api.weatherapi.com/v1/current.json"
    response = requests.get(base_url, params={'key': api_key, 'q': city})
    
    if response.status_code == 200:
        data = response.json()
        return data['current']['temp_c']
    return "N/A"
