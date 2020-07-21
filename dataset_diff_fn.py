import numpy as np
import matplotlib.pyplot as plt
import random
for i in range(100):
    X = []
    p = random.randint(1,10)
    n = random.randint(1,5)
    m = random.randint(-5,5)
    f = lambda x: (m*x+p/n) % (p) - p/n
    for j in range(20):
        X.append(f(j))
    #plt.scatter(list(range(len(X))),X)
    y = 1# Add flag
    entry = X
    entry.append(y)
    # First 20 columns are points and 21st column is flag
    import csv
    with open('data_test.csv','a',newline='') as file:
        wr = csv.writer(file,dialect='excel')
        wr.writerow(entry)