#date ---mode
#distance---mean
#avgmovingspeed--median
# fueleconomy--mode
import numpy as np
import pandas as pd

a=pd.read_csv('travel-times.csv')
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

#distance---mean
y=a['Distance'].mean()
print(y)
a['Distance'].fillna(y,inplace=True)
print(a)
print('*'*100)

#avgmoving speed---median
z=a['AvgMovingSpeed'].median()
print(z)
a['AvgMovingSpeed'].fillna(z,inplace=True)  #inplpace use cheyyunnath aa same file il fill cheyyan aan
print(a)

#fueleconomy--mode
b=a['FuelEconomy'].mode()[0]
print(b)
a['FuelEconomy'].fillna(b,inplace=True)
print(a)

print(a.isna().sum())
