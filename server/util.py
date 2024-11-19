import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None


def get_estimated_price(location, sqft, bhk, bath):
    try:
        print(f"Inputs to model: Location: {location}, Sqft: {sqft}, BHK: {bhk}, Bath: {bath}")

        loc_index = __data_columns.index(location.lower()) if location.lower() in __data_columns else -1
        x = np.zeros(len(__data_columns))
        x[0] = sqft
        x[1] = bath
        x[2] = bhk
        if loc_index >= 0:
            x[loc_index] = 1

        price = round(__model.predict([x])[0], 2)
        print(f"Predicted price: {price}")
        return price

    except Exception as e:
        print(f"Error in get_estimated_price: {e}")
        return None


def load_saved_artifacts():
    print("Loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model

    with open('artifacts/columns.json', "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # First 3 columns are sqft, bath, bhk

    with open('artifacts/banglore_home_prices_model.pickle', 'rb') as f:
        __model = pickle.load(f)

    print("Loading saved artifacts...done")


def get_location_names():
    return __locations


def get_data_columns():
    return __data_columns


if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
