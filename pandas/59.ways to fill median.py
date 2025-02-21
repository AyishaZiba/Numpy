#ways to fill -median

import numpy as np
import pandas as pd
a=pd.read_csv('missing_data1.csv')
print(a.shape)
print(a.isna().sum())
print("*"*100)

#calories--->median
y=a['Calories'].median()
print(y)

print("*"*100)

a['Calories'].fillna(y,inplace=True)
print(a)
print("*"*100)

print(a.isna().sum())