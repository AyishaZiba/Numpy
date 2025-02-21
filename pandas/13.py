#Pandas Read CSV
#If you have a large DataFrame with many rows,
#too_string()--used to print the entire DataFrame .

import pandas as pd

df= pd.read_csv('big.csv')

print(df.to_string())

#print(df)--method
#will only return the firsst 5 rows, and the last 5 rows: