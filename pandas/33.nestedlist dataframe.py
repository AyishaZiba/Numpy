#Used for 2D data.
import numpy as np
import pandas as pd
data = [[100,'ali','khan',23,'python','kannur',2000],
       [101,'rahul','h',34,'python','kozhikode',3000],
       [102,'anu','k',36,'python','kannur',3000],
       [102,'das','l',45,'bigdata','thrissur',2000],
       [103,'elna','shaji',30,'python','palakkad',2500]]

a = pd.DataFrame(data,columns=['id','fname','lname','age','prof','place','salary'])
print(a)
print(a.shape)
print(a.columns)
print("*"*100)
print(a.dtypes)  #string is readed as object
