# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:30:23 2024

@author: ilnyu
"""

import pandas as pd

df = pd.DataFrame([[15,'남','덕명중'],[17,'여','수리중']],
                  index = ['준서','예은'],columns = ['나이','성별', '학교'])

print(df)
print(df.index)
print(df.columns)

#행 인덱스 변경 : DataFrame 객체.index = 새로운 행 인덱스 배열
df.index = ['student1','student2']

#열 이름 변경 : DataFrame 객체.columns = 새로운 열 이름 배열
df.columns = ['age','gender','belong to']

print(df)
print(df.index)
print(df.columns)