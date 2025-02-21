#Locate Named Indexes
#Use the named index in the loc attribute to return the specified row(s).

#Return "day2"?

import pandas as pd

data={"calories":[420,380,390],
      "duration":[50,40,45]}

#load data into a DataFrame object
df = pd.DataFrame(data,index=["day1","day2","day3"])


print(df.loc["day2"]) #return series

#Use the named index in the loc attribute to t=return row1 and row 2?
print(df.loc[["day1","day2"]])#return dataFrame