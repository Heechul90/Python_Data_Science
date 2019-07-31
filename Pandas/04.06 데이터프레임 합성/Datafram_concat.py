### 데이터프레임 병합

import pandas as pd
import numpy as np

## concat 명령을 사용한 데이터 연결
## concat 명령을 사용하면 기준 열(key column)을 사용하지 않고 단순히 데이터를 연결(concatenate)한다.
## 기본적으로는 위/아래로 데이터 행을 연결한다.
## 단순히 두 시리즈나 데이터프레임을 연결하기 때문에 인덱스 값이 중복될 수 있다.
s1 = pd.Series([0, 1], index=['A', 'B'])
s2 = pd.Series([2, 3, 4], index=['A', 'B', 'C'])

pd.concat([s1, s2])

# 만약 옆으로 데이터 열을 연결하고 싶으면 axis=1로 인수를 설정한다.
df1 = pd.DataFrame(
    np.arange(6).reshape(3, 2),
    index=['a', 'b', 'c'],
    columns=['데이터1', '데이터2'])
df1

df2 = pd.DataFrame(
    5 + np.arange(4).reshape(2, 2),
    index=['a', 'c'],
    columns=['데이터3', '데이터4'])
df2

pd.concat([df1, df2], axis = 1)