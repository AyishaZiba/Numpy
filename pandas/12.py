#Load  Files Into DataFrame
#If your data sets are stored on s=a file , Pandas can load then into a DtaFrame '

#Load a comma seperated file( CSV file) into a DataFrame?

import pandas as pd

df=pd.read_csv('data.csv')

print(df)