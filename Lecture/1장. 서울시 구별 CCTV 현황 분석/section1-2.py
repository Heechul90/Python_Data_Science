### section 1-2 (파이썬에서 텍스트 파일과 엑셀 파일 읽기 - pandas
import pandas as pd

CCTV_Seoul = pd.read_csv('Lecture/Data/01. CCTV_in_Seoul.csv', encoding = 'utf-8')
CCTV_Seoul.head()
CCTV_Seoul.columns
CCTV_Seoul.columns[0]

CCTV_Seoul.rename(columns = {CCTV_Seoul.columns[0] : '구별'}, inplace = True)
CCTV_Seoul.head()

pop_Seoul = pd.read.excel('Lecture/Data/01. population_in_Seoul.xls', encoding = 'utf-8')

