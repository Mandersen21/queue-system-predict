import sys
import numpy
import importlib
import pandas as pd

data = pd.read_csv("./data.csv")

X = data.iloc[:, 0:4]  #independent columns
y = data.iloc[:,4]    #target column i.e price range

wait = y

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

print(regressor.predict([[0, 0, 0, 40]]))