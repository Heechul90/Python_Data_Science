### section 3-5 (다수의 웹 페이지에 자동으로 접근해서 원하는 정보 가져오기)

# 모듈 준비하기
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from urllib.request import urlopen


# 파일 불러오기
df = pd.read_csv('Lecture/Data/03. best_sandwiches_list_chicago.csv',
                 index_col = 0)
df.head()
df['URL'][0]

# 첫번째 URL을 BeautifulSoup로 읽기
html = urlopen(df['URL'][0])
soup_tmp =BeautifulSoup(html, 'html.parser')
soup_tmp

# 웹에서 얻고자 하는것을 태그를 이용해서 찾기
print(soup_tmp('p', 'addy'))     # 내가 찾고자 하는 태그 맞음
price_tmp = soup_tmp.find('p', 'addy').get_text()
price_tmp.split()

# 가격가져오기
price_tmp.split()[0]
price_tmp.split()[0].strip('.')     # 뒤에 점 없애기
price_tmp.split()[0][:-1]           # 뒤에 점 없애기

# 주소 가져오기
' '.join(price_tmp.split()[1 : -2])

# 50 페이지에서 가격과 주소 가져오기
price = []
address = []

for i in df.index:
    html = urlopen(df['URL'][i])
    soup_tmp = BeautifulSoup(html, 'html.parser')

    gettings = soup_tmp.find('p', 'addy').get_text()

    price.append(gettings.split()[0].strip('.'))
    address.append(' '.join(gettings.split()[1 : -2]))
    print(i)

price
address



### section 3-6 (Jupyter Notebook에서 상태 진행바를 쉽게 만들어주는 tqdm 모듈)

# 설치는 conda install -c conda-forge tqdm


### section 3-7 (상태 진행바까지 적용하고 다시 샌드위치 페이지 50개에 접근하기)
# tqdm 적용해서 JUpyter에서 해보기
from tqdm import tqdm_notebook

price = []
address = []

for n in tqdm_notebook(df.index):
    html = urlopen(df['URL'][n])
    soup_tmp = BeautifulSoup(html, 'lxml')

    gettings = soup_tmp.find('p', 'addy').get_text()

    price.append(gettings.split()[0][:-1])
    address.append(' '.join(gettings.split()[1:-2]))

price
address



### section 3-8 (50개 웹 페이지데 대한 정보 가져오기
price
address

# 크기 확인
len(price), len(address), len(df)

# df에 price와 address 추가하기
df['Price'] = price
df['Address'] = address
df.head()
df.columns

del df['URL']

df = df.set_index('Rank')
df.head()
df.columns

# csv 저장하기
df.to_csv('Lecture/Data/03. best_sandwiches_list_chicago2.csv',
          sep = ',',
          encoding = 'utf-8')