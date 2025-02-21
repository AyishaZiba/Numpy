#Pandas - Analyzing DataFrames

#Viewing the Data
#The head() method returns the headers anda specified number of rows,
#starting from the top.

#print the first 10 rows and headers of csv file as DtaFrame ?

import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(10))