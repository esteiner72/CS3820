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
# Change on your laptop/machine if re-doing process (but we shouldn't need to)
df.to_csv('Documents/GitHub/CS3820/trimmed_disease_data.csv', index=False)