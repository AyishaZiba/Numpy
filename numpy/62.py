#NumPy Splitting Srray

#array_split() ----method

#Split the array in 3 parts ?

import numpy as np

arr = np.array([1,2,3,4,5,6])

newarr = np.array_split(arr,3)
print(newarr)