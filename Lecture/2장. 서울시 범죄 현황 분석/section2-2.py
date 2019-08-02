### section 2-2 (Pandas를 이용하여 데이터 정리하기)

import pandas as pd
import numpy as np

# 데이터 불러오기
crime_anal_police = pd.read_csv('Lecture/Data/02. crime_in_Seoul.csv',
                                thousands = ',',         # ',' 가 없어짐
                                encoding = 'euc-kr')
crime_anal_police





