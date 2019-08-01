### section 1-8 (CCTV 현황 그래프로 분석하기)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## matplotlib는 한글을 지원하지 않기 때문에
## matplotlib의 폰트를 변경할 필요가 있다
import platform

from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')



#################### 데이터 만들기####################
## CCTV 현황
CCTV_Seoul = pd.read_csv('Lecture/Data/01. CCTV_in_Seoul.csv',
                         encoding = 'utf-8')
CCTV_Seoul.rename(columns = {CCTV_Seoul.columns[0]: '구별'}, inplace = True)

CCTV_Seoul['최근증가율'] = (CCTV_Seoul['2016년'] + CCTV_Seoul['2015년'] + CCTV_Seoul['2014년']) \
                      / CCTV_Seoul['2013년도 이전'] * 100

CCTV_Seoul.head(5)


## 서울시 인구 현활
pop_Seoul = pd.read_excel('Lecture/Data/01. population_in_Seoul.xls',
                          header = 2,
                          parse_cols = 'B, D, G, J, N',
                          encoding = 'utf-8')

pop_Seoul.rename(columns = {pop_Seoul.columns[0] : '구별',
                            pop_Seoul.columns[1] : '인구수',
                            pop_Seoul.columns[2] : '한국인',
                            pop_Seoul.columns[3] : '외국인',
                            pop_Seoul.columns[4] : '고령자'}, inplace = True)

pop_Seoul.drop([0], inplace = True)
pop_Seoul['구별'].unique()
pop_Seoul[pop_Seoul['구별'].isnull()]
pop_Seoul.drop([26], inplace = True)
pop_Seoul['구별'].unique()

pop_Seoul['외국인비율'] = pop_Seoul['외국인'] / pop_Seoul['인구수'] * 100
pop_Seoul['고령자비율'] = pop_Seoul['고령자'] / pop_Seoul['인구수'] * 100

pop_Seoul.head()



## merge 명령으로 합치기
data_result = pd.merge(CCTV_Seoul, pop_Seoul, on = '구별')
data_result.head()

# 의미 없는 열 지우기
# 행 지우기는 drop, 열 지우기는 del
del data_result['2013년도 이전']
del data_result['2014년']
del data_result['2015년']
del data_result['2016년']
data_result.head()


# 구별을 index로 지정하기
data_result.set_index('구별', inplace = True)     # 구별을 index로 지정
data_result.head()
###################################################

## 그래프 그리기
data_result['소계'].plot(kind = 'barh',           # 수평바로 지정
                       grid = True,              # grid 그리기
                       figsize = (10, 10))       # 그림 크기 지정
plt.show()


# 정렬해서 그래프 그리기
data_result['소계'].sort_values().plot(kind='barh',    # values로 정렬하기
                                     grid=True,
                                     figsize=(10,10))
plt.show()


# 인구 대비 CCTV 비율을 계산해서 정렬
data_result['CCTV비율'] = data_result['소계'] / data_result['인구수'] * 100
data_result.columns
data_result['CCTV비율'].sort_values().plot(kind = 'barh',
                                         grid = True,
                                         figsize = (10, 10))


# scatter 명령으로 그래프 그리기
plt.figure(figsize = (10, 10))
plt.scatter(data_result['인구수'], data_result['소계'], s = 50)   # s는 marker 크기
plt.xlabel('인구수')
plt.ylabel('CCTV')
plt.grid()
plt.show()

# 그래프에 직선 하나 그리기
# numpy의 polyfit 명령으로 직선 만들기
# x 축은 linspace
# y 축은 poly1d
fp1 = np.polyfit(data_result['인구수'], data_result['소계'], 1)
fp1

f1 = np.poly1d(fp1)
fx = np.linspace(100000, 700000, 700)

plt.figure(figsize = (10, 10))
plt.scatter(data_result['인구수'], data_result['소계'], s = 50)
plt.plot(fx, f1(fx), ls = 'dashed', lw = 3, color = 'g')
plt.xlabel('인구수')
plt.ylabel('CCTV')
plt.grid()
plt.show()


# 조금더 설득력 있는 자료 만들기(이름 text, color map 추가하기)
# 오차를 계산할 코드를 만들고 오차가 큰 순으로 데이터를 정렬
fp1 = np.polyfit(data_result['인구수'], data_result['소계'], 1)

f1 = np.poly1d(fp1)
fx = np.linspace(100000, 700000, 100)

data_result['오차'] = np.abs(data_result['소계'] - f1(data_result['인구수']))

df_sort = data_result.sort_values(by='오차', ascending=False)
df_sort.head()

# 그래프 그리기
plt.figure(figsize = (14, 10))
plt.scatter(data_result['인구수'], data_result['소계'],
            c = data_result['오차'],         # color map 지정
            s = 50)                        # marker 크기 지정
plt.plot(fx, f1(fx),
         ls = 'dashed',                     # linestyle 지정
         lw = 3,                           # 라인 굵기 지정
         color = 'g')                      # 색상 지정

for n in range(10):
    plt.text(df_sort['인구수'][n] * 1.02, df_sort['소계'][n] * 0.98,
             df_sort.index[n], fontsize = 15)

plt.xlabel('인구수')
plt.ylabel('인구당비율')
plt.colorbar()
plt.grid()
plt.show()