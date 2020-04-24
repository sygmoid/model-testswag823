import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
import dill as pickle

# ## Data Loading
data = pd.read_csv("data.csv")

labels = data['price']
conv_dates = [1 if values == 2014 else 0 for values in data.date ]
data['date'] = conv_dates
train1 = data.drop(['id', 'price'],axis=1)

x_train, x_test, y_train, y_test = train_test_split(train1, labels, test_size=0.10, random_state=2)

#clf = GradientBoostingRegressor(n_estimators=400, max_depth=5, min_samples_split=2,
#          learning_rate=0.1, loss='ls')

#clf.fit(x_train, y_train)

col_imp = ["grade", "lat", "long", "sqft_living", "waterfront", "yr_built"]

clf = GradientBoostingRegressor(n_estimators = 400, max_depth = 5, min_samples_split = 2)
clf.fit(train1[col_imp], labels)

filename = 'model.pk'
with open(filename, 'wb') as file:
  pickle.dump(clf, file)