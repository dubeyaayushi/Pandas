# what are we gonna learn
# 1 How to select a specififc column
# 2 How to filter rows
# 3 How to combine Multiple conditions 


# Answers to above questions are
# 1 in order to select a particular column we use square brack
# 2 in order to filter rows we use boolean condition

# selecting columns humein ek series(series of column) return karega (ye single column ke liye hai)
# dusra ye dataframe return karega that is multiple column of data( ye dusra vala tab return karega jab hum multiple columns ko access kar rhe honge )


#filtering rows
#ismein hum ek specifc conditon de kar ke data extract kartet hai aka extracting data based on some specific condition iske liye hum boolean indexing ka use karte hai 

# Accessing a column
# column = df["Column Name of that particular column"]
# for selecting multiple columns
# subset = df["Column1", "Column2","Column3",...."columnN"]


#filtering rows based on a specifc condition

# based on a single condition
# filtered_Rows = df[df["Column Name"] condition]
# example suppose we want to find out the salary above 50000 the 
# filtered_Rows = df[df["Salary"]>50000]

#for multiple conditions
# suppose we want to find the salary of employee who have salary above 50000 but below 60000
# filtered_Rows = df[(df["Column"]>50000)& (df['Column2]<8000)]

import pandas as pd
 
data = {
    "Name": ["Ram","Shayam","Ghanshyama","Mira","Shira"],
    "Age": [22,23,20,23,24],
    "Salary":[500,600,400,700,750],
    "Perfromamnce Score":[85,87,89,86,88]
}

df = pd.DataFrame(data)
print(df)

#selecting single column it will return series
print('Displaying a single column')
name = df['Name']
print(name)

#selecting multiple column
subset = df[["Name" ,"Age"]] #yaha ye subset ki jagah kuch bhi name de sakte hai 
print('\n Subset with Name and Age')
print(subset)


#filtering rows
#filtering rows based on single condtion
high_salary = df[df['Salary']>500]
print("\n Employees with Salary > 500")
print(high_salary)

#filtering rows with multiple conditions
filtered = df[(df['Age']>20)&(df['Salary']>500)]
print('Name of Employees with age > 20 and salary >500')
print(filtered)

#filtering rows with multiple consition using or operator the 'or' operator returns the value even if a single ccondtion is true

filtered_or = df[(df['Age']>35) | (df['Perfromamnce Score']>87)]
print('\n Employees whose age is either > 35 or Perfromamnce Score is > 87')
print(filtered_or)