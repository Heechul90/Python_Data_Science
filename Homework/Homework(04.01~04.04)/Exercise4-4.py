### Exercise 4-4

import pandas as pd
import numpy as np


## 연습 문제 4.2.5
## 다음 명령으로 타이타닉호 승객 데이터를 데이터프레임으로 읽어온다.
## 이 명령을 실행하려면 seaborn 패키지가 설치되어 있어야 한다.
import seaborn as sns
titanic = sns.load_dataset("titanic")


## 타이타닉호 승객 데이터의 데이터 값을 각 열마다 구해본다.
titanic.columns
titanic.head()

titanic['survived']
titanic['pclass']
titanic['sex']
titanic.iloc[:,3]
titanic.iloc[:,4]
titanic.iloc[:,5]
titanic.iloc[:,6]
titanic.iloc[:,7]
titanic.iloc[:,8]
titanic['who']
titanic.iloc[:,10]
titanic['deck']
titanic.iloc[:,12]




## 연습 문제 4.2.6
## 타이타닉호 승객중 성별(sex) 인원수,
titanic.columns
titanic.head()
titanic.groupby('sex').size()


## 나이별(age) 인원수,
titanic.groupby('age').size()

## 선실별(class) 인원수,
titanic.groupby('class').size()

## 사망/생존(alive) 인원수를 구하라.
titanic.groupby('alive').size()





## 연습 문제 4.2.7

bins = [1, 15, 25, 35, 60, 99]
labels = ["미성년자", "청년", "중년", "장년", "노년"]

## 타이타닉호 승객을 사망자와 생존자 그룹으로 나누고
## 각 그룹에 대해
## '미성년자', '청년', '중년', '장년', '노년' 승객의 비율을 구한다.
## 각 그룹 별로 비율의 전체 합은 1이 되어야 한다.

titanic['group_age'] = pd.cut(titanic['age'], bins, labels = labels)

g_titanic = titanic.groupby(['alive', 'group_age']).count()[['survived']]

g_titanic['group_age_pct'] = g_titanic['survived']/ g_titanic['survived'].sum() * 100

