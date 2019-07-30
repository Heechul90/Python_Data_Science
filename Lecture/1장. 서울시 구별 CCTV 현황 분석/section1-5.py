### section 1-5 (pandas 고급기능 - 두 DataFrame 병합하기)
import pandas as pd
import numpy as np

## 연습용 데이터 프레임 만들기

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[4, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                   index=[8, 9, 10, 11])

## concat 명령은 단순히 합치는 것

result = pd.concat([df1, df2, df3])            # 아무 옵션이 없으면 열 방향으로 병합
result

result = pd.concat([df1, df2, df3],
                   keys = ['x', 'y', 'z'])     # key 지정된 구분은 다중 index가 되어 level을 형성
result

# index 확인하기
result.index
result.index.get_level_values(0)
result.index.get_level_values(1)

# 'df4' 데이터 프레임 만들기

df4 = pd.DataFrame({'B': ['B2', 'B3', 'B6', 'B7'],
                    'D': ['D2', 'D3', 'D6', 'D7'],
                    'F': ['F2', 'F3', 'F6', 'F7']},
                   index = [2, 3, 6, 7])

# df4와 df1 병합하기
# concat 명령은 index를 기준으로 병합하기 때문에
# 값을 가질 수 없는 곳은 NaN이 저장됨

result = pd.concat([df1, df4],
                   axis = 1)                   # 행 방향으로 병합
result

# 공통된 index로 합치거나 버리기

result = pd.concat([df1, df4],
                   axis = 1,
                   join = 'inner')             # 공통된 index만 병합
result

# join_axes = [df1.index]
result = pd.concat([df1, df4],
                   axis = 1,
                   join_axes = [df1.index])    # df1 index에 맞추기
result

# ignore_index = True 옵션
result = pd.concat([df1, df4],
                   ignore_index = True)        # 두 데이터의 index를 무시하고 합친 후 다시 index를 부여
result


## 데이터 프레임 만들기

left = pd.DataFrame({'key': ['K0', 'K4', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

# merge 명령어로 병합
pd.merge(left, right, on = 'key')                    # on 옵션으로 key를 설정하면 공통된 key로 병합

# how 옵션
pd.merge(left, right, how = 'left', on = 'key')      # left 데이터 기준으로 병합
pd.merge(left, right, how = 'right', on = 'key')     # right 데이터 기준으로 병합
pd.merge(left, right, how = 'outer', on = 'key')     # 데이터 결과를 모두 가져옴
pd.merge(left, right, how = 'inner', on = 'key')     # 공통된 요소만 가져옴

