#Pandas  - Cleaning Data
#Data Cleaning
#Data cleaning means fixing bad data in your data set.
#Bad data could be:

#Empty cells
#Data in wrong format
#Wrong data
#Duplicates

import pandas as pd
df = pd.read_csv('data1.csv')

print(df.to_string())

#The data set contains some empty cells ("Date" in row 22, and "calories" in row 18
# and 28

#The data set contains wrong format  ("Date" in row 26)

#The data set contains wrong data ("Duration" in row 7).
#The data set contains duplicates(row 11 and12).