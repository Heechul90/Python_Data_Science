### 시각화 패키지 Matplotlib 소개

# 모듈 준비하기
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import pandas as pd

# 한글 사용하기(둘 중 하나)
mpl.reParams['axes.unicode_minus'] = False
[(f.namn f.fname) for f in fm.fontManager.ttflist if 'Malgun' in f.name]

plt.rcParams["font.family"] = 'NanumBarunGothic'
plt.rcParams["font.size"] = 10


## 그림의 구조
## Matplotlib가 그리는 그림은 Figure 객체, Axes 객체, Axis 객체 등으로 구성된다.
## Figure 객체는 한 개 이상의 Axes 객체를 포함하고
## Axes 객체는 다시 두 개 이상의 Axis 객체를 포함한다.


## Figure 객체
## figure 명령을 명시적으로 사용하는 경우는
## 여러개의 윈도우를 동시에 띄워야 하거나(line plot이 아닌 경우),
## Jupyter 노트북 등에서(line plot의 경우) 그림의 크기를 설정하고 싶을 때이다.
## 그림의 크기는 figsize 인수로 설정한다.
np.random.seed(0)
f1 = plt.figure(figsize=(10, 2))
plt.title("figure size : (10, 2)")
plt.plot(np.random.randn(100))
plt.show()

# 현재 사용하고 있는 Figure 객체를 얻으려면(다른 변수에 할당할 수도 있다.) gcf 명령을 사용한다.
f1 = plt.figure(1)
plt.title("현재의 Figure 객체")
plt.plot([1, 2, 3, 4], 'ro:')

f2 = plt.gcf()
print(f1, id(f1))
print(f2, id(f2))
plt.show()


## Axes 객체와 subplot 명령
## Figure 안에 Axes를 생성하려면 원래 subplot 명령을 사용하여 명시적으로 Axes 객체를 얻어야 한다.
## subplot 명령은 세개의 인수를 가지는데
## 처음 두개의 원소가 전체 그리드 행렬의 모양을 지시하는 두 숫자이고
## 세번째 인수가 네 개 중 어느것인지를 의미하는 숫자이다.

subplot(2, 1, 1)     # 여기에서 윗부분에 그릴 플롯 명령 실행
subplot(2, 1, 2)     # 여기에서 아랫부분에 그릴 플롯 명령 실행

# tight_layout 명령을 실행하면 플롯간의 간격을 자동으로 맞춰준다.
x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)
y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

ax1 = plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'yo-')
plt.title('A tale of 2 subplots')
plt.ylabel('Damped oscillation')
print(ax1)

ax2 = plt.subplot(2, 1, 2)
plt.plot(x2, y2, 'r.-')
plt.xlabel('time (s)')
plt.ylabel('Undamped')
print(ax2)

plt.tight_layout()
plt.show()

# 만약 2x2 형태의 네 개의 플롯이라면 다음과 같이 그린다.
# 이 때 subplot 의 인수는 (2,2,1)를 줄여서 221 라는 하나의 숫자로 표시할 수도 있다.
# Axes의 위치는 위에서 부터 아래로, 왼쪽에서 오른쪽으로 카운트한다.
np.random.seed(0)

plt.subplot(221)
plt.plot(np.random.rand(5))
plt.title("axes 1")

plt.subplot(222)
plt.plot(np.random.rand(5))
plt.title("axes 2")

plt.subplot(223)
plt.plot(np.random.rand(5))
plt.title("axes 3")

plt.subplot(224)
plt.plot(np.random.rand(5))
plt.title("axes 4")

plt.tight_layout()
plt.show()

# subplots 명령으로 복수의 Axes 객체를 동시에 생성할 수도 있다.
# 이때는 2차원 ndarray 형태로 Axes 객체가 반환된다.
fig, axes = plt.subplots(2, 2)

np.random.seed(0)
axes[0, 0].plot(np.random.rand(5))
axes[0, 0].set_title("axes 1")
axes[0, 1].plot(np.random.rand(5))
axes[0, 1].set_title("axes 2")
axes[1, 0].plot(np.random.rand(5))
axes[1, 0].set_title("axes 3")
axes[1, 1].plot(np.random.rand(5))
axes[1, 1].set_title("axes 4")

plt.tight_layout()
plt.show()


## Axis 객체와 축
## 하나의 Axes 객체는 두 개 이상의 Axis 객체를 가진다.
## Axis 객체는 플롯의 가로축이나 세로축을 나타내는 객체이다.

# 여러가지 플롯을 하나의 Axes 객체에 표시할 때 y값의 크기가 달라서 표시하기 힘든 경우가 있다.
# 이 때는 다음처럼 twinx 명령으로 대해 복수의 y 축을 가진 플롯을 만들수도 있다.
# twinx 명령은 x 축을 공유하는 새로운 Axes 객체를 만든다.
fig, ax0 = plt.subplots()
ax1 = ax0.twinx()
ax0.set_title("2개의 y축 한 figure에서 사용하기")
ax0.plot([10, 5, 2, 9, 7], 'r-', label="y0")
ax0.set_ylabel("y0")
ax0.grid(False)
ax1.plot([100, 200, 220, 180, 120], 'g:', label="y1")
ax1.set_ylabel("y1")
ax1.grid(False)
ax0.set_xlabel("공유되는 x축")
plt.show()