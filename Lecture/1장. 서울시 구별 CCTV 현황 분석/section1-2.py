### section 1-2 (파이썬에서 텍스트 파일과 엑셀 파일 읽기 - pandas)
import pandas as pd

## csv 파일 일기: read_csv()

CCTV_Seoul = pd.read_csv('Lecture/Data/01. CCTV_in_Seoul.csv',
                         encoding = 'utf-8')       # 한글이 인코딩 되어 있을 때 옵션.
CCTV_Seoul.head()            # pandas 데이터의 첫 5행만 보여줌
CCTV_Seoul.columns           # pandas 데이터의 column의 이름들을 반환
CCTV_Seoul.columns[0]        # column 첫번째 이름 반환


# 이름 바꾸는 명령어: rename()

CCTV_Seoul.rename(columns = {CCTV_Seoul.columns[0] : '구별'}, inplace = True) # inplace=True 는 변수의 내용을 갱신하라는 의미
CCTV_Seoul.head()


## 엑셀 파일 읽기: read_excel()

pop_Seoul = pd.read_excel('Lecture/Data/01. population_in_Seoul.xls', encoding = 'utf-8')
pop_Seoul.head()

pop_Seoul = pd.read_excel('Lecture/Data/01. population_in_Seoul.xls',
                          header = 2,                         # 세번째 줄부터 읽음
                          parse_cols = 'B, D, G, J, N',       # B, D, G, J, N 열만 읽음
                          encoding = 'utf-8')
pop_Seoul.head()

pop_Seoul.rename(columns = {pop_Seoul.columns[0] : '구별',
                            pop_Seoul.columns[1] : '인구수',
                            pop_Seoul.columns[2] : '한국인',
                            pop_Seoul.columns[3] : '외국인',
                            pop_Seoul.columns[4] : '고령자'}, inplace = True)
pop_Seoul.head()


