#NumPy Data Types
#By default Python have these data types:

# strings -
# integer -
# float-
# boolean -
# complex -

#Data Types in NumPy

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )


#Get the data type of an array object :?

import numpy as np

arr= np.array([1,2,3,4])

print((arr.dtype))