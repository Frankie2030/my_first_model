import json
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
import joblib

features = ["age", "workclass", "fnlwgt", "education", "education-num", "marital-status", "occupation", "relationship", "race" , "sex", "capital-gain", "capital-loss", "hours-per-week", "native-country", "income"]

data_train = pd.read_csv("adult.data", sep=" ", header=None)
data_train.columns = features
print(data_train.head())

X_train = data_train[features[:-1]]
y_train = data_train["income"]
print(X_train.shape, y_train.shape)
