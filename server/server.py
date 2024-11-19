from flask import Flask, request, jsonify, send_from_directory
import util
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'app.html')

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    try:
        locations = util.get_location_names()
        response = jsonify({'locations': locations})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        print(f"Error in /get_location_names: {e}")
        return jsonify({'error': 'Failed to fetch location names'}), 500

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        data = request.get_json()
        print(f"Data received: {data}")

        total_sqft = float(data['total_sqft'])
        location = data['location']
        bhk = int(data['bhk'])
        bath = int(data['bath'])

        print(f"Inputs: sqft={total_sqft}, location={location}, bhk={bhk}, bath={bath}")

        # Call the util function
        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
        print(f"Predicted price: {estimated_price}")

        response = jsonify({'estimated_price': estimated_price})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except KeyError as ke:
        print(f"KeyError: Missing field in data: {ke}")
        return jsonify({'error': f"Missing field: {str(ke)}"}), 400
    except ValueError as ve:
        print(f"ValueError: Invalid data type: {ve}")
        return jsonify({'error': f"Invalid input: {str(ve)}"}), 400
    except Exception as e:
        print(f"Exception: {e}")
        return jsonify({'error': 'Error occurred while predicting price'}), 500

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(host='0.0.0.0', port=10000)
