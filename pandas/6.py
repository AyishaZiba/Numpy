#DataFrames
#Data sets in pandas are usually multi-dimensional tables , calles DtaFrames.

#Series is like a column , a DtaFrame is the whole table.
#Create a DtaFrame from two series?

import pandas as pd

data={"calories":[420,380,390],
      "duration":[50,40,45]}

#load data into a DataFrame object
myvar = pd.DataFrame(data)

print(myvar)

#Apanda DtaFrame is a 2-D data structure,
#Like a 2 dimensional array, or a table with rows and columns.