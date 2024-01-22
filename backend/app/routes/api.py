# api.py

import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/current_weather/<city>', methods=['GET'])
def get_current_weather(city, api_key):
    '''Get current weather data for the specified city.'''
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},US&APPID={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        return jsonify(weather_data)
    else:
        return jsonify({'error': 'Unable to fetch weather data'}), 500

if __name__ == '__main__':
    app.run(debug=True)
