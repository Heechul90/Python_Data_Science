### 데이터프레임 인덱스 조작

import pandas as pd
import numpy as np

## 데이터프레임 인덱스 설정 및 제거
## set_index 명령이나
## reset_index 명령으로 인덱스와 일반 데이터 열을 교환할 수 있다.

# set_index : 기존의 행 인덱스를 제거하고 데이터 열 중 하나를 인덱스로 설정
# reset_index : 기존의 행 인덱스를 제거하고 인덱스를 데이터 열로 추가

np.random.seed(0)
df1 = pd.DataFrame(np.vstack([list('ABCDE'),
                              np.round(np.random.rand(3,5), 2)]).T,
                   columns = ['C1', 'C2', 'C3', 'C4'])
df1

# set_index 명령으로 C1열을 인덱스로 설정
df2 = df1.set_index('C1')
df2

# C2열을 인덱스로 지정하면 기존의 인덱스는 사라진다.
df2.set_index('C2')

# reset_index 명령으로 인덱스를 보통의 자료열로 바꿀 수도 있다.
# 이 때 인덱스 열은 자료열의 가장 선두로 삽입된다.
# 데이터프레임의 인덱스는 정수로 된 디폴트 인덱스로 바뀐다.
df2.reset_index()

# reset_index 명령 사용시에 drop=True 로 설정하면
# 인덱스 열을 보통의 자료열로 올리는 것이 아니라 그냥 버리게 된다.
df2.reset_index(drop = True)


## 다중 인덱스
## 행이나 열에 여러 계층을 가지는 인덱스 즉, 다중 인덱스(multi-index)를 설정할 수도 있다.
## 데이터프레임을 생성할 때 columns 인수에
## 다음 예제처럼 리스트의 리스트(행렬) 형태로 인덱스를 넣으면 다중 열 인덱스를 가지게 된다.
np.random.seed(0)
df3 = pd.DataFrame(np.round(np.random.randn(5, 4), 2),
                   columns=[["A", "A", "B", "B"],
                            ["C1", "C2", "C1", "C2"]])
df3

# 인덱스들의 이름 지정은 columns 객체의 names 속성에 리스트를 넣어서 지정한다.
df3.columns.names = ['Cidx1', 'Cidx2']
df3


## index 인수에 리스트의 리스트(행렬) 형태로 인덱스를 넣으면 다중 (행) 인덱스를 가진다.
## 행 인덱스들의 이름 지정은 index 객체의 names 속성에 리스트를 넣어서 지정한다.
np.random.seed(0)
df4 = pd.DataFrame(np.round(np.random.randn(6, 4), 2),
                   columns=[["A", "A", "B", "B"],
                            ["C", "D", "C", "D"]],
                   index=[["M", "M", "M", "F", "F", "F"],
                          ["id_" + str(i + 1) for i in range(3)] * 2])
df4.columns.names = ["Cidx1", "Cidx2"]
df4.index.names = ["Ridx1", "Ridx2"]
df4



## 행 인덱스와 열 인덱스 교환
## stack 명령이나 unstack 명령을 쓰면 열 인덱스를 행 인덱스로 바꾸거나
## 반대로 행 인덱스를 열 인덱스로 바꿀 수 있다.

# stack(): 열 인덱스 -> 행 인덱스로 변환
# unstack(): 행 인덱스 -> 열 인덱스로 변환

# stack 명령을 실행하면 열 인덱스가 반시계 방향으로 90도 회전한 것과 비슷한 모양이 된다.
# 마찬가지로 unstack 명령을 실행하면 행 인덱스가 시계 방향으로 90도 회전한 것과 비슷하다.
# 인덱스를 지정할 때는 문자열 이름과 순서를 표시하는 숫자 인덱스를 모두 사용할 수 있다.
df4.stack('Cidx1')
df4.stack(1)
df4.unstack("Ridx2")
df4.unstack(0)


## 다중 인덱스가 있는 경우의 인덱싱
## 데이터프레임이 다중 인덱스를 가지는 경우에는 인덱스가 하나의 라벨이나 숫자가 아니라
## ()로 둘러싸인 튜플이 되어야 한다.
df3
df3[('B', 'C1')]
df3.loc[0, ('B', 'C1')]
df3.loc[0, ('B', 'C1')] = 100

# iloc 인덱서를 사용하는 경우에는 튜플 형태의 다중인덱스를 사용할 수 없다.
df3.iloc[0, 2]

# 만약 하나의 레벨 값만 넣으면 다중 인덱스 중에서 가장 상위의 값을 지정한 것으로 본다
df3['A']

# df4 데이터프레임은 다음과 같이 인덱싱할 수 있다.
df4.loc[('M', 'id_1'), ('A', 'C')]
df4.loc[:, ('A','C')]
df4.loc[('M', 'id_1'), :]
df4.loc[('All', 'All'), :] = df4.sum()
df4



## 다중 인덱스의 인덱스 순서 교환
## 다중 인덱스의 인덱스 순서를 바꾸고 싶으면 swaplevel 명령을 사용한다.

# swaplevel(i, j, axis)
# i와 j는 교환하고자 하는 인덱스 라벨(혹은 인덱스 번호)이고
# axis는 0일 때 행 인덱스, 1일 때 열 인덱스를 뜻한다. 디폴트는 행 인덱스이다.
df5 = df4.swaplevel('Ridx1', 'Ridx2')
df5

df6 = df4.swaplevel('Cidx1', 'Cidx2', 1)
df6


## 다중 인덱스가 있는 경우의 정렬
## 다중 인덱스가 있는 데이터프레임을 sort_index로 정렬할 때는
## level 인수를 사용하여 어떤 인덱스를 기준으로 정렬하는지 알려주어야 한다.
df5.sort_index(level = 0)
df5.sort_index(axis = 1, level = 1)
