# -*- coding: utf-8 -*-

import pandas as pd

tup_data = ('영인', '2010-05-01','여',True)
sr = pd.Series(tup_data,index=['이름','생년월일','성별','학생여부'])
print(sr)
print('\n')

#원소 선택
print(sr[0]) # == print(sr['이름'])
print(sr[[1,2]]) #여러 인덱스 선택
print(sr[0:3]) #인덱스 범위 지정
