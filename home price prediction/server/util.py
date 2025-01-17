import json
import pickle
import numpy as np
__location=None
__data_columns=None
__model=None
def get_estimated_prices(location,sqft,bhk,bath):
    try:
        loc_index=__data_columns.index(location.lower())
    except:
        loc_index=-1

    p=np.zeros(len(__data_columns))
    p[0]=sqft
    p[1]=bath
    p[2]=bhk
    if loc_index>=0:
        p[loc_index]=1
    return round(__model.predict([p])[0],2)
  

def get_location_names():
    return __location
def load_saved_artifacts():
    print("loading saved artifacts...")
    global __data_columns
    global __location
    global __model

    with open("server/artifacts/columns.json",'r')as f:
        __data_columns= json.load(f)['data_columns']
        __location=__data_columns[3:]
    with open("server/artifacts/Bengaluru_House_Data.pickle",'rb') as f:
        __model=pickle.load(f)
    print("artifacts loading is done")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_prices('1st phase jp nagar','1000','2','2'))
    print(get_estimated_prices('1st phase jp nagar','1000','3','2'))
    print(get_estimated_prices('1st phase jp nagar','1000','2','3'))


