### 피봇테이블과 그룹분석

import pandas as pd
import numpy as np

## 그룹분석
## 만약 키가 지정하는 조건에 맞는 데이터가 하나 이상이라서 데이터 그룹을 이루는 경우에는
## 그룹의 특성을 보여주는 그룹분석(group analysis)을 한다.

# 그룹분석은 피봇테이블과 달리 키에 의해서 결정되는 데이터가 여러개가 있을 경우
# 미리 지정한 연산을 통해 그 그룹 데이터의 대표값을 계산한다.
# Pandas에서는 groupby 명령을 사용하여 다음처럼 그룹분석을 한다.

# 1. 분석하고자 하는 시리즈나 데이터프레임에 groupby 메서드를 호출하여 그룹화를 한다.
# 2. 그룹 객체에 대해 그룹연산을 수행한다.

## groupby 메서드
## groupby 메서드는 데이터를 그룹 별로 분류하는 역할을 한다.
## groupby 메서드의 인수로는 다음과 같은 값을 사용한다.

# 열 또는 열의 리스트
# 행 인덱스

## 그룹연산 메서드
## groupby 결과, 즉 GroupBy 클래스 객체의 뒤에 붙일 수 있는 그룹연산 메서드는 다양하다.
## 다음은 자주 사용되는 그룹연산 메서드들이다.

# size, count: 그룹 데이터의 갯수
# mean, median, min, max: 그룹 데이터의 평균, 중앙값, 최소, 최대
# sum, prod, std, var, quantile : 그룹 데이터의 합계, 곱, 표준편차, 분산, 사분위수
# first, last: 그룹 데이터 중 가장 첫번째 데이터와 가장 나중 데이터

# 이 외에도 많이 사용되는 것으로는 다음과 같은 그룹연산이 있다.

# agg, aggregate
#   만약 원하는 그룹연산이 없는 경우 함수를 만들고 이 함수를 agg에 전달한다.
#   또는 여러가지 그룹연산을 동시에 하고 싶은 경우 함수 이름 문자열의 리스트를 전달한다.

# describe
#   하나의 그룹 대표값이 아니라 여러개의 값을 데이터프레임으로 구한다.

# apply
#   describe 처럼 하나의 대표값이 아닌 데이터프레임을 출력하지만 원하는 그룹연산이 없는 경우에 사용한다.

# transform
#   그룹에 대한 대표값을 만드는 것이 아니라 그룹별 계산을 통해 데이터 자체를 변형한다.


np.random.seed(0)
df2 = pd.DataFrame({
    'key1': ['A', 'A', 'B', 'B', 'A'],
    'key2': ['one', 'two', 'one', 'two', 'one'],
    'data1': [1, 2, 3, 4, 5],
    'data2': [10, 20, 30, 40, 50]
})
df2

# groupby 명령을 사용하여 그룹 A와 그룹 B로 구분한 그룹 데이터를 만든다.
groups = df2.groupby(df2.key1)
groups

# GroupBy 클래스 객체에는 각 그룹 데이터의 인덱스를 저장한 groups 속성이 있다.
groups.groups

# A그룹과 B그룹 데이터의 합계를 구하기 위해 sum이라는 그룹연산을 한다.
groups.sum()


# GroupBy 클래스 객체를 명시적으로 얻을 필요가 없다면
# groupby 메서드와 그룹연산 메서드를 연속으로 호출한다.
# 다음 예제는 열 data1에 대해서만 그룹연산을 하는 코드이다.
df2.data1.groupby(df2.key1).sum()

# 데이터를 그룹으로 나눈 GroupBy 클래스 객체 또는 그룹분석한 결과에서 data1만 뽑아도 된다.
df2.groupby(df2.key1)['data1'].sum()    # `GroupBy` 클래스 객체에서 data1만 선택하여 분석하는 경우
df2.groupby(df2.key1).sum()['data1']    # 전체 데이터를 분석한 후 data1만 선택한 경우


# 이번에는 복합 키 (key1, key2) 값에 따른 data1의 합계를 구하자.
# 분석하고자 하는 키가 복수이면 리스트를 사용한다.
df2.data1.groupby([df2.key1, df2.key2]).sum()

# 이 결과를 unstack 명령으로 피봇 데이블 형태로 만들수도 있다.
df2.data1.groupby([df2.key1, df2.key2]).sum().unstack('key2')


# 그룹분석 기능을 사용하면 인구 데이터로부터 지역별 합계를 구할 수도 있다.
data = {
    "도시": ["서울", "서울", "서울", "부산", "부산", "부산", "인천", "인천"],
    "연도": ["2015", "2010", "2005", "2015", "2010", "2005", "2015", "2010"],
    "인구": [9904312, 9631482, 9762546, 3448737, 3393191, 3512547, 2890451, 263203],
    "지역": ["수도권", "수도권", "수도권", "경상권", "경상권", "경상권", "수도권", "수도권"]
}
columns = ["도시", "연도", "인구", "지역"]
df1 = pd.DataFrame(data, columns=columns)
df1

df1['인구'].groupby([df1['지역'], df1['연도']]).sum().unstack('연도')


# 다음 데이터는 150 송이의 붓꽃(iris)에 대해
# 붓꽃 종(species)별로 꽃잎길이(sepal_length), 꽃잎폭(sepal_width), 꽃잎폭(sepal_width), 꽃잎폭(sepal_width)을 측정한 데이터이다.
# (Seaborn 패키지가 설치되어 있어야 한다.)
import seaborn as sns
iris = sns.load_dataset('iris')
iris


# 각 붓꽃 종별로 가장 큰 값과 가장 작은 값의 비율을 구해보자.
# 이러한 계산을 하는 그룹연산 메서드는 없으므로 직접 만든 후 agg 메서드를 적용한다.
def peak_to_peak_ratio(x):
    return x.max() / x.min()

iris.groupby(iris.species).agg(peak_to_peak_ratio)

# describe 메서드를 사용하면 다양한 기술 통계(descriptive statistics)값을 한 번에 구한다.
iris.groupby(iris.species).describe().T


# apply 메서드를 사용하면 describe 메서드처럼 하나의 그룹에 대해
# 하나의 대표값(스칼라 값)을 구하는 게 아니라 데이터프레임을 만들 수 있다.
def top3_petal_length(df):
    return df.sort_values(by = 'petal_length', ascending = False)[:3]

iris.groupby(iris.species).apply(top3_petal_length)


# transform 메서드는 그룹별 대표값을 만드는 것이 아니라
# 그룹별 계산을 통해 데이터프레임 자체를 변화시킨다.
# 따라서 만들어진 데이터프레임의 크기는 원래 데이터프레임과 같다.
def q3cut(s):
    return pd.qcut(s, 3, labels = ['소', '중', '대'])

iris['petal_length_class'] = iris.groupby(iris.species)['petal_length'].transform(q3cut)
iris[['petal_length', 'petal_length_class']].tail(10)