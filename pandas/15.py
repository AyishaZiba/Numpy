#Increase the maximum number of rows to display the entire DtaFrame ?

import pandas as pd

pd.options.display.max_rows= 9999

df = pd.read_csv('data.csv')

print(df)