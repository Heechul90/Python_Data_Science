### section 3-2 (크롬 개발자 도구를 이용해서 원하는 태그 찾기)

# 모듈 준비하기
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from urllib.request import urlopen


url = 'https://finance.naver.com/marketindex/'
page = urlopen(url)

soup = BeautifulSoup(page, 'html.parser')
print(soup.prettify())
soup.find_all('span', 'value')[0].string

soup.find_all('href')[0]
