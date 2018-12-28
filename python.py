import sys
import numpy
import pandas as pd

data = pd.read_csv("./data.csv")

X = data.iloc[:, 0:4]  #independent columns
y = data.iloc[:,4]    #target column i.e price range

print("length of script: ", len(data))