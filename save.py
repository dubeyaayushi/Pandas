import pandas as pd

data = {
    "Name": ['Ram','Sham','Ghanshyam'],
    "Age": [10,20,30],
    "City": ['Nagpur','Mumbai','Delhi']
}
 
df = pd.DataFrame(data)
print(df)

# #to save my file as csv file
df.to_csv("output.csv", index= False)

#to save file as excel file
# df.to_excel("output.xlsx", index=False)

#to save file as json file
# df.to_json("output.json", index= false)

