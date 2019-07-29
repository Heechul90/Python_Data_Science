### section 1-3 (pandas 기초 익히기)

import pandas as pd
import numpy as np


## Series: pandas의 데이터 유형 중 기초가 되는 것이 Series

s = pd.Series([1, 3, 5, np.nan, 6, 8])     # np.nin: Not A Numbers
s

## 날짜형 데이터 date_range()

dates = pd.date_range('20130101', periods = 6)
dates


##

df = pd.DataFrame(np.random.randn(6, 4),           # 6행 4열의 random 변수
                  index = dates,                   # 위에서 만든 코드 dates를 지정ㄷ
                  columns = ['A', 'B', 'C', 'D'])  # 컬럼 이름 지정
df
df.head(3)     # 3번째 행까지만 추출

# pandas의 DataFrame의 컬럼과 인덱스를 확인
df.index
df.columns

# DataFrame의 내용 확인
df.values

# DataFrame의 개요 확인
df.info()

# DataFrame의 통계적 개요 확인
df.describe()

# vlues가 숫자가 아니라 문자라고 하더라도 그에 맞는 개요 나타남
df.sort_values(by = 'B',                # by로 지정된 컬럼을 기준으로 정렬
               ascending = False)       # ascending으로 오름차순이나 내림차순으로 정렬

df
df['A']                        # 컴럼만 Series로 보여줌
df[0 : 3]                      # 중간부터 보고 싶을 때
df['20130102' : '20130104']    # 원하는 날짜 구간을 보고 싶을 때

# dates 변수를 이용해서 특정 날짜의 데이터만 보고 싶을 때: df.loc
df.loc[dates[0]]               # loc은 location을 뜻함
df.loc[:, ['A', 'B']]          # A, B의 열의 모든 행
df.loc['20130102' : '20130104', ['A', 'B']]
df.loc['20130102', ['A', 'B']] # 20130102의 A, B 컬럼을 확인
df.loc[dates[0], 'A']          # dates[0]에 맞는 20130101의 A컬럼

# 행과 열의 번호를 이용해서 데이터에 바로 접근
df.iloc[3]                     # 3번 행(0번 부터 시작이니 4번 행)
df.iloc[3 : 5, 0 : 2]          # 3번째부터 5번째 앞행, 0번째 열부터 2번째 앞열까지
df.iloc[[1, 2, 4], [0, 2]]     # 1, 2, 4행의 0, 2번열
df.iloc[1 : 3, :]              # 1, 2행의 전체 열
df.iloc[:, 1 : 3]              # 전체 행의 1, 2 열

# 특정 조건을 만족하는 데이터 df.A, df['A']
df
df[df.A > 0]                   # 컴럼 A에서 0보다 큰 행
df[df > 0]                     # 데이터 전체에서 조건을 걸면 만족하지 않은 곳은 NaN 처리

# copy()
df2 = df.copy()

# 원래의 DataFrame에서 새로운 컬럼을 추가
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
df2
df2['E'].isin(['two','four'])           # E컬럼에 two와 four가 있는지 확인
df2[df2['E'].isin(['two', 'four'])]     # True만 반환


# df변수에서 좀 더 통계 느낌의 데이터
df
df.apply(np.cumsum)                     # numpy의 누적함
df.apply(lambda x: x.max() - x.min())   # 최대값과 최소값의 차이(두 점의 거리)

