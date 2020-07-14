import numpy as np

from sklearn.externals import joblib 

# make sure you have downloaded the periodic_pattern_model_1.pkl file and is present in the current directory 

classifier = joblib.load('periodic_pattern_model_2.pkl')

test = np.array([1,2,4,7,4,2,1,2,4,7,4,2,1,2,4,7,4,2,1,2]).reshape(1,-1) # Add 20 values to the array and execute

IsItPattern = classifier.predict(test) > 0.5 # Remove > 0.5 if you want to know how good the pattern is

print(IsItPattern)