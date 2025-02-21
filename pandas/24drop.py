#Pandas - Cleaning Empty Cells
 #Return a new Dta Frame with  no empty cells?

import pandas as pd

df = pd.read_csv('data1.csv')
print(df)
new_df = df.dropna()

print(new_df.to_string())

#Note: By default , the dropna() method returns a new DataFrame ,
#and will not change the original .
#none values row will be deleted.