### Exercise 4-7

import pandas as pd
import numpy as np


## 연습 문제 1
## key1의 값을 기준으로 data1의 값을 분류하여
## 합계를 구한 결과를 시리즈가 아닌 데이터프레임으로 구한다.
np.random.seed(0)
df2 = pd.DataFrame({
    'key1': ['A', 'A', 'B', 'B', 'A'],
    'key2': ['one', 'two', 'one', 'two', 'one'],
    'data1': [1, 2, 3, 4, 5],
    'data2': [10, 20, 30, 40, 50]})
df2

df2.groupby(df2.key1)[['data1']].sum()




## 연습 문제 2
## 붓꽃(iris) 데이터에서 붓꽃 종(species)별로
## 꽃잎길이(sepal_length), 꽃잎폭(sepal_width) 등의 평균을 구하라.
## 만약 붓꽃 종(species)이 표시되지 않았을 때
## 이 수치들을 이용하여 붓꽃 종을 찾아낼 수 있을지 생각하라.
import seaborn as sns
iris = sns.load_dataset("iris")
iris.groupby(iris.species)[['sepal_length', 'sepal_width']].mean()




## 연습 문제 3
import seaborn as sns

tips = sns.load_dataset('tips')
tips['tip_pct'] = (tips['tip'] / tips['total_bill'] * 100).round(2)

# 1. 팁의 비율이 요일과 점심/저녁 여부, 인원수에 어떤 영향을 받는지 살펴본다.
tips.pivot_table('tip_pct',
                 index = 'day')

tips.pivot_table('tip_pct',
                 index = 'time')

tips.pivot_table('tip_pct',
                 index = 'size')




# 2. 어떤 요인이 가장 크게 작용하는지 판단할 수 있는 방법이 있는가?
tips.groupby(['day', 'time', 'size'])[['tip_pct']].describe()
# day = Sat
# time = Dinner
# size = 1
# tip_pct = 0.231832




## 연습 문제 4
## 타이타닉 승객 데이터를 이용하여 다음 분석을 실시하라. 데이터는 다음과 같이 받을 수 있다.
import seaborn as sns

titanic = sns.load_dataset("titanic")

# 1. qcut 명령으로 세 개의 나이 그룹을 만든다.
titanic['age_group'] = pd.qcut(titanic['age'], 3, labels = ['청소년', '어른', '노인'])


# 2. 성별, 선실, 나이 그룹에 의한 생존율을 데이터프레임으로 계산한다.
#    행에는 성별 및 나이 그룹에 대한 다중 인덱스를 사용하고 열에는 선실 인덱스를 사용한다.
titanic.pivot_table(values = 'survived',
                    index = ['sex', 'class'],
                    columns = 'age_group',
                    aggfunc = 'mean')

# 3. 성별 및 선실에 의한 생존율을 피봇 데이터 형태로 만든다.
titanic.pivot_table(values = 'survived',
                    index = 'sex',
                    columns = 'class',
                    aggfunc = 'mean')
