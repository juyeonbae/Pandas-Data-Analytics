# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:33:59 2024

@author: ilnyu
"""

import pandas as pd

exam = {'math':[90,80,70],'eng':[98,89,95],'music':[85,95,100],'gym':[100,90,90]}
df = pd.DataFrame(exam,index = ['Seojun','Uhyeon','Inah'])
print(df)

'''
행 선택
loc / 탐색 대상: 인덱스 이름 (index label) / 범위 지정: 가능(범위의 끝 포함)
iloc / 탐색 대상: 정수형 위치 인덱스 (index position) / 범위 지정: 가능(범위의 끝 제외)
'''

#행 인덱스를 사용하여 행 1개 선택
label1 = df.loc['Seojun']
position1 = df.iloc[0]
print(label1)
print(position1)

#행 인덱스를 사용해서 행 2개 선택
label2 = df.loc[['Uhyeon','Inah']]
position2 = df.iloc[[0,1]]
print(label2)
print(position2)

#행 인덱스 범위를 지정하여 행 선택
label3 = df.loc['Seojun':'Uhyeon']
position3 = df.iloc[0:1]
print(label3)
print(position3)

'''
열 선택
열 1개 선택(시리즈 생성): DataFrame 객체["열이름"] 또는 DataFrame 객체.열이름 

열 N개 선택(데이터프레임 생성): DataFrame 객체[[열1,열2,...,열n]]
'''

math1 = df['math']
print(math1)
print(type(math1))

eng1 = df.eng
print(eng1)
print(type(eng1))

#'music', 'gym' 점수 데이터를 선택, 변수 music_gym에 저장
music_gym = df[['music','gym']]
print(music_gym)
print(type(music_gym))


#'math' 점수 데이터만 선택, 변수 math2에 저장
math2 = df[['math']]
print(math2)
print(type(math2))


'''
범위 슬라이싱의 고급 활용
범위 슬라이싱: DataFrame 객체.iloc[시작 인덱스:끝 인덱스:슬라이싱 간격]
역순으로 인덱싱하려면 "슬라이싱 간격"에 -1 입력
'''
