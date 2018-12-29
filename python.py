import sys
import numpy
import json
import importlib
import pandas as pd

# Get parameters from request
triage = int(sys.argv[1])
week = int(sys.argv[2])
time = int(sys.argv[3])
avgWait = int(sys.argv[4])

data = pd.read_csv("./data.csv")

X = data.iloc[:, 0:4]  #independent columns
y = data.iloc[:,4]    #target column i.e price range

wait = y

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

print(regressor.predict([[triage, week, time, avgWait]]))