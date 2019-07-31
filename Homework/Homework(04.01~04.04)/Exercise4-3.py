### Exercise 4-3

import pandas as pd
import numpy as np

## 연습 문제 1
## 1. 모든 행과 열에 라벨을 가지는 5 x 5 이상의 크기를 가지는 데이터프레임을 만든다.

data = np.arange(1, 101).reshape(10, 10)
index = ['행1', '행2', '행3', '행4', '행5', '행6', '행7', '행8', '행9', '행10']
columns = ['열1', '열2', '열3', '열4', '열5', '열6', '열7', '열8', '열9', '열10']
df = pd.DataFrame(data,
                  columns = columns,
                  index = index)


## 2. 10가지 이상의 방법으로 특정한 행과 열을 선택한다.
df[1:2]
df['열9']
df['열9'][3]
df[:6:2]
df[['열5','열10']][2:9:2]
df[4:]
df.loc[['행5', '행8'], ['열1', '열6']]
df.iloc[0,1]
df.iloc[: 2,2]
df.iloc[2:3, 5:9]
df.iloc[-1] * 3