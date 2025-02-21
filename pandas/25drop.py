#If you want to change the original DtaFrame ,
#Use the inplace = True argument:

#Remove all rowss with NULL values ?

import pandas as pd

df =  pd.read_csv('data1.csv')

df.dropna(inplace= True,ignore_index= True)

print(df.to_string())

#Note: Now, the dropna (inplace = True)
#will NOT return a new DataFrame ,
#but it will remove all rows containing NULL values
#from the original DataFrame .