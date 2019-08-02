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


## 한글 사용
## Matplotlib에서 한글을 사용하려면 다음과 같이 한글 폰트를 적용해야 한다.
## 당연히 해당 폰트는 컴퓨터에 깔려 있어야 한다.

# 폰트를 설치한 후에는 다음 명령으로 원하는 폰트가 설치되어 있는지 확인한다.
set(sorted([f.name for f in mpl.font_manager.fontManager.ttflist]))

# 설치된 폰트를 사용하는 방법은 크게 두가지 이다.

# rc parameter 설정으로 이후의 그림 전체에 적용
# 인수를 사용하여 개별 텍스트 관련 명령에만 적용

# 한글 문자열은 항상 유니코드를 사용해야 한다.

# 우선 rc parameter를 설정하여 이후의 그림 전체에 적용해 보자
mpl.rc('font', family='nanumgothic')
mpl.rc('axes', unicode_minus=False)

plt.title('한글 제목')
plt.plot(X, C, label="코사인")
t = 2 * np.pi / 3
plt.scatter(t, np.cos(t), 50, color='blue')
plt.xlabel("엑스축 라벨")
plt.ylabel("와이축 라벨")
plt.annotate("여기가 0.5!",
             xy=(t, np.cos(t)), xycoords='data', xytext=(-90, -50),
             textcoords='offset points',
             fontsize=16, arrowprops=dict(arrowstyle="->"))
plt.show()

# 만약 개별적으로 폰트를 적용하고 싶을 때는
# 다음과 같이 폰트 패밀리, 색상, 크기를 정하여 플롯 명령의 fontdict 인수에 넣는다.
font1 = {'family': 'NanumMyeongjo', 'color':  'black', 'size': 24}
font2 = {'family': 'NanumBarunpen',
         'color':  'darkred', 'weight': 'bold', 'size': 18}
font3 = {'family': 'NanumBarunGothic',
         'color':  'blue', 'weight': 'light', 'size': 12}

x = np.linspace(0.0, 5.0, 100)
y = np.cos(2 * np.pi * x) * np.exp(-x)

plt.plot(x, y, 'k')
plt.title('한글 제목', fontdict=font1)
plt.xlabel('엑스 축', fontdict=font2)
plt.ylabel('와이 축', fontdict=font3)
plt.subplots_adjust()
plt.show()