#ways to fill - mode

import pandas as pd
a=pd.read_csv('missing_data1.csv')
print(a.shape)
print(a.isna().sum())
print("*"*100)

#Date--->mode
x=a['Date'].mode()[0]
print(x)
print("*"*100)

a['Date'].fillna(x,inplace=True)
print(a)
print("*"*100)