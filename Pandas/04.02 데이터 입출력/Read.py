### 데이터 입출력

import pandas as pd
import numpy as np


## %%writefile 명령
%%writefile sample1.csv
c1, c2, c3
1, 1.11, one
2, 2.22, two
3, 3.33, three

Writing sample1.csv


## CSV 파일 입력
pd.read_csv('sample1.csv')

# %%writefile 명령
%%writefile sample2.csv
1, 1.11, one
2, 2.22, two
3, 3.33, three

Writing sample1.csv

# 열의 이름을 지정해서 읽음
pd.read_csv('sample2.csv',
            names = ['c1', 'c2', 'c3'])

# 특정한 열을 행 인덱스로 지정
pd.read_csv('sample1.csv', index_col = 'c1')


# 확장자가 CSV가 아닌 파일
# 즉, 데이터를 구분하는 구분자(separator)가 쉼표(comma)가 아니면
# sep 인수를 써서 구분자를 사용자가 지정해준다.
# 만약 구분자가 길이가 정해지지 않은 공백인 경우에는
# \s+라는 정규식(regular expression) 문자열을 사용한다.

%%writefile sample3.txt
c1        c2        c3        c4
0.179181 -1.538472  1.347553  0.43381
1.024209  0.087307 -1.281997  0.49265
0.417899 -2.002308  0.255245 -1.10515

pd.read_table('sample3.txt', sep='\s+')

# 만약 자료 파일 중에 건너 뛰어야 할 행이 있으면 skiprows 인수를 사용한다.
%%writefile sample4.txt
파일 제목: sample4.txt
데이터 포맷의 설명:
c1, c2, c3
1, 1.11, one
2, 2.22, two
3, 3.33, three

Writing sample4.txt

pd.read_table('sample4.txt', skiprows = [0, 1])

# 특정한 값을 NaN으로 취급하고 싶으면 na_values 인수에 NaN 값으로 취급할 값을 넣는다.
%%writefile sample5.csv
c1, c2, c3
1, 1.11, one
2, , two
누락, 3.33, three

Writing sample5.csv

df = pd.read_csv('sample5.csv', na_values = ['누락'])
df


## CSV 파일 출력
## 파이썬의 데이터프레임 값을 CSV 파일로 출력하고 싶으면 to_csv() 메서드를 사용

df.to_csv('sample6.csv')
!type sample6.csv

# 파일을 읽을 때와 마찬가지로 출력할 때도 sep 인수로 구분자를 바꿀 수 있다.
df.to_csv('sample7.txt', sep='|')
!type sample7.txt

# na_rep 인수로 NaN 표시값을 바꿀 수도 있다.
df.to_csv('sample8.csv', na_rep='누락')
!type sample8.csv

# index, header 인수를 지정하여 인덱스 및 헤더 출력 여부를 지정하는 것도 가능
df.index = ["a", "b", "c"]
df

df.to_csv('sample9.csv', index=False, header=False)
!type sample9.csv  # 윈도우에서는 !type sample6.csv 명령을 사용



## 인터넷 상의 CSV 파일 입력
## 웹상에는 다양한 데이터 파일이 CSV 파일 형태로 제공된다.
## read_csv 명령 사용시 파일 패스 대신 URL을 지정하면
## Pandas가 직접 해당 파일을 다운로드하여 읽어들인다.
df = pd.read_csv("https://raw.githubusercontent.com/datascienceschool/docker_rpython/master/data/titanic.csv")

pd.set_option("display.max_rows", 20)  # 앞뒤로 모두 20행만 보여준다.
df

# 만약 앞이나 뒤의 특정 갯수만 보고 싶다면 head 메서드나 tail 메서드를 이용
df.head()
df.tail(2)


## 인터넷 상의 데이터 베이스 자료 입력
## pandas_datareader 패키지의 DataReader 을 사용하면
## 일부 인터넷 사이트의 자료를 바로 pandas로 읽어들일 수 있다.
import datetime
dt_start = datetime.datetime(2015, 1, 1)
dt_end = "2016, 6, 30"

# data_source 인수로 데이터를 읽어올 웹 사이트를 지정
import pandas_datareader as pdr

gdp = pdr.get_data_fred('GDP', dt_start, dt_end)
gdp.tail()

# 데이터 코드에 리스트를 넣으면 여러개의 데이터를 동시에 가져온다.
inflation = pdr.get_data_fred(["CPIAUCSL", "CPILFESL"], dt_start, dt_end)
inflation.tail()