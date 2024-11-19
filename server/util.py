import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    try:
        print(f"Inputs: location={location}, sqft={sqft}, bhk={bhk}, bath={bath}")

        if __data_columns is None or __model is None:
            raise Exception("Artifacts not loaded. Call load_saved_artifacts() first.")

        loc_index = __data_columns.index(location.lower()) if location.lower() in __data_columns else -1
        print(f"Location index in data_columns: {loc_index}")

        x = np.zeros(len(__data_columns))
        x[0] = sqft
        x[1] = bath
        x[2] = bhk
        if loc_index >= 0:
            x[loc_index] = 1

        print(f"Feature vector: {x}")

        price = round(__model.predict([x])[0], 2)
        return price
    except Exception as e:
        print(f"Error in get_estimated_price: {e}")
        raise e

def load_saved_artifacts():
    print("Loading saved artifacts...")
    global __data_columns
    global __locations
    global __model

    try:
        with open('artifacts/columns.json', "r") as f:
            __data_columns = json.load(f)['data_columns']
            __locations = __data_columns[3:]  # First 3 columns are sqft, bath, bhk
        print(f"Loaded data_columns: {__data_columns}")

        with open('artifacts/banglore_home_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
        print("Model loaded successfully.")

    except Exception as e:
        print(f"Error loading artifacts: {e}")
        raise e

def get_location_names():
    if __locations is None:
        raise Exception("Artifacts not loaded. Call load_saved_artifacts() first.")
    return __locations

def get_data_columns():
    if __data_columns is None:
        raise Exception("Artifacts not loaded. Call load_saved_artifacts() first.")
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2))  # other location
    print(get_estimated_price('Ejipura', 1000, 2, 2))   # other location
