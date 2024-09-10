import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = datasets.load_iris()
X = iris.data  # we only take the first two features.
y = iris.target

# Split the data into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features (mean=0, variance=1) using a vectorized operation
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train a logistic regression classifier
clf = LogisticRegression(random_state=42)
clf.fit(X_train_scaled, y_train)

# Predict the test set results
y_pred = clf.predict(X_test_scaled)

# Output the accuracy of the classifier
print('Accuracy: {:.2f}'.format(accuracy_score(y_test, y_pred)))