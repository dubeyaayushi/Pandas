import pandas as pd

data = {
    "Name": ["Ram","Shayam","Ghanshyama","Mira","Shira"],
    "Age": [22,23,20,23,24],
    "Salary":[500,600,400,700,750],
    "Perfromamnce Score":[85,87,89,86,88]
}

df = pd.DataFrame(data)
print("Sample Dataframe")
print(df)

#descirbe numerical colummn ka ek summary statistics dega

print('Descriptive statistics')
print(df.describe())

