import numpy as np

from sklearn.externals import joblib 

# make sure you have downloaded the periodic_pattern_model_1.pkl file and is present in the current directory 

classifier = joblib.load('periodic_pattern_model_2.pkl')
 # Add 20 values to the array and execute

import pandas as pd

data_test = pd.read_csv('data_test.csv')

data_test = np.array(data_test)

X_test = data_test[:,0:20]
y_test = data_test[:,20:21]

y_pred = classifier.predict(X_test)

y_pred = y_pred > 0.5 # Remove > 0.5 if you want to know how good the pattern is

from sklearn.metrics import confusion_matrix, accuracy_score

cm = confusion_matrix(y_test,y_pred)
acc = accuracy_score(y_test,y_pred)