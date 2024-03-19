# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:02:46 2024

@author: ilnyu
"""

import pandas as pd

#행/열 삭제
#행 삭제: DataFrame 객체.drop(행 인덱스 또는 배열, axis=0)
#열 삭제: DataFrame 객체.drop(열 이름 또는 배열, axis=1)

exam = {'math':[90,80,70],'eng':[98,89,95],'music':[85,95,100],'gym':[100,90,90]}

df = pd.DataFrame(exam,index = ['Seojun','Uhyeon','Inah'])
print(df)


#df를 복제하여 변수 df2에 저장, df2의 1개 행(row) 삭제
df2 = df [:]
df2.drop('Uhyeon',inplace=True)
print(df2)

#df를 복제하여 변수 df3에 저장, df3의 2개 행(row) 삭제 
df3 = df [:]
df3.drop(['Uhyeon','Inah'],axis = 0,inplace=True)
print(df3)

#df 복제하여 변수 df4에 저장, df4의 1개의 열(column) 삭제
df4 = df.copy()
df4.drop('math',axis=1,inplace=True)
print(df4)

#df 복제하여 변수 df5에 저장, df5의 2개의 열(column) 삭제
df5 = df.copy()
df5.drop(['eng','music'],axis=1,inplace=True)
print(df5)
