### Exercise 4-5

import pandas as pd
import numpy as np

## 연습 문제 1¶
## 5명의 학생의 국어, 영어, 수학 점수를 나타내는 데이터프레임을 다음과 같이 만든다.

# 1. 학생 이름을 나타내는 열을 포함시키지 않고 데이터프레임 df_score1 을 생성한 후,
# df_score1.index 속성에 학생 이름을 나타내는 열을 지정하여 인덱스를 지정한다.
# reset_index 명령으로 이 인덱스 열을 명령으로 일반 데이터열로 바꾸여 데이터프레임 df_score2을 만든다.
df_score1 = pd.DataFrame({'국어': [50, 60, 70, 80, 90],
                          '영어': [40, 50, 60, 70, 80],
                          '수학': [60, 60, 70, 70, 40]})

df_score1.index = ['길동', '영희', '철구', '짱구', '머저리']
df_score1.index.name = '이름'

df_score2 = df_score1.reset_index()

df_score1
df_score2

# 2. 학생 이름을 나타내는 열이 일반 데이터 열을 포함하는
#    데이터프레임 df_score2에 set_index 명령을 적용하여 다시 학생 이름을 나타내는 열을 인덱스로 변경한다.
df_score2 = df_score2.set_index('이름')
df_score2




## 연습 문제 2
## A 반 학생 5명과 B반 학생 5명의 국어, 영어, 수학 점수를 나타내는 데이터프레임을 다음과 같이 만든다.

# 1. "반", "번호", "국어", "영어", "수학" 을 열로 가지는 데이터프레임 df_score3을 만든다.
import random

s1 = []
for i in range(10):
    result = random.randint(50, 100)
    s1.append(result)
s2 = []
for i in range(10):
    result = random.randint(50, 100)
    s2.append(result)
s3 = []
for i in range(10):
    result = random.randint(50, 100)
    s3.append(result)

df_score3 = pd.DataFrame({'반': ['A','A','A','A','A','B','B','B','B','B'],
                          '번호': [11, 22, 13, 24, 15, 26, 17, 28, 19, 20],
                          '국어': s1,
                          '영어': s2,
                          '수학': s3})
                         #columns = ['반', '번호', '국어', '영어', '수학'])
df_score3


# 2. df_score3을 변형하여
# 1차 행 인덱스로 "반"을
# 2차 행 인덱스로 "번호"을 가지는 데이터프레임 df_score4을 만든다.
df_score4 = df_score3.set_index(['반', '번호'])
df_score4

# 3. 데이터 프레임 df_score4에 각 학생의 평균을 나타내는 행을 오른쪽에 추가한다.
df_score4['평균'] = df_score4.mean(axis = 1).round(2)
df_score4

# 4. df_score3을 변형하여
# 행 인덱스로 "번호"를,
# 1차 열 인덱스로 "국어", "영어", "수학"을,
# 2차 열 인덱스로 "반"을 가지는 데이터프레임 df_score5을 만든다.
df_score5 = df_score3.set_index(['반', '번호']).unstack('반')
df_score5

# 5. 데이터 프레임 df_score5에 각 반별 각 과목의 평균을 나타내는 행을 아래에 추가한다.
df_score5.loc['평균'] = df_score5.mean(axis = 0)
df_score5
