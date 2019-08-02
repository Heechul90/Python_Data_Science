### section 2-5 Pandas의 pivot_table 학습하기

import pandas as pd
import numpy as np

# 데이터 불러오기
df = pd.read_excel('Lecture/Data/02. sales-funnel.xlsx')
df.head()

# Name 항목으로 정렬해 pivot_table 만들기
pd.pivot_table(df, index = 'Name')

pd.pivot_table(df, index = ['Name', 'Rep', 'Manager'])

# 특정 value만 지정(value 값은 평균임)
pd.pivot_table(df,
               index = ['Manager', 'Rep'],
               values = 'Price')

# 합계를 사용하려면 aggfunc 옵션을 이용해서 np.sum을 사용
pd.pivot_table(df,
               index = ['Manager', 'Rep'],
               values = ['Price'],
               aggfunc = np.sum)

# 합산, 평균 표시하고 NaN은 0으로 하기
pd.pivot_table(df,
               index = ['Manager', 'Rep', 'Product'],    # index 지정
               values = ['Price', 'Quantity'],           # value 지정
               aggfunc = [np.sum, np.mean],              # 합산, 평균
               fill_value = 0,                           # NaN을 0으로 처리
               margins = True)                           # 행열별 총합

