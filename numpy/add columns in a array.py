import numpy as np

# Original array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# New column to add
new_col = np.array([[7], [8]])

# Stack the new column horizontally
arr = np.hstack([arr, new_col])
print(arr)



import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
newcol = np.array([[7],[8]])
arr = np.hstack([arr,newcol])
print(arr)