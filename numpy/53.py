#Iterating With Different Step Size

#We can use filtering and followed by iteration .

#Iterate through every scalar element of the 20 array skipping 1 element?
import numpy as np

arr = np.array([[1,2,3,4],[5,6,7,8]])
for x in np.nditer(arr[:,::2]):
     print(x)

#This slice operation select all rows (:)
# and every second column starting from the first column (::2).
# so it selects columns 0 and 2 from both rows.
