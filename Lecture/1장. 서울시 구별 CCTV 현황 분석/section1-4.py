### section 1-4 (pandas 이용해서 CCTV와 인구 현황 데이터 파악하기)
import pandas as pd
import numpy as np

CCTV_Seoul = pd.read_csv('Lecture/Data/01. CCTV_in_Seoul.csv',
                         encoding = 'utf-8')
CCTV_Seoul.head()
CCTV_Seoul.rename(columns = {CCTV_Seoul.columns[0] : '구별'}, inplace = True)
CCTV_Seoul.head()


# 정렬하기
CCTV_Seoul.sort_values(by = '소계', ascending = True).head(5)
CCTV_Seoul.sort_values(by = '소계', ascending = False).head(5)


# 최근 3년간 CCTV 증가율 계산
CCTV_Seoul['최근증가율'] = (CCTV_Seoul['2016년'] + CCTV_Seoul['2015년'] + CCTV_Seoul['2014년']) \
                      / CCTV_Seoul['2013년도 이전'] * 100

CCTV_Seoul.sort_values(by = '최근증가율', ascending = False).head(5)


# 서울시 인원 현황
pop_Seoul = pd.read_excel('Lecture/Data/01. population_in_Seoul.xls',
                          header = 2,
                          parse_cols = 'B, D, G, J, N',
                          encoding = 'utf-8')
pop_Seoul.head()
pop_Seoul.rename(columns = {pop_Seoul.columns[0] : '구별',
                            pop_Seoul.columns[1] : '인구수',
                            pop_Seoul.columns[2] : '한국인',
                            pop_Seoul.columns[3] : '외국인',
                            pop_Seoul.columns[4] : '고령자'}, inplace = True)
pop_Seoul.head()


# drop 명령어를 사용하여 행을 삭제
pop_Seoul.drop([0], inplace = True)
pop_Seoul.head()

# 데이터의 '구별' 컬럼의 unique를 조사
pop_Seoul['구별'].unique()

# isnull 명령으로 NaN 데이터 추출
pop_Seoul[pop_Seoul['구별'].isnull()]

# drop 명령으로 26번째 행 삭제
pop_Seoul.drop([26], inplace = True)
pop_Seoul['구별'].unique()

# '외국인비율'과 '고령자비율' 추가하기
pop_Seoul['외국인비율'] = pop_Seoul['외국인'] / pop_Seoul['인구수'] * 100
pop_Seoul['고령자비율'] = pop_Seoul['고령자'] / pop_Seoul['인구수'] * 100
pop_Seoul.head()

# 인구수로 내림차순정렬
pop_Seoul.sort_values(by = '인구수', ascending = False).head(5)

# 외국인으로 내림차순정렬
pop_Seoul.sort_values(by = '외국인', ascending = False).head(5)

# 외국인비율로 내림차순정렬
pop_Seoul.sort_values(by = '외국인비율', ascending = False).head(5)

# 고령자로 내림차순정렬
pop_Seoul.sort_values(by = '고령자', ascending = False).head(5)

# 고령자비율로 내림차순정렬
pop_Seoul.sort_values(by = '고령자비율', ascending = False).head(5)