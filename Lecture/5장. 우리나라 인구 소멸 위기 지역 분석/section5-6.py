### section 5-6 Cartogram으로 우리나라 지도 만들기

# 모듈 준비하기
import urllib.request
import json
import pandas as pd
import bs4

# 데이터 불러오기
draw_korea_raw = pd.read_excel('Lecture/Data/05. draw_korea_raw.xlsx',
                               encoding = 'euc-kr')
draw_korea_raw

