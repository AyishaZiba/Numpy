#there are 3 ways to fill the missing value
# 1.mean(avg)  2.median(centre value) 3.mode()
#ways to fill mean
import pandas as pd

a=pd.read_csv('missing_data1.csv')
print(a.shape)
print(a.isna().sum())
print("*"*100)

#calories--->mean
x=a['Calories'].mean()
print(x)

print("*"*100)


a['Calories'].fillna(x,inplace=True)
print(a)
print("*"*100)