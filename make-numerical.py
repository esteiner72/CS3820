import pandas as pd

mappings = {
    'Yes': 1,
    'No': 0,
    'High': 2,
    'Normal': 1,
    'Low': 0,
    'Female': 1,
    'Male': 0,
    'Asthma': 0,
    'Stroke': 1,
    'Osteoporosis': 2,
    'Diabetes': 3,
    'Migraine': 4,
    'Influenza': 5,
    'Pneumonia': 6,
    'Hypertension': 7,
    'Hypothyroidism': 8,
}

df = pd.read_csv('Downloads/disease_data.csv')
df.replace(mappings, inplace=True)
# Change on your laptop/machine if re-doing process (but we shouldn't need to)
df.to_csv('Documents/GitHub/CS3820/trimmed_disease_data.csv', index=False)

df = pd.read_csv('Documents/GitHub/CS3820/trimmed_disease_data.csv')
df.drop('Asthma', inplace=True, axis=1) 
df.to_csv('Documents/GitHub/CS3820/trimmed_disease_data2.csv', index=False)

