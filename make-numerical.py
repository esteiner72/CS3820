import pandas as pd

mappings = {
    'Yes': 1,
    'No': 0,
    'High': 2,
    'Normal': 1,
    'Low': 0,
    'Female': 1,
    'Male': 0
}

df = pd.read_csv('Downloads/Disease_symptom_and_patient_profile_dataset.csv')
df.replace(mappings, inplace=True)
df.to_csv('trimmed_disease_data.csv', index=False)