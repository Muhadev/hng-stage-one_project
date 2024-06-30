from flask import Blueprint, request, jsonify

bp = Blueprint('main', __name__)

@bp.route('/api/hello', methods=['GET'])
def hello():
    visitor_name = request.args.get('visitor_name', 'Visitor')
    client_ip = request.remote_addr

    # Mock response for location and temperature data
    location = "New York"
    temperature = 11

    greeting = f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {location}"
    response = {
        "client_ip": client_ip,
        "location": location,
        "greeting": greeting
    }
    return jsonify(response)
