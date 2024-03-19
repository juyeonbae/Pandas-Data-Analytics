# -*- coding: utf-8 -*-

import pandas as pd

dictData = {'c0':[1,2,3],'c1':[4,5,6],'c2':[7,8,9],'c3':[10,11,12],'c4':[13,14,15]}

df = pd.DataFrame(dictData)

print(type(df))
print(df)
