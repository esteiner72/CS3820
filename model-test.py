import numpy as np
from numpy.linalg import norm
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import csv
from sklearn.utils import Bunch
from scipy import spatial

def load_my_fancy_dataset():
    with open(r'C:\Users\Orange\JavaRepo\CS3820\trimmed_disease_data.csv') as csv_file:
        data_reader = csv.reader(csv_file)
        feature_names = next(data_reader)[:-1]
        data = []
        target = []
        for row in data_reader:
            features = row[1:]
            label = row[0]
            data.append([float(num) for num in features])
            target.append(int(label))
        
        data = np.array(data)
        target = np.array(target)
    return Bunch(data=data, target=target, feature_names=feature_names)
'''
test = [1, 0, 0, 1, 20, 0, 2]
data = load_my_fancy_dataset()
ex_data = data.data[1]
# to get rid of disease id num in disease data
ex_data = ex_data[1:]
print(test)
print(ex_data)
# calculating distance between vectors (lists)
#cos_sim = np.dot(test, ex_data)/(norm(test)*norm(ex_data))
cos_sim = spatial.distance.cosine(test, ex_data)
print((cos_sim))'''

dataset = load_my_fancy_dataset()
X = dataset.data
y = dataset.target
print(X)
print(y)

# Split the data into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.14, random_state=42)

# Standardize the features (mean=0, variance=1) using a vectorized operation
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train a logistic regression classifier
#clf = LogisticRegression(random_state=42)
clf = GaussianNB(var_smoothing=0.25)
clf.fit(X_train_scaled, y_train)

# Predict the test set results
y_pred = clf.predict(X_test_scaled)

# Output the accuracy of the classifier
print('Accuracy: {:.2f}'.format(accuracy_score(y_test, y_pred)))
print(y_pred)
print(y_test)
