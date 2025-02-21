#Creating the Filter Array
#Create a filter array that will reeturn only values higher than 42?

import numpy as np

arr = np.array([41,42,43,44])

#Create an empty list
filter_arr=[]

#go througgh each element in arr
for element in arr:
    #if the element is higher than 42 , set the value to True,
#otherwise False:
  if element> 42:
      filter_arr.append(True)
  else:
      filter_arr.append(False)

newarr= arr[filter_arr]
print(filter_arr)
print(newarr)