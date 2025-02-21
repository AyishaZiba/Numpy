#Locate Row
#Pandas use the loc attribute to return one or more specified row(s)

#Return row 0?
import pandas as pd

data={"calories":[420,380,390],
      "duration":[50,40,45]}

#load data into a DataFrame object
df = pd.DataFrame(data)

print(df)
print(df.loc[0])
