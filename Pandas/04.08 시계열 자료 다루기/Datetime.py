### 시계열 자료 다루기

import pandas as pd
import numpy as np

## Pandas에서 시계열 자료를 생성하려면 인덱스를 DatetimeIndex 자료형으로 만들어야 한다.
## DatetimeIndex는 특정한 순간에 기록된 타임스탬프(timestamp) 형식의 시계열 자료를 다루기 위한 인덱스이다.
## 타임스탬프 인덱스의 라벨값이 반드시 일정한 간격일 필요는 없다.

# DatetimeIndex 인덱스는 다음과 같은 보조 함수를 사용하여 생성한다.

# pd.to_datetime 함수
# pd.date_range 함수.

# pd.to_datetime 함수를 쓰면 날짜/시간을 나타내는 문자열을 자동으로 datetime 자료형으로 바꾼 후
# DatetimeIndex 자료형 인덱스를 생성
date_str = ['2018, 1,1', '2018, 1, 4', '2018, 1, 5', '2018, 1, 6']
idx = pd.to_datetime(date_str)
idx

# 만들어진 인덱스를 사용하여 시리즈나 데이터프레임을 생성하면 된다.
np.random.seed(0)
s = pd.Series(np.random.randn(4),index = idx)
s

# pd.date_range 함수를 쓰면 모든 날짜/시간을 일일히 입력할 필요없이
# 시작일과 종료일 또는 시작일과 기간을 입력하면 범위 내의 인덱스를 생성
pd.date_range('2019-5-27', '2019-11-7')
pd.date_range(start = '2019-5-27', periods = 30)

# freq 인수로 특정한 날짜만 생성되도록 할 수도 있다. 많이 사용되는 freq 인수값은 다음과 같다.
# s: 초
# T: 분
# H: 시간
# D: 일(day)
# B: 주말이 아닌 평일
# W: 주(일요일)
# W-MON: 주(월요일)
# M: 각 달(month)의 마지막 날
# MS: 각 달의 첫날
# BM: 주말이 아닌 평일 중에서 각 달의 마지막 날
# BMS: 주말이 아닌 평일 중에서 각 달의 첫날
# WOM-2THU: 각 달의 두번째 목요일
# Q-JAN: 각 분기의 첫달의 마지막 날
# Q-DEC: 각 분기의 마지막 달의 마지막 날

pd.date_range(start = '2019-5-27', periods = 60, freq = 's')
pd.date_range(start = '2019-5-27', periods = 60, freq = 'T')
pd.date_range(start = '2019-5-27', periods = 60, freq = 'H')
pd.date_range(start = '2019-5-27', periods = 60, freq = 'D')
pd.date_range(start = '2019-5-27', periods = 60, freq = 'B')
pd.date_range(start = '2019-5-27', periods = 60, freq = 'W')
pd.date_range(start = '2019-5-27', periods = 60, freq = 'W-SAT') # 요일지정
pd.date_range(start = '2019-5-27', periods = 60, freq = 'M')
pd.date_range(start = '2019-5-27', periods = 60, freq = 'MS')
pd.date_range(start = '2019-5-27', periods = 20, freq = 'BM')
pd.date_range(start = '2019-5-27', periods = 20, freq = 'BMS')
pd.date_range(start = '2019-5-27', periods = 20, freq = 'WOM-2THU')
pd.date_range(start = '2019-5-27', periods = 20, freq = 'Q-JAN')
pd.date_range(start = '2019-5-27', periods = 20, freq = 'Q-DEC')



## shift 연산
## 시계열 데이터의 인덱스는 시간이나 날짜를 나타내기 때문에 날짜 이동 등의 다양한 연산이 가능하다.
## 예를 들어 shift 연산을 사용하면 인덱스는 그대로 두고 데이터만 이동할 수도 있다.
np.random.seed(0)
ts = pd.Series(np.random.randn(4),
               index = pd.date_range(start = '2018-1-1', periods = 4, freq = 'M'))
ts

ts.shift(1)      # values가 아래로 내려간다
ts.shift(-1)     # values가 위로 올라간다
ts.shift(1, freq = 'M')     # index가 아래로 내려간다
ts.shift(1, freq = 'W')     # index 주(일요일) 다 바뀜


## resample 연산
## resample 연산을 쓰면 시간 간격을 재조정하는 리샘플링(resampling)이 가능하다.
## 이 때 시간 구간이 작아지면 데이터 양이 증가한다고 해서 업-샘플링(up-sampling)이라 하고
## 시간 구간이 커지면 데이터 양이 감소한다고 해서 다운-샘플링(down-sampling)이라 부른다
ts = pd.Series(np.random.randn(100),
               index = pd.date_range(start = '2018-1-1', periods = 100, freq = 'D'))
ts

# 다운-샘플링의 경우에는 원래의 데이터가 그룹으로 묶이기 때문에
# 그룹바이(groupby)때와 같이 그룹 연산을 해서 대표값을 구해야 한다.
ts.resample('W').mean()
ts.resample('M').first()


# 날짜가 아닌 시/분 단위에서는 구간위 왼쪽 한계값(가장 빠른 값)은 포함하고
# 오른쪽 한계값(가장 늦은 값)은 포함하지 않는다.
# 즉, 가장 늦은 값은 다음 구간에 포함된다.
# 예를 들어 10분 간격으로 구간을 만들면 10의 배수가 되는 시각은 구간의 시작점이 된다.
ts = pd.Series(np.random.randn(60),
               index = pd.date_range(start = '2018-1-1', periods = 60, freq = 'T'))
ts.head(20)

ts.resample('10T').sum()

# 왼쪽이 아니라 오른쪽 한계값을 구간에 포함하려면 closed="right" 인수를 사용한다.
# 이 때는 10의 배수가 되는 시각이 앞 구간에 포함된다.
ts.resample('10T', closed = 'right').sum()

# ohlc 메서드는 구간의 시고저종(open, high, low, close)값을 구한다.
ts.resample('5T').ohlc()

# 업-샘플링의 경우에는 실제로 존재하지 않는 데이터를 만들어야 한다.
# 이 때는 앞에서 나온 데이터를 뒤에서 그대로 쓰는 forward filling 방식과
# 뒤에서 나올 데이터를 앞에서 미리 쓰는 backward filling 방식을 사용할 수 있다.
# 각각 ffill, bfill 메서드를 이용한다.
ts.resample('30s').ffill().head(20)
ts.resample('30s').bfill().head(20)