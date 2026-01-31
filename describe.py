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



# You will see the percentiles(25%, 50%, 75%..etc) and some values in front of them.

# The significance is to tell you the distribution of your data.

# For example:

# s = pd.Series([1, 2, 3, 1])

# s.describe()   will give

# count    4.000000
# mean     1.750000
# std      0.957427
# min      1.000000
# 25%      1.000000
# 50%      1.500000
# 75%      2.250000
# max      3.000000
# 25% means 25% of your data have the value 1.0000 or below. That is if you were to look at your data manually, 25% of it is less than or equal 1. (you will agree with this if you look at our data [1, 2, 3, 1]. [1] which is 25% of the data is less than or equal to 1.

# 50% means 50% of your data have the value 1.5 or below. [1, 1] which constitute 50% of the data are less than or equal 1.5.

# 75% means 75% of your data have the value 2.25 or below. [1, 2, 1] which constitute 75% of the data are less than or equal 2.25.

