""" #5 to 128
import random
for i in range(100):
    x = abs(2*random.random())
    k = round(abs(6*random.random()))
    X=[]
    for j in range(3):
        for i in range(6):
            X.append(round(((abs(k-i))**(2-x)),2))
    X.append(X[0])
    X.append(X[1])
    
    y = 1# Add flag
    entry = X
    entry.append(y)
    # First 20 columns are points and 21st column is flag
    import csv
    with open('dataset.csv','a',newline='') as file:
        wr = csv.writer(file,dialect='excel')
        wr.writerow(entry)
"""
""" 129 to 328
import random
import numpy as np
for i in range(100):
    x = abs(10*random.random())
    m = abs(6*random.random())
    k = abs(10*random.random())
    X=[]
    for i in range(6):        
        X.append(round(x*(np.cos((3.14/3)*(i+m))) + k , 2 ))
    for j in range(2):
        for i in range(6):          
            X.append(X[i])
    X.append(X[0])
    X.append(X[1])
    
    y = 1# Add flag
    entry = X
    entry.append(y)
    # First 20 columns are points and 21st column is flag
    import csv
    with open('dataset.csv','a',newline='') as file:
        wr = csv.writer(file,dialect='excel')
        wr.writerow(entry)   
    """