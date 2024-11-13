import pandas as pd

# How many of each disease we have 
df = pd.read_csv(r"data\\Original_Data.csv")
mappings = {}
index = 0
for disease in df["diseases"]:
    if disease in mappings.keys():
        mappings[disease] += 1
    else:
        mappings[disease] = 1
print(mappings.items())


#creating a dataframe with a single instance for each disease
df.drop_duplicates(subset=["diseases"], inplace=True)
df.to_csv(r"data\\Diseases_1_Instance.csv", index=False)
