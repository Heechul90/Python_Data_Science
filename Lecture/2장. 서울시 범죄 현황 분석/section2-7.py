### section 2-7 좀 더 편리한 시각화 도구 - Seaborn

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# sin 함수 그래프 그리기
x = np.linspace(0, 14, 100)
y1 = np.sin(x)
y2 = 2 * np.sin(x + 0.5)
y3 = 3 * np.sin(x + 1.0)
y4 = 4 * np.sin(x + 1.5)

plt.figure(figsize = (10, 6))
plt.plot(x, y1,
         x, y2,
         x, y3,
         x, y4)
plt.show()

# grid 스타일
# white
sns.set_style('white')

plt.figure(figsize = (10, 6))
plt.plot(x, y1,
         x, y2,
         x, y3,
         x, y4)
plt.show()

# whitegrid
sns.set_style('whitegrid')

plt.figure(figsize = (10, 6))
plt.plot(x, y1,
         x, y2,
         x, y3,
         x, y4)
plt.show()

# dark
sns.set_style('dark')

plt.figure(figsize = (10, 6))
plt.plot(x, y1,
         x, y2,
         x, y3,
         x, y4)
plt.show()

#######################
plt.figure(figsize = (10, 6))
plt.plot(x, y1,
         x, y2,
         x, y3,
         x, y4)
sns.despine(offset = 10)
plt.show()


# Seaborn의 여러가지 dataset
tips = sns.load_dataset('tips')
tips.head()

# 요일별 total_bill 박스 그래프
plt.figure(figsize = (10, 6))
sns.boxplot(x = 'day',
            y = 'total_bill',
            data = tips)
plt.show()

# hue 옵션을 이용해서 구분하기
plt.figure(figsize = (10, 6))
sns.boxplot(data = tips,
            x = 'day',
            y = 'total_bill',
            hue = 'smoker',      # smoker 로 구분
            palette = 'Set3')    # 색 지정
plt.show()

# swarmplot
plt.figure(figsize=(8,6))
sns.swarmplot(x = "day",
              y = "total_bill",
              data=tips,
              color=".5")
plt.show()

# boxplot, swarmplot 같이 그리기
plt.figure(figsize=(8,6))
sns.boxplot(x="day",
            y="total_bill",
            data=tips)
sns.swarmplot(x="day",
              y="total_bill",
              data=tips,
              color=".25")
plt.show()

# 스타일은 darkgrid하고 lmplot 그리기
sns.set_style("darkgrid")
sns.lmplot(x="total_bill",
           y="tip",
           data=tips,
           size=7)
plt.show()

# hue 옵션 사용하기
sns.lmplot(x="total_bill",
           y="tip",
           hue="smoker",
           data=tips, size=7)
plt.show()


sns.lmplot(x="total_bill",
           y="tip",
           hue="smoker",
           data=tips,
           palette="Set1",   # 색 지정
           size=15)          # 화면 크기 지정
plt.show()

# heatmap
uniform_data = np.random.rand(10, 12)
uniform_data

sns.heatmap(uniform_data)
plt.show()

# 범위 지정하기
sns.heatmap(uniform_data,
            vmin=0,          # 범위 최소값
            vmax=1)          # 범위 최대값
plt.show()

# flights 데이터 가져오기
flights = sns.load_dataset('flights')
flights = flights.pivot("month", "year", "passengers")
flights.head(5)

plt.figure(figsize=(10,8))
sns.heatmap(flights)
plt.show()

# 옵션 넣기
plt.figure(figsize=(10,8))
sns.heatmap(flights, annot=True, fmt="d")
plt.show()

# iris 데이터 불러오기
sns.set(style="ticks")
iris = sns.load_dataset("iris")
iris.head(10)

# pairplot
sns.pairplot(iris)
plt.show()

# hue 옵션으로 구분하기
sns.pairplot(iris, hue="species")
plt.show()

# value값 지정하기
sns.pairplot(iris, vars=["sepal_width", "sepal_length"])
plt.show()

# x값, y값 둘다 지정하기
sns.pairplot(iris, x_vars=["sepal_width", "sepal_length"],
             y_vars=["petal_width", "petal_length"])
plt.show()


# anscombe 데이터 불러오기
anscombe = sns.load_dataset("anscombe")
anscombe.head(5)

# lmplot
sns.set_style("darkgrid")

sns.lmplot(x="x",
           y="y",
           data=anscombe.query("dataset == 'I'"),
           ci=None,
           size=7)
plt.show()


sns.lmplot(x="x",
           y="y",
           data=anscombe.query("dataset == 'I'"),
           ci=None,
           scatter_kws={"s": 80},
           size=7)
plt.show()


sns.lmplot(x="x",
           y="y",
           data=anscombe.query("dataset == 'II'"),
           order=1,
           ci=None,
           scatter_kws={"s": 80},
           size=7)
plt.show()


sns.lmplot(x="x",
           y="y",
           data=anscombe.query("dataset == 'II'"),
           order=2,
           ci=None,
           scatter_kws={"s": 80},
           size=7)
plt.show()


sns.lmplot(x="x",
           y="y",
           data=anscombe.query("dataset == 'III'"),
           ci=None,
           scatter_kws={"s": 80},
           size=7)
plt.show()


sns.lmplot(x="x",
           y="y",
           data=anscombe.query("dataset == 'III'"),
           robust=True,
           ci=None,
           scatter_kws={"s": 80},
           size=7)
plt.show()