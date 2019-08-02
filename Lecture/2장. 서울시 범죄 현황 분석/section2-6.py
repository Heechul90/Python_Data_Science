### section 2-6 Pivot_table을 이용해서 데이터 정리하기

import pandas as pd
import numpy as np

# 데이터 불러오기
crime_anal_raw = pd.read_csv('Lecture/Data/02. crime_in_Seoul_include_gu_name.csv',
                             encoding = 'utf-8',
                             index_col = 0)
crime_anal_raw

crime_anal = pd.pivot_table(crime_anal_raw,
                            index = '구별',
                            aggfunc = np.sum)
crime_anal

# 강간검거율
crime_anal['강간검거율'] = crime_anal['강간 검거'] / crime_anal['강간 발생'] * 100

# 강도검거율
crime_anal['강도검거율'] = crime_anal['강도 검거'] / crime_anal['강도 발생'] * 100

# 살인검거율
crime_anal['살인검거율'] = crime_anal['살인 검거'] / crime_anal['살인 발생'] * 100

# 절도검거율
crime_anal['절도검거율'] = crime_anal['절도 검거'] / crime_anal['절도 발생'] * 100

# 폭력검거율
crime_anal['폭력검거율'] = crime_anal['폭력 검거'] / crime_anal['폭력 발생'] * 100

# 검거 삭제하기
del crime_anal['강간 검거']
del crime_anal['강도 검거']
del crime_anal['살인 검거']
del crime_anal['절도 검거']
del crime_anal['폭력 검거']

crime_anal.head()

# 검거율이 100이 넘는거는 100으로 처리
con_list = ['강간검거율', '강도검거율', '살인검거율', '절도검거율', '폭력검거율']

for column in con_list:
    crime_anal.loc[crime_anal[column] > 100, column] = 100

crime_anal.head()

# 발생이라는 열 이름 삭제
crime_anal.rename(columns = {'강간 발생': '강간',
                             '강도 발생': '강도',
                             '살인 발생': '살인',
                             '절도 발생': '절도',
                             '폭력 발생': '폭력'}, inplace = True)
crime_anal.head()





### section 2-7 데이터 표현을 위해 다듬기
# 파이썬 머신러닝에 관한 모듈로 scikit learn에 있는 전처리(preprocessing)도구에는
# 최소값, 최대값을 이용해서 정규화시키는 함수이다.
from sklearn import preprocessing

# 강간, 강도, 살인, 절도, 폭력에 대해 컬럽별로 '정규화'하기
col = ['강간', '강도', '살인', '절도', '폭력']

x = crime_anal[col].values
min_max_scaler = preprocessing.MinMaxScaler()

x_scaled = min_max_scaler.fit_transform(x.astype(float))
crime_anal_norm = pd.DataFrame(x_scaled,
                               columns = col,
                               index = crime_anal.index)

col2 = ['강간검거율', '강도검거율', '살인검거율', '절도검거율', '폭력검거율']
crime_anal_norm[col2] = crime_anal[col2]
crime_anal_norm.head()

# CCTV_result.csv 파일 불러와서 구별 인구수와 CCTV 개수 가져오기
CCTV_result = pd.read_csv('Lecture/Data/01. CCTV_result.csv',
                          encoding = 'utf-8',
                          index_col = '구별')

crime_anal_norm[['인구수', 'CCTV']] = CCTV_result[['인구수', '소계']]
crime_anal_norm.head()

# 컬럼에 '범죄'에 발생 건수 합 넣기
col = ['강간', '강도', '살인', '절도', '폭력']
crime_anal_norm['범죄'] = np.sum(crime_anal_norm[col], axis = 1)
crime_anal_norm.head()

# 컬럼에 '검거'에 검거율 합 넣기
crime_anal_norm.columns
col = ['강간검거율', '강도검거율', '살인검거율', '절도검거율', '폭력검거율']
crime_anal_norm['검거'] = np.sum(crime_anal_norm[col], axis = 1)
crime_anal_norm.columns
crime_anal_norm

crime_anal_norm.to_csv('Lecture/Data/02. crime_anal_norm.csv')
