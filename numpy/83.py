#Create a filter array that will
# return only en=ven elements from the original array?

import numpy as np

arr= np.array([1,2,3,4,5,6,7])

filter_arr = arr % 2 == 0

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)