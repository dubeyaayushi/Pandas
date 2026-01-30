import pandas as pd


# df = pd.read_csv("sales_data_sample.csv", encoding = "latin1")

# print('Displaying the info of data set')
# print(df.info())

data = {
    "Name": ['Ram','Sham','Ghanshyam'],
    "Age": [10,20,30],
    "City": ['Nagpur','Mumbai','Delhi']
}

df = pd.DataFrame(data)
print('Displaying the data info')
print(df.info())


