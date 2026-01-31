import pandas as pd

data = {
    "Name": ["Ram","Shayam","Ghanshyama","Mira","Shira"],
    "Age": [22,23,20,23,24],
    "Salary":[500,600,400,700,750],
    "Perfromamnce Score":[85,87,89,86,88]
}

df = pd.DataFrame(data)
print(df)
print(f'Shape: {df.shape}')
print(f'Column Names: {df.columns}')


# In pandas, the .shape attribute is used to get the dimensions (rows and columns) of a DataFrame, while the .columns attribute provides access to the column labels. 





