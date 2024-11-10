import json
import os
import pickle

import numpy as np

__locations  = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
        
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    
    artifacts_path = os.path.join(os.path.dirname(__file__), 'artifacts', 'columns.json')
    
    with open(artifacts_path, 'r') as f:    
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    
    global __model
        
    model_path = os.path.join(os.path.dirname(__file__), 'artifacts', 'banglore_home_prices_model.pickle')
        
    with open(model_path, 'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")
    
def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location