### section 1-6 (CCTV 데이터와 인구 현황 데이터를 합치고 분석하기)
import pandas as pd
import numpy as np

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

# 상과계수의 절대값이 클수록 데이터는 관계가 있다
# 절대값이 0.1 이하면 거의 무시
# 절대값이 0.3 이하면 약한 상관관계
# 절대값이 0.7 이하면 뚜렷한 상관관계
# 상과계수 구하는 명령어: corrcoef

np.corrcoef(data_result['고령자비율'], data_result['소계'])
np.corrcoef(data_result['외국인비율'],data_result['소계'])
np.corrcoef(data_result['인구수'], data_result['소계'])


# 인구수와 상관계수가 0.3이어서 약한 상관관계가 있다.
data_result.sort_values(by = '소계', ascending = False).head(5)
data_result.sort_values(by = '인구수', ascending = False).head(5)