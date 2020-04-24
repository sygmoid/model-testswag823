import os
import numpy as np
import pandas as pd
from sklearn.externals import joblib
from joblib import dump, load
from flask import Flask, jsonify, request
import dill as pickle

app = Flask(__name__)


@app.route('/healthz', methods=['GET'])
def healthz():
    message = {"status": "The Real-Estate Prediction API is healthy and available."}
    response = jsonify(message)
    response.status_code = 200
    return response

@app.route('/predict', methods=['POST'])
def apicall():
    """API Call

    Pandas dataframe (sent as a payload) from API Call
    """
    
    try:       
        #data_json = request.get_json()
        #print(data_json)
        #data = pd.read_json(data_json, orient='records')

        #print("++++++++++++++++++++++++++testing+++++++++++++++++++++++++++++")
        dict_values = request.get_json()
        col_imp = ["grade", "lat", "long", "sqft_living", "waterfront", "yr_built"]
        x = np.array([float(dict_values[col]) for col in col_imp])
        x = x.reshape(1,-1)
        data = pd.DataFrame(x)

        #data = pd.read_json(data_json)
        print(data)
    
    except Exception as e:
        raise e

    if data.empty:
        return(bad_request())
    else:
        #Load the saved model
        print("Loading the model...")
        clf = None
        filename = 'model.pk'
        with open(filename,'rb') as f:
            clf = pickle.load(f)

        print("The model has been loaded...doing predictions now...")
        predictions = clf.predict(data)
        predictions = round(predictions[0])
        price_pred = {'Predicted Price':predictions} 
        responses = jsonify(price_pred)    
        responses.status_code = 200
        return (responses)
    

@app.errorhandler(400)
def bad_request(error=None):
	message = {
			'status': 400,
			'message': 'Bad Request: ' + request.url + '--> Please check your data payload...',
	}
	resp = jsonify(message)
	resp.status_code = 400

	return resp

app.run(host='0.0.0.0', port=3002, debug=True)