### section 3-3(실전: 시카고 샌드위치 맛집 소개 사이트에 접근하기)

# 모듈 준비하기
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from urllib.request import urlopen


# url 가져오기
url_base = 'http://www.chicagomag.com'
url_sub = '/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/'
url = url_base + url_sub

# html 열기
html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")
soup

# find_all 명령어를 통해 div의 sammy태그를 찾아 확인
# 내가 찾고자 하는것이 맞는지 확인
print(soup.find_all('div', 'sammy'))
len(soup.find_all('div', 'sammy'))
print(soup.find_all('div', 'sammy')[0])



### section 3-4 (접근한 웹 페이지에서 원하는 데이터 추출하고 정리하기
tmp_one = soup.find_all('div', 'sammy')[0]
type(tmp_one)

bs4.element.Tag의 타입은 (find, find_all)명령을 사용할 수 있음

# 랭크순위 가져오기
tmp_one.find(class_ = 'sammyRank')
tmp_one.find(class_ = 'sammyRank').get_text()

# 가게 이름 가져오기
tmp_one.find(class_ = 'sammyListing').get_text()

import re

tmp_string = tmp_one.find(class_ = 'sammyListing').get_text()
re.split(('\n|\r\n'), tmp_string)

print(re.split(('\n|\r\n'), tmp_string)[0])
print(re.split(('\n|\r\n'), tmp_string)[1])


# 링크주소 가져오기
tmp_one.find('a')['href']


from urllib.parse import urljoin

rank = []
main_menu = []
cafe_name = []
url_add = []

list_soup = soup.find_all('div', 'sammy')

for i in list_soup:
    rank.append(i.find(class_ = 'sammyRank').get_text())

    tmp_string = i.find(class_ = 'sammyListing').get_text()

    main_menu.append(re.split(('\n|\r\n'), tmp_string)[0])
    cafe_name.append(re.split(('\n|\r\n'), tmp_string)[1])

    url_add.append(urljoin(url_base, i.find('a')['href']))


rank[:5]
main_menu[:5]
cafe_name[:5]
url_add[:5]

len(rank), len(main_menu), len(cafe_name), len(url_add)

# pandas를 이용해 데이터 프레임 만들기
data = {'Rank':rank,
        'Menu':main_menu,
        'Cafe':cafe_name,
        'URL':url_add}

df = pd.DataFrame(data)
df.head()
df.columns

# csv 로 저장하기
df.to_csv('../data/03. best_sandwiches_list_chicago.csv', sep=',',
          encoding='UTF-8')