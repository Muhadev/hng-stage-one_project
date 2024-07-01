from flask import Blueprint, request, jsonify
from .weather import get_weather
from .location import get_location

main = Blueprint('main', __name__)

@main.route('/api/hello', methods=['GET'])
def hello():
    visitor_name = request.args.get('visitor_name', 'Guest')
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    
    location = get_location(client_ip)
    city = location['city']  # Ensure 'city' is correctly retrieved from the location
    
    temperature = get_weather(city)  # Assuming get_weather function works correctly
    
    greeting = f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {city}"
    
    response = {
        "client_ip": client_ip,
        "greeting": greeting,
        "location": city
    }
    
    return jsonify(response)
