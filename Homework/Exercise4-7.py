import pandas as pd
import numpy as np


## 연습 문제 1
## key1의 값을 기준으로 data1의 값을 분류하여 합계를 구한 결과를 시리즈가 아닌 데이터프레임으로 구한다.
np.random.seed(0)
df2 = pd.DataFrame({
    'key1': ['A', 'A', 'B', 'B', 'A'],
    'key2': ['one', 'two', 'one', 'two', 'one'],
    'data1': [1, 2, 3, 4, 5],
    'data2': [10, 20, 30, 40, 50]
})
df2




## 연습 문제 2
## 붓꽃(iris) 데이터에서 붓꽃 종(species)별로
## 꽃잎길이(sepal_length), 꽃잎폭(sepal_width) 등의 평균을 구하라.
## 만약 붓꽃 종(species)이 표시되지 않았을 때
## 이 수치들을 이용하여 붓꽃 종을 찾아낼 수 있을지 생각하라.
import seaborn as sns
iris = sns.load_dataset("iris")

