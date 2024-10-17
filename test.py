import pandas as pd

df = pd.read_csv('/Users/Ethan/Downloads/Final_Augmented_dataset_Diseases_and_Symptoms.csv')

df.columns = df.columns.str.strip()

disease_counts = df.iloc[:, 0].value_counts()
print("Disease counts:\n", disease_counts)

diseases = disease_counts.head(30).index.tolist()

symptom_counts = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce').sum().sort_values(ascending=False)
symptoms = symptom_counts.head(30).index.tolist()

print("Top Symptoms:", symptoms)
print("Top Diseases:", diseases)
