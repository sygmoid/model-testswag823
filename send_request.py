import json
import requests
import numpy as np
import pandas as pd
from sklearn import datasets


"""Setting the headers to send and accept json responses
"""
header = {'Content-Type': 'application/json', \
                  'Accept': 'application/json'}

"""Reading test batch
"""
col_imp = ["grade", "lat", "long", "sqft_living", "waterfront", "yr_built"]

dict_values = {"grade":10.0,"lat":47.5396,"long":-122.073,"sqft_living":4490.0,"waterfront":0.0,"yr_built":2006.0}

'''
x = np.array([float(dict_values[col]) for col in col_imp])
x = x.reshape(1,-1)
df = pd.DataFrame(x)

data = df.to_json(orient='records')
print(data)
print(type(data))
'''
#print(dict_values)

resp = requests.post("http://localhost:3002/predict", \
                    data = json.dumps(dict_values),\
                    headers= header)


#resp = requests.post("http://alpha.thinkingstack.com/predict", \
#                    data = json.dumps(data),\
#                    headers= header)

#resp = requests.post("http://getsygmoid-realestate-price-prediction.thinkingstack.com/predict", \
#                    data = json.dumps(data),\
#                    headers= header)

#print(json.dumps(data))
#print(resp.status_code)

print(resp.json())
