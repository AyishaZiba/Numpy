#Info About the Data

#The DtaFrames object has a method called info(),
#that gives you more information about the data set.

#Print information about th data?
import pandas as pd

df = pd.read_csv('data.csv')

print(df.info())