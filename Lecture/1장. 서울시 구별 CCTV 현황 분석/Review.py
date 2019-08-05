### 1. Basic of Python, Pandas and Matplotlib via analysis of CCTV in Seoul - Review

# 패키지, 모듈, 함수 준비하기
import pandas as pd
import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt

# 한글 사용하기
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


## 1. 데이터 불러오기
cctv_seoul = pd.read_csv('Lecture/Data/01. CCTV_in_Seoul.csv',
                         encoding = 'utf-8')

cctv_seoul.rename(columns = {cctv_seoul.columns[0]: '구별'},
                  inplace = True)
cctv_seoul.head()


pop_seoul = pd.read_excel('Lecture/Data/01. population_in_Seoul.xls',
                          encoding = 'utf-8',                   # 인코딩
                          header = 2,                           # 첫 두줄 생략
                          usecols = 'B, D, G, J, N')            # 원하는 컬럼만 가져오기
pop_seoul.rename(columns = {pop_seoul.columns[0]: '구별',        # 0번째 컬럼
                            pop_seoul.columns[1]: '인구수',      # 1번째 컬럼
                            pop_seoul.columns[2]: '한국인',      # 2번째 컬럼
                            pop_seoul.columns[3]: '외국인',      # 3번째 컬럼
                            pop_seoul.columns[4]: '고령자',},    # 4번째 컬럼
                 inplace = True)

pop_seoul.head()


## 2. 데이터 파악하기
## CCTV 데이터 파악하기
cctv_seoul.head()
cctv_seoul.sort_values(by = '소계',                     # 소계를 정령
                       ascending = False,).head(5)     # 내림차순으로 정렬

cctv_seoul.sort_values(by = '소계',                     # 소계를 정령
                       ascending = True,).head(5)      # 오름차순으로 정렬

# 최근증가율 컬럼 만들기(2016+2015+2014/2013이전*100)
cctv_seoul['최근증가율'] = (cctv_seoul['2016년'] + \
                          cctv_seoul['2015년'] + \
                          cctv_seoul['2014년'] / \
                          cctv_seoul['2013년도 이전']) * 100
cctv_seoul.head()


## pop_seoul 데이터 파악하기
pop_seoul.head()

# 필요없는 행 삭제하기
pop_seoul.drop([0],                      # 첫 행 삭제하기
               inplace = True)

# unique로 반복된 데이터를 하나로 나타내서 한 번 이상 나타난 데이터를 확인
pop_seoul['구별'].unique                 # NaN 발견
pop_seoul[pop_seoul['구별'].isnull()]    # NaN이 어디에 있는지 알아내기
pop_seoul.drop([26], inplace = True)    # NaN 행 삭제
pop_seoul['구별'].unique                 # 삭제되었는지 확인


## 외국인비율, 고령자비율 컬럼 만들기(외국인/인구수*100)
pop_seoul['외국인비율'] = pop_seoul['외국인'] / pop_seoul['인구수'] * 100
pop_seoul['고령자비율'] = pop_seoul['고령자'] / pop_seoul['인구수'] * 100
pop_seoul.head()

# 인구수로 내림차순 정렬하기
pop_seoul.sort_values(by = '인구수', ascending = False).head()

# 외국인으로 내림차순 정렬하기
pop_seoul.sort_values(by = '외국인', ascending = False).head()

# 외국인비율로 내림차순 정렬하기
pop_seoul.sort_values(by = '외국인비율', ascending = False).head()

# 고령자로 내림차순 정렬하기
pop_seoul.sort_values(by = '고령자', ascending = False).head()

# 고령자비율로 내림차순 정렬하기
pop_seoul.sort_values(by = '고령자비율', ascending = False).head()


## 3. CCTV 데이터와 인구 데이터 합치고 분석하기
data_result = pd.merge(cctv_seoul, pop_seoul,    # 두 데이터 합치기
                       on = '구별')               # 기준은 '구별'

data_result.columns
data_result.head()

# 2013년도 이전, 2014년, 2015년, 2016년 컬럼 삭제하기
del data_result['2013년도 이전']
del data_result['2014년']
del data_result['2015년']
del data_result['2016년']
data_result.head()

# '구별'을 index.name으로 설정하기
data_result.set_index('구별', inplace = True)
data_result.head()

# 상관계수 구하기: np.corrcoef
np.corrcoef([data_result['고령자비율'], data_result['소계']])
np.corrcoef([data_result['외국인비율'], data_result['소계']])
np.corrcoef([data_result['인구수'], data_result['소계']])

# 인구수와 소계의 상관계수가 0.3이므로 약한 상관관계가 있다
# 인구수와 소계를 좀더 알아보자
# 소계로 내림차순 정렬하기
data_result.sort_values(by = '소계', ascending = False).head()

# 인구수로 내림차순 정렬하기
data_result.sort_values(by = '인구수', ascending = False).head()


## 4. CCTV와 인구현황 그래프로 분석하기
# 소계로 그래프 그리기
plt.figure(figsize = (10, 10))
data_result['소계'].plot(kind = 'barh', grid = True)
plt.show()

# 소계를 내림차순으로 정렬해서 그래프 그리기
plt.figure(figsize = (10, 10))
data_result['소계'].sort_values().plot(kind = 'barh', grid = True)
plt.show()

# CCTV비율 만들고 정렬해서 그래프 그려보기
data_result['CCTV비율'] = data_result['소계'] / data_result['인구수'] * 100
data_result['CCTV비율'].sort_values().plot(kind = 'barh', grid = True, figsize = (10, 10))

# 인구수와 소계의 점선도 그리기
plt.scatter(data_result['인구수'], data_result['소계'], s=50)
plt.xlabel('인구수')
plt.ylabel('CCTV')
plt.grid()
plt.show()

# 직선 추가하기
# 선형 회귀식
fp1 = np.polyfit(data_result['인구수'], data_result['소계'], 1)    # 기울기 , y절편
fp1

f1 = np.poly1d(fp1)
fx = np.linspace(100000, 700000, 100)

plt.figure(figsize=(10,10))
plt.scatter(data_result['인구수'], data_result['소계'], s=50)
plt.plot(fx, f1(fx), ls='dashed', lw=3, color='g')
plt.xlabel('인구수')
plt.ylabel('CCTV')
plt.grid()

plt.show()


## 5. 조금더 설득력 있는 자료 만들기
fp1 = np.polyfit(data_result['인구수'], data_result['소계'], 1)

f1 = np.poly1d(fp1)
fx = np.linspace(100000, 700000, 100)

# 오차 컬럼 만들기(오차 = 소계 - 인구수)
data_result['오차'] = np.abs(data_result['소계'] - f1(data_result['인구수']))
df_sort = data_result.sort_values(by='오차', ascending=False)
df_sort.head()

# 그래프 그리기
plt.figure(figsize=(14, 10))
plt.scatter(data_result['인구수'], data_result['소계'],
            c=data_result['오차'], s=50)
plt.plot(fx, f1(fx), ls='dashed', lw=3, color='g')

for i in range(10):
    plt.text(df_sort['인구수'][i] * 1.02,      # x축 위치
             df_sort['소계'][i] * 0.98,        # y축 위치
             df_sort.index[i],                #label 이름
             fontsize=15)                     # label 크기

plt.xlabel('인구수')
plt.ylabel('인구당비율')
plt.colorbar()
plt.grid()
plt.show()