import numpy as np
import pandas as pd
data= [[100,'ali','khan',23,'python','kannur',2000],
       [101,'rahul','h',34,'python','kozhikode',3000],
       [102,'anu','k',36,'python','kannur',3000],
       [102,'das','l',45,'bigdata','thrissur',2000],
       [103,'elna','shaji',30,'python','palakkad',2500]]
a = pd.DataFrame(data,columns=['id','fname','lname','age','prof','place','salary'])
print(a.describe())
#describe===> int values mathram print cheyum.
print("*"*100)
print(a.describe(include='O'))  #O(Caps 'o') is object top = most repeated value
                                #freg = frequency of the top
print("*"*100)
print(a.describe(include='all'))