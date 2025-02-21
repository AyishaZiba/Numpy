#fill missing value specific column

import numpy as np
import pandas as pd

a = pd.read_csv('missing_data1.csv')
print(a.info())
print(a.shape)
print(a.isna().sum())
print('*'*100)
a['Calories'].fillna(300,inplace=True)
a['Date'].fillna('2020/12/22',inplace=True)
print(a)