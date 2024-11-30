from pickle import load
import numpy as np
from numpy.linalg import norm
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import csv
from sklearn.utils import Bunch
from scipy import spatial
from sklearn.metrics import classification_report

with open("clf.pkl", "rb") as f:
    clf = load(f)

user_input = [0] * 377
with open(r'data/User_Input.csv') as csv_file:
    data_reader = csv.reader(csv_file)
    data = next(data_reader)
for item in range(len(data)):
    data[item] = int(data[item])
    user_input[data[item]] = 1
user_input = np.array(user_input)
user_input = user_input.reshape(1, -1)
user_pred = clf.predict(user_input)

print(user_pred[0])

result = ""
with open("data/Disease_Map.csv", mode="r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        disease_name, disease_id = row[0], int(row[1])
        if user_pred[0] == disease_id:
            result = disease_name
            break

with open("data/result.csv", mode="w") as file:
    csv_write = csv.writer(file)
    csv_write.writerow([result])
