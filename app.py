import pandas as pd 

#read adata from csv file into a dataframe

# df = pd.read_csv("sales_data_sample.csv", encoding="latin1")


#to read in sxcel
df = pd.read_json("sample_Data.json", encoding = "latin1")
print(df)


