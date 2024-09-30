import json
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
import joblib

#? Preprocessing stage
# Download data source first on terminal:
# wget https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data
# wget https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.test
# wget https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.names

# Extract features from data
features = ["age", "workclass", "fnlwgt", "education", "education-num", "marital-status", "occupation", "relationship", "race" , "sex", "capital-gain", "capital-loss", "hours-per-week", "native-country", "income"]

# Combine lại dữ liệu và label, dùng pandas đọc cho rõ ràng
data_train = pd.read_csv("adult.data", sep=", ", header=None, engine='python')
data_train.columns = features
print(data_train.head())

# C engine of pandas does not support >1-length-separator so we switch to slower one: Python engine
# data_test = pd.read_csv("adult.test", sep=", ", header=None, engine='python', skiprows=1)
# data_test.columns = features

# Lấy features các cột trừ cột income, bởi cột income là cột label.
X_train = data_train[features[:-1]]
y_train = data_train["income"]
#print(X_train.shape, y_train.shape)

# X_test = data_test[features[:-1]]
# y_test = data_test["income"]
# print(X_test.shape, y_test.shape)

# Fill empty cells with the cell having the highest frequency
train_mode = dict(X_train.mode().iloc[0]) # mode() để lấy giá trị xuất hiện nhiều và iloc để xác định vị trí
X_train = X_train.fillna(train_mode) # fill giá trị NaN, Na, Null, ... bằng param đưa vào

# Transform categorical columns into numbers using LabelEncoder (alternative: OneHotEncoder)
features_categorical = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex','native-country']
encoders = {}

#! this code does not store the fitted encoders
# for column in features_categorical:
#     X_train[column] = LabelEncoder().fit_transform(X_train[column])
#     encoders[column] = LabelEncoder()

for column in features_categorical:
    print(X_train[column][0])
    enc = LabelEncoder()
    X_train[column] = enc.fit_transform(X_train[column])
    encoders[column] = enc

#print(X_train.head())

# Dữ liệu ở các cột age, fnlwgt, education-num, ... đang có dtype là string, nên tôi phải chuyển về dạng int64
for c in features[:-1]:
    if X_train[c].dtypes != "int64":
        X_train[c] = X_train[c].apply(lambda x: x.split(',')[0]).astype('int')

#? Training stage
# train the Random Forest algorithm
rf = RandomForestClassifier(n_estimators = 100) # n_estimators: số  lượng trees
rf = rf.fit(X_train, y_train)

# train the Extra Trees algorithm
et = ExtraTreesClassifier(n_estimators = 100)
et = et.fit(X_train, y_train)

print("Finish training")

# save preprocessing objects and weights
joblib.dump(train_mode, "./train_mode.joblib", compress=True)
joblib.dump(encoders, "./encoders.joblib", compress=True)
joblib.dump(rf, "./random_forest.joblib", compress=True)
joblib.dump(et, "./extra_trees.joblib", compress=True)

print("Finish packaging with joblib")