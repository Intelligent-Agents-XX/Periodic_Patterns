import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('dataset.csv')
X = np.array(data.iloc[:,:-1])
y = np.array(data.iloc[:,-1]).reshape(-1,1)


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2, random_state = 0)

from keras.models import Sequential
from keras.layers import Dense

classifier = Sequential()

classifier.add(Dense(output_dim = 80, init="uniform", activation = "relu",  input_dim = 20))

classifier.add(Dense(output_dim = 400, init="uniform", activation = "relu"))

classifier.add(Dense(output_dim = 1, init="uniform", activation = "sigmoid"))

classifier.compile(optimizer = "adam", loss = "binary_crossentropy", metrics = ['accuracy'])

classifier.fit(X_train,y_train, epochs = 50)

y_pred = classifier.predict(X_test)

y_pred = y_pred > 0.5

from sklearn.metrics import confusion_matrix, accuracy_score

cm = confusion_matrix(y_test,y_pred)

accuracy = accuracy_score(y_test,y_pred)

'''
from sklearn.externals import joblib 
  
# Save the model as a pickle in a file 
joblib.dump(classifier, 'periodic_pattern_model_x.pkl')
'''