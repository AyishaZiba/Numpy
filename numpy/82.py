#Creating ilter Directly From Array

#We can directly substitute the array instead
#of the iterable vaeiable in our condition and
#it will work just as we expect it to .

#Create a filter array that will return only values higher than 42?

import numpy as np

arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)