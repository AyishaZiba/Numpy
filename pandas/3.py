#Create Labels

#With the index argument, you can name your own labels.
#Create your own labels?

import pandas as pd

a = [1,7,2]
myvar = pd.Series(a, index=["x","y","z"])
print(myvar)

#Retunr the vlue "y"
print(myvar["y"])