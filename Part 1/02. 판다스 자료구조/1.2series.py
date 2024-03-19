# -*- coding: utf-8 -*-
import pandas as pd

list_data = ['2024-03-19',3.14,'ABC',100,True,123]
sr = pd.Series(list_data)
print(sr)

idx = sr.index #인덱스 배열 
val = sr.values #데이터 값 배열 

print(idx)
print(val)