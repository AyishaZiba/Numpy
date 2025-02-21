#NumPy Filter Array
#If the value at an index is True that element
#is contained in the filtered array,
#if the value at that index is False that element is excluded,
#from the filtered array.

#Create an array from the elements on index 0 and 1 :?

import numpy as np

arr = np.array([41,42,43,44])

x=[True,False,True,False]

newarr = arr[x]

print(newarr)
