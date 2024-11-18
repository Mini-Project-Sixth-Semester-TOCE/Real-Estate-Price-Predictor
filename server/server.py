from flask import Flask, request, jsonify, send_from_directory
import util
from flask_cors import CORS 
import os

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    locations = util.get_location_names()
    print("Locations returned:", locations)  # Debugging
    response = jsonify({
        'locations': locations
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    data = request.get_json()
    total_sqft = float(data['total_sqft'])
    location = data['location']
    bhk = int(data['bhk'])
    bath = int(data['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/')
def index():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'app.html')

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(host='0.0.0.0', port=10000)
