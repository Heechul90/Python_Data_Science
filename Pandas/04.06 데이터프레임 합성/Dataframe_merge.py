### 데이터프레임 병합

import pandas as pd
import numpy as np

## Pandas는 두 개 이상의 데이터프레임을 하나로 합치는 데이터 병합(merge)이나 연결(concatenate)을 지원

## merge 명령을 사용한 데이터프레임 병합
## merge 명령은 두 데이터 프레임의 공통 열 혹은 인덱스를 기준으로 두 개의 테이블을 합친다.
## 이 때 기준이 되는 열, 행의 데이터를 키(key)라고 한다.
df1 = pd.DataFrame({
    '고객번호': [1001, 1002, 1003, 1004, 1005, 1006, 1007],
    '이름': ['둘리', '도우너', '또치', '길동', '희동', '마이콜', '영희']
}, columns=['고객번호', '이름'])
df1

df2 = pd.DataFrame({
    '고객번호': [1001, 1001, 1005, 1006, 1008, 1001],
    '금액': [10000, 20000, 15000, 5000, 100000, 30000]
}, columns=['고객번호', '금액'])
df2

# merge 명령으로 위의 두 데이터프레임 df1, df2 를 합치면
# 공통 열인 고객번호 열을 기준으로 데이터를 찾아서 합친다.
# 이 때 기본적으로는 양쪽 데이터프레임에 모두 키가 존재하는 데이터만 보여주는 inner join 방식을 사용
pd.merge(df1, df2)

# outer join 방식은 키 값이 한쪽에만 있어도 데이터를 보여준다.
pd.merge(df1, df2, how = 'outer')

# left, right 방식은 각각 첫번째, 혹은 두번째 데이터프레임의 키 값을 모두 보여준다.
pd.merge(df1, df2, how = 'left')
pd.merge(df1, df2, how = 'right')



# 만약 테이블에 키 값이 같은 데이터가 여러개 있는 경우에는 있을 수 있는 모든 경우의 수를 따져서 조합을 만들어 낸다.
df1 = pd.DataFrame({
    '품종': ['setosa', 'setosa', 'virginica', 'virginica'],
    '꽃잎길이': [1.4, 1.3, 1.5, 1.3]},
    columns=['품종', '꽃잎길이'])
df1

df2 = pd.DataFrame({
    '품종': ['setosa', 'virginica', 'virginica', 'versicolor'],
    '꽃잎너비': [0.4, 0.3, 0.5, 0.3]},
    columns=['품종', '꽃잎너비'])
df2

pd.merge(df1, df2)

#두 데이터프레임에서 이름이 같은 열은 모두 키가 된다.
# 만약 이름이 같아도 키가 되면 안되는 열이 있다면 on 인수로 기준열을 명시해야 한다.
df1 = pd.DataFrame({
    '고객명': ['춘향', '춘향', '몽룡'],
    '날짜': ['2018-01-01', '2018-01-02', '2018-01-01'],
    '데이터': ['20000', '30000', '100000']})
df1

df2 = pd.DataFrame({
    '고객명': ['춘향', '몽룡'],
    '데이터': ['여자', '남자']})
df2

pd.merge(df1, df2, on = '고객명')

# 키가 되는 기준열의 이름이 두 데이터프레임에서 다르다면
# left_on, right_on 인수를 사용하여 기준열을 명시해야 한다.
df1 = pd.DataFrame({
    '이름': ['영희', '철수', '철수'],
    '성적': [1, 2, 3]})
df1

df2 = pd.DataFrame({
    '성명': ['영희', '영희', '철수'],
    '성적2': [4, 5, 6]})
df2

pd.merge(df1, df2, left_on = '이름', right_on = '성명')


# 일반 데이터 열이 아닌 인덱스를 기준열로 사용하려면
# left_index 또는 right_index 인수를 True 로 설정한다.
df1 = pd.DataFrame({
    '도시': ['서울', '서울', '서울', '부산', '부산'],
    '연도': [2000, 2005, 2010, 2000, 2005],
    '인구': [9853972, 9762546, 9631482, 3655437, 3512547]})
df1

df2 = pd.DataFrame(
    np.arange(12).reshape((6, 2)),
    index=[['부산', '부산', '서울', '서울', '서울', '서울'],
           [2000, 2005, 2000, 2005, 2010, 2015]],
    columns=['데이터1', '데이터2'])
df2

pd.merge(df1, df2, left_on = ['도시', '연도'], right_index = True)


df1 = pd.DataFrame(
    [[1., 2.], [3., 4.], [5., 6.]],
    index=['a', 'c', 'e'],
    columns=['서울', '부산'])
df1

df2 = pd.DataFrame(
    [[7., 8.], [9., 10.], [11., 12.], [13, 14]],
    index=['b', 'c', 'd', 'e'],
    columns=['대구', '광주'])
df2

pd.merge(df1, df2, how = 'outer', left_index = True, right_index = True)


## join 메서드
## merge 명령어 대신 join 메서드를 사용할 수도 있다.
df1.join(df2, how = 'outer')



