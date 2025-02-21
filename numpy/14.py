#Access 2-D Arrays
#To access elelments  from 2-D arrays we can use
# comma sepreated integers representing the dimensions
# and the index of the element .

#Think of 2-D arrays like a table with rows and  columns ,
#where the dimension represents the row and the index represents the column.
#Access the element on the first row , second column?

import numpy as np

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print('2nd element on 1st row :',arr[0,1])
                                 #row index number , element index number