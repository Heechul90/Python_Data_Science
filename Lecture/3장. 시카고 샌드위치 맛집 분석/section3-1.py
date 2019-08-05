### section 3-1 (웹 데이터를 가져오는 Beautiful Soup 익히기)

# 모듈 준비하기
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

# htlm 파일 읽어오기
page = open('Lecture/Data/03. test_first.html', 'r').read()
soup = BeautifulSoup(page, 'html.parser')
print(soup.prettify())           # html 페이지의 내용 전체 보기
list(soup.children)              # soup 변수의 한 단계 아래에 포함된 태그

# soup는 문서 전체를 저장한 변수이기 때문에 그 안에서 html 태그에 접속하기
html = list(soup.children)[2]
html
list(html.children)

# body 태그 보기
body = list(html.children)[3]
body

# children, parent이용 말고 한번에 나타내기
soup.body
list(body.children)

# 접근할 태그에 find나 find_all 명령 사용하기
soup.find_all('p')

# 하나만 찾을 때는 find
soup.find('p')

# p 태그의 class가 outer-text 찾기
soup.find_all(class_ = 'outer-text')

# class 이름만으로 outer-text 찾기
soup.find_all(id = 'first')

# id가 first인 태그
soup.find('p')

# find는 제일 처음 나타난 태그만 찾기때문에 다음 태그찾는것은 다른 방법 이용
soup.head
soup.head.next_sibling

# head와 같은 위치에 있던 body 태그로 접근
soup.head.next_sibling.next_sibling

# 처음 나타나는 p태그에 next_sibling을 두번걸어 p태그로 이동
body.p
body.p.next_sibling.next_sibling

# 반복문으로 get_text를 이용해 텍스트만 가지고오기
for each_tag in soup.find_all('p'):
    print(each_tag.get_text())

# body전체에서 get_text하면 태그자리에 있던 자리는 \n 줄바꿈이 표시되고 text 보여줌
body.get_text

# 클릭 가능한을 의미하는 a태그 찾기
links = soup.find_all('a')
links

# 반복문으로 가져오기
for each in links:
    href = each['href']
    text = each.string
    print(text + '->' + href)
    
