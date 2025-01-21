from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Ask Deepu!"})

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city', 'London')
    api_key = "YOUR_API_KEY"  # Get from OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url).json()
    if response.get('cod') != 200:
        return jsonify({"error": "City not found"})
    weather = {
        "city": response['name'],
        "temperature": round(response['main']['temp'] - 273.15, 2),
        "description": response['weather'][0]['description']
    }
    return jsonify(weather)

if __name__ == '__main__':
    app.run(debug=True)
