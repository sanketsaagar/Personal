#import csv 
#import pandas as pd

#b=pd.read_csv(r'/Users/sanket/Desktop/Blockchain/Python/Personal/iris.csv')

import csv
import math 

with open("iris.csv", 'r') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        print(" ", row)

c1= {'sepal.length':4.3,'sepal.width': 3.5,'petal.length': 2.7,'petal.width': 1.6}
c2= {'sepal.length':4.9,'sepal.width': 2.1,'petal.length': 2.4,'petal.width': 7.3}
c3= {'sepal.length':5.2,'sepal.width': 1.8,'petal.length': 7.2,'petal.width': 3.7}

dist = sqrt((int(c1[0])-mean[i][0])**2 +(int(c2[1])-mean[i][1])**2+(int(c3[2])-mean[i][2])**2 )


