import requests
import os

def get_location(ip):
    api_key = os.getenv('IPSTACK_API_KEY')
    base_url = "http://api.ipstack.com/"
    response = requests.get(f"{base_url}{ip}", params={'access_key': api_key})
    
    if response.status_code == 200:
        data = response.json()
        if 'city' in data:
            return {
                'city': data['city']
            }
        else:
            return {
                'city': 'Unknown'
            }
    return {
        'city': 'Unknown'
    }
