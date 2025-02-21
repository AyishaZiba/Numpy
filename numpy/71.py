#Find the indexes where the values are odd?

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8])

x =np.array(arr%2 == 1)
print(x)