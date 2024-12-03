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
probabilities = clf.predict_proba(user_input)
prob2 = [probabilities]
highest_3 = [prob2[0][0][0], 0, 0]
highest_3_i = [0, 0, 0]
for i in range(len(prob2[0][0])):
    if prob2[0][0][i] > highest_3[0]:
        highest_3[0] = prob2[0][0][i]
        highest_3_i[0] = i
        continue
    elif prob2[0][0][i] > highest_3[1]:
        highest_3[1] = prob2[0][0][i]
        highest_3_i[1] = i
        continue
    elif prob2[0][0][i] > highest_3[2]:
        highest_3[2] = prob2[0][0][i]
        highest_3_i[2] = i
        continue
print(highest_3)
print(highest_3_i)

result = ""
result2 = ""
result3 = ""
with open("data/Disease_Map.csv", mode="r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        disease_name, disease_id = row[0], int(row[1])
        if highest_3_i[0] == disease_id:
            result = disease_name
        elif highest_3_i[1] == disease_id:
            result2 = disease_name
        elif highest_3_i[2] == disease_id:
            result3 = disease_name

print(result)
print(result2)
print(result3)
data = "1.) {} \n".format(result)
data2 = "2.) {} \n".format(result2)
data3 = "3.) {} \n".format(result3)

with open("data/result.csv", mode="w") as file:
    csv_write = csv.writer(file)
    csv_write.writerows([[data]])
    csv_write.writerows([[data2]])
    csv_write.writerows([[data3]])

