#Creating Arrays With  a Defined Data Type

# dtype - allows us to define the expected data type of the array elements

#Create an array with data type string ?

import numpy as np

arr = np.array([1,2,3,2], dtype='S')

print(arr)
print(arr.dtype)  #s1 = length of integer