import pandas as pd




df = pd.read_csv('C:\\Users\\K4L3B\\git\\Projects C\\projects\\CS3820\\Diseases_and_Symptoms.csv')
mappings = {}
index = 0
for disease in df["diseases"]:
    if disease not in mappings.keys():
        mappings[disease] = index
        index += 1
print(mappings.items())

df.replace(mappings, inplace=True)
# Change on your laptop/machine if re-doing process (but we shouldn't need to)
df.to_csv('C:\\Users\\K4L3B\\git\\Projects C\\projects\\CS3820\\Diseases_and_Symptoms_Final.csv', index=False)

#Strip
df.columns = df.columns.str.strip()

disease_counts = df.iloc[:, 0].value_counts()
print("Disease counts:\n", disease_counts)

diseases = disease_counts.head(30).index.tolist()

symptom_counts = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce').sum().sort_values(ascending=False)
symptoms = symptom_counts.head(30).index.tolist()

print("\nTop Symptoms:".format(), symptoms)
print("\nTop Diseases:".format(), diseases)

"""
disease_to_drop = []
for disease in df["diseases"]:
    if disease not in diseases and disease not in disease_to_drop:
        disease_to_drop.append(disease)

all_symptoms = symptom_counts.head().index.tolist()
symptoms_to_drop = []
for symptom in all_symptoms:
    if symptom not in symptoms and symptom not in symptoms_to_drop:
        symptoms_to_drop.append(symptom)

print(df.columns)
df.drop(columns=symptoms_to_drop, inplace=True)
print("after")
print(df.columns)
trimmed_df = df
#trimmed_df.drop(index=symptoms_to_drop, inplace=True)
trimmed_df.to_csv('C:\\Users\\K4L3B\\git\\Projects C\\projects\\CS3820\\Diseases_and_Symptoms_Final_Trimmed.csv', index=False)
"""
