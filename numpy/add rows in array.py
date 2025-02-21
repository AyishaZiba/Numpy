import numpy as np

# Original array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# New row to add
new_row = np.array([[7, 8, 9]])

# Append the new row
arr = np.append(arr, new_row, axis=0)
print(arr)



import numpy as np

arr = np.array([1,2,3])

#new row
newrow = np.array([4,5,6])

arr1=np.append(arr,newrow,axis=0)

print(arr1)

import numpy as np

# Original array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# New row to add
new_row = np.array([7, 8, 9])

# Stack the new row vertically
arr = np.vstack([arr, new_row])
print(arr)


import numpy as np
arr2=np.array([[1,2,3],[4,5,6]])
newrow = np.array([7,8,9])
arr = np.vstack([arr2,newrow])
print(arr)