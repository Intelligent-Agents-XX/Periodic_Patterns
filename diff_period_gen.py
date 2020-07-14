''' first hundres values
import random
for i in range(100):
    p= random.randint(1,15) ## taking periodicity 1 to 15 in account
    x = abs(2*random.random())
    k = round(abs(p*random.random()))
    X=[]

    for j in range((20/p)):
        for i in range(p):
            X.append(round(((abs(k-i))**(2-x)),2))
    
    for j in range ((20%p)):
        X.append(X[j])


    y = 1# Add flag
    entry = X
    entry.append(y)
    # First 20 columns are points and 21st column is flag
    import csv
    with open('dataset.csv','a',newline='') as file:
        wr = csv.writer(file,dialect='excel')
        wr.writerow(entry)
'''
"""
import random
import numpy as np
for i in range(100):
    p= random.randint(1,15) ## taking periodicity 1 to 15 in account
    x = abs(10*random.random())
    m = abs(p*random.random())
    k = abs(10*random.random())
    X=[]
    for i in range(p):        
        X.append(round(x*(np.cos((3.14/3)*(i+m))) + k , 2 ))
    for j in range((20/p)-1):
        for i in range(p):          
            X.append(X[i])
    for j in range ((20%p)):
        X.append(X[j])
    
    y = 1# Add flag
    entry = X
    entry.append(y)
    # First 20 columns are points and 21st column is flag
    import csv
    with open('dataset.csv','a',newline='') as file:
        wr = csv.writer(file,dialect='excel')
        wr.writerow(entry)   
"""
'''
import random
for i in range(100):
    X=[]
    for j in range(20):
        X.append(round(10*random.random(),2))

    
    y = 0# Add flag
    entry = X
    entry.append(y)
    # First 20 columns are points and 21st column is flag
    import csv
    with open('dataset.csv','a',newline='') as file:
        wr = csv.writer(file,dialect='excel')
        wr.writerow(entry)