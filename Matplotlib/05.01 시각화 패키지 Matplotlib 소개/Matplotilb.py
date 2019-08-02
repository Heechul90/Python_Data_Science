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



# Matplotlib는 다음과 같은 정형화된 차트나 플롯 이외에도
# 저수준 api를 사용한 다양한 시각화 기능을 제공한다.

# 라인 플롯(line plot)
# 스캐터 플롯(scatter plot)
# 컨투어 플롯(contour plot)
# 서피스 플롯(surface plot)
# 바 차트(bar chart)
# 히스토그램(histogram)
# 박스 플롯(box plot)


# 한글 사용
mpl.rcParams['axes.unicode_minus'] = False # minus 표시

[(f.name, f.fname) for f in fm.fontManager.ttflist if 'Nanum' in f.name]

plt.rcParams['forn.family'] = 'Malgun Gothic'
plt.rcParams['font.size'] = 10


## pylab 서브패키지
## pylab 서브패키지는 matlab 이라는 수치해석 소프트웨어의 시각화 명령을 거의 그대로 사용할 수 있도록
##  Matplotlib 의 하위 API를 포장(wrapping)한 명령어 집합을 제공



## 라인 플롯
## 라인 플롯은 데이터가 시간, 순서 등에 따라 어떻게 변화하는지 보여주기 위해 사용한다.
## 명령은 pylab 서브패키지의 plot 명령을 사용
plt.title('Plot')
plt.plot([1, 4, 9, 16])
plt.show()

# x 축의 자료 위치 즉, 틱(tick)은 자동으로 0, 1, 2, 3 이 된다.
# 만약 이 x tick 위치를 별도로 명시하고 싶다면
# 다음과 같이 두 개의 같은 길이의 리스트 혹은 배열 자료를 넣는다
plt.title("x축의 tick 위치를 명시")
plt.plot([10, 20, 30, 40], [1, 4, 9, 16])
plt.show()


## 스타일 지정
# 플롯 명령어는 보는 사람이 그림을 더 알아보기 쉽게 하기 위해 다양한 스타일(style)을 지원
# plot 명령어에서는 다음과 같이 추가 문자열 인수를 사용하여 스타일을 지원
plt.title("'rs--' 스타일의 plot ")
plt.plot([10, 20, 30, 40], [1, 4, 9, 16], 'rs--')   # rs 스타일
plt.show()


## 색깔
## 스타일 문자열은 색깔(color), 마커(marker), 선 종류(line style)의 순서로 지정한다.

# 문자열	     약자
# blue	     b
# green	     g
# red        r
# cyan	     c
# magenta	 m
# yellow	 y
# black	     k
# white	     w


## 마커
## 이터 위치를 나타내는 기호를 마커(marker)라고 한다. 마커의 종류는 다음과 같다.

# 마커    문자열	의미
# .	     point marker
# ,	     pixel marker
# o	     circle marker
# v	     triangle_down marker
# ^	     triangle_up marker
# <	     triangle_left marker
# >      triangle_right marker
# 1	     tri_down marker
# 2	     tri_up marker
# 3	     tri_left marker
# 4      tri_right marker
# s      square marker
# p      pentagon marker
# *      star marker
# h	     hexagon1 marker
# H	     hexagon2 marker
# +	     plus marker
# x      x marker
# D	     diamond marker
# d	     thin_diamond marker


## 선 스타일
## 선 스타일에는 실선(solid), 대시선(dashed), 점선(dotted), 대시-점선(dash-dit) 이 있다

# 선 스타일 문자열	   의미
# -	               solid line style
# --	           dashed line style
# -.	           dash-dot line style
# :	               dotted line style


## 기타 스타일
## 라인 플롯에서는 앞서 설명한 세 가지 스타일 이외에도 여러가지 스타일을 지정할 수 있지만
## 이 경우에는 인수 이름을 정확하게 지정해야 한다.

# 스타일 문자열	     약자	    의미
# color	             c	        선 색깔
# linewidth	         lw	        선 굵기
# linestyle	         ls	        선 스타일
# marker		                마커 종류
# markersize	     ms	        마커 크기
# markeredgecolor	 mec     	마커 선 색깔
# markeredgewidth	 mew	    마커 선 굵기
# markerfacecolor	 mfc	    마커 내부 색깔

plt.plot([10, 20, 30, 40], [1, 4, 9, 16],
         c="b",                # 선 색깔
         lw=5,                 # 선 굵기
         ls="--",              # 선 스타일
         marker="o",           # 마커
         ms=15,                # 마커 크기
         mec="g",              # 마커 선 색깔
         mew=5,                # 마커 선 굵기
         mfc="r")              # 마커 내부 색깔
plt.title("스타일 적용 예")
plt.show()


## 그림 범위 지정
## 그림의 범위를 수동으로 지정하려면 xlim 명령과 ylim 명령을 사용한다.
## 이 명령들은 그림의 범위가 되는 x축, y축의 최소값과 최대값을 지정한다.
plt.title("x축, y축의 범위 설정")
plt.plot([10, 20, 30, 40], [1, 4, 9, 16],
         c="b",
         lw=5,
         ls="--",
         marker="o",
         ms=15,
         mec="g",
         mew=5,
         mfc="r")
plt.xlim(0, 50)
plt.ylim(-10, 30)
plt.show()


## 틱 설정
## 플롯이나 차트에서 축상의 위치 표시 지점을 틱(tick)이라고 하고
## 이 틱에 써진 숫자 혹은 글자를 틱 라벨(tick label)이라고 한다.
## 틱의 위치나 틱 라벨은 Matplotlib가 자동으로 정해주지만 만약 수동으로 설정하고 싶다면
## xticks 명령이나 yticks 명령을 사용한다.
X = np.linspace(-np.pi, np.pi, 256)                    # -pi부터 pi까지 256으로 나눠라
C = np.cos(X)
plt.title("x축과 y축의 tick label 설정")
plt.plot(X, C)
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi])
plt.yticks([-1, 0, +1])
plt.show()

# 틱 라벨 문자열에는 $$ 사이에 LaTeX 수학 문자식을 넣을 수도 있다
X = np.linspace(-np.pi, np.pi, 256)
C = np.cos(X)
plt.title("LaTeX, 문자열로 tick label 정의")
plt.plot(X, C)
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1, 0, 1], ["Low", "Zero", "High"])
plt.show()


## 그리드 설정
## 그리드를 사용하지 않으려면 grid(False) 명령을 사용한다.
## 다시 그리드를 사용하려면 grid(True)를 사용한다.
X = np.linspace(-np.pi, np.pi, 256)
C = np.cos(X)
plt.title("Grid ")
plt.plot(X, C)
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1, 0, 1], ["Low", "Zero", "High"])
plt.grid(True)
plt.show()


## 여러개의 선을 그리기
## 라인 플롯에서 선을 하나가 아니라 여러개를 그리고 싶은 경우에는
## x 데이터, y 데이터, 스타일 문자열을 반복하여 인수로 넘긴다.
## 이 경우에는 하나의 선을 그릴 때 처럼 x 데이터나 스타일 문자열을 생략할 수 없다.
t = np.arange(0., 5., 0.2)
plt.title("라인 플롯에서 여러개의 선 그리기")
plt.plot(t, t, 'r--',
         t, 0.5 * t**2, 'bs:',
         t, 0.2 * t**3, 'g^-')
plt.show()


## 홀드 명령
## 하나의 plot 명령이 아니라 복수의 plot 명령을 하나의 그림에 겹쳐서 그릴 수도 있다.
## Matplotlib 1.5까지는 hold(True) 명령을 이용하여 기존의 그림 위에 겹쳐 그리도록 하였다.
## 겹치기를 종료하는 것은 hold(False) 명령이다.
## Matplotlib 2.0부터는 모든 플롯 명령에 hold(True)가 자동 적용된다.
plt.title("복수의 plot 명령을 한 그림에서 표현")
plt.plot([1, 4, 9, 16],
         c="b",
         lw=5,
         ls="--",
         marker="o",
         ms=15,
         mec="g",
         mew=5,
         mfc="r")
# plt.hold(True)           # <- 1,5 버전에서는 이 코드가 필요하다.
plt.plot([9, 16, 4, 1],
         c="k",
         lw=3,
         ls=":",
         marker="s",
         ms=10,
         mec="m",
         mew=5,
         mfc="c")
# plt.hold(False)          # <- 1,5 버전에서는 이 코드가 필요하다.
plt.show()


## 범례
## 여러개의 라인 플롯을 동시에 그리는 경우에는 각 선이 무슨 자료를 표시하는지를 보여주기 위해
## legend 명령으로 범례(legend)를 추가할 수 있다.
## 범례의 위치는 자동으로 정해지지만 수동으로 설정하고 싶으면 loc 인수를 사용한다.

# loc 문자열	     숫자
# best	         0
# upper right	 1
# upper left	 2
# lower left	 3
# lower right	 4
# right	         5
# center left	 6
# center right	 7
# lower center	 8
# upper center	 9
# center	     10

X = np.linspace(-np.pi, np.pi, 256)
C, S = np.cos(X), np.sin(X)
plt.title("legend를 표시한 플롯")
plt.plot(X, C, ls="--", label="cosine")
plt.plot(X, S, ls=":", label="sine")
plt.legend(loc=2)                       # 옵션을 주지않으면 가장 좋은 자리에 들어간다
plt.show()


## x축, y축 라벨, 타이틀
## 라벨을 붙이려면 xlabel. ylabel 명령을 사용한다.
## 또 플롯의 위에는 title 명령으로 제목(title)을 붙일 수 있다.
X = np.linspace(-np.pi, np.pi, 256)
C, S = np.cos(X), np.sin(X)
plt.plot(X, C, label="cosine")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.title("Cosine Plot")
plt.show()






