### section 5-2 (인구 데이터 확보하고 정리하기)

# 모듈 준비하기
import pandas as pd
import numpy as np
import platform
import matplotlib.pyplot as plt


# 한글 사용하기
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')


## 데이터 불러오기
population = pd.read_excel('Lecture/Data/05. population_raw_data.xlsx',
                           header = 1)

# NaN 빈칸으로 말고 앞 내용으로 채우기
population.fillna(method = 'pad', inplace = True)

# 컬럼 이름 바꾸기
population.rename(columns = {'행정구역(동읍면)별(1)': '광역시도',
                             '행정구역(동읍면)별(2)': '시도',
                             '계': '인구수'},
                  inplace = True)

# 중간중간에 소계 항목 삭제하기
population = population[(population['시도'] != '소계')]

population.is_copy = False

# 항목 컴럼이름을 구분으로 바꾸기
population.rename(columns = {'항목': '구분'},
                  inplace = True)

# 긴 이름 짧고 보기 쉽게 바꾸기
population.loc[population['구분'] == '총인구수 (명)', '구분'] = '합계'
population.loc[population['구분'] == '남자인구수 (명)', '구분'] = '남자'
population.loc[population['구분'] == '여자인구수 (명)', '구분'] = '여자'

population.head()
population.columns



### section 5-3 (인구 소멸 위기 지역 계산하고 데이터 정리하기)

# 20-39, 65세이상 컬럼 만들기
population['20-39세'] = population['20 - 24세'] + \
                        population['25 - 29세'] + \
                        population['30 - 34세'] + \
                        population['35 - 39세']
population['65세이상'] = population['65 - 69세'] + \
                        population['70 - 74세'] + \
                        population['75 - 79세'] + \
                        population['80 - 84세'] + \
                        population['85 - 89세'] + \
                        population['90 - 94세'] + \
                        population['95 - 99세'] + \
                        population['100+']

# 인덱스는 광역시도, 시도로 잡고 컬럼은 구분, values는 인구수, 20-39세, 65세 이상으로 하기
pop = pd.pivot_table(data = population,
                     index = ['광역시도', '시도'],
                     columns = '구분',
                     values = ['인구수', '20-39세', '65세이상'])
pop

# 소멸비율 컬럼 만들기(소멸비율 = 20-39세 / 65세이상 / 2)
# 여성인구와 65세이상 인구
pop['소멸비율'] = pop['20-39세', '여자'] / (pop['65세이상', '합계'] / 2)

# 소멸위기지역 컬럼 만들기 (소멸위기지역은 소멸비율이 1보다 작은지역)
pop['소멸위기지역'] = pop['소멸비율'] < 1

# 소멸위기지역 리트스 뽑기
pop[pop['소멸위기지역'] == True].index.get_level_values(1)

# pivot_table에 의해 다단으로 구성된 index를 다시 초기화
pop.reset_index(inplace = True)

# 다단으로 표시된 컬럼을 하나로 합치기
tmp_columns = [pop.columns.get_level_values(0)[n] + \
               pop.columns.get_level_values(1)[n]
               for n in range(0, len(pop.columns.get_level_values(0)))]

pop.columns = tmp_columns
pop.head()
pop.info()



### section 5-4 (대한민국 지도 그리는 방법에 대한 소개)

# 참고
# https://www.pinkwink.kr/1005
# https://goo.gl/5wWzLL



### section 5-5 (지도 시각화를 위해 지역별 고유 ID 만들기
pop['시도'].unique()

# 광역시가 아니면서 구를 가지고 있는 시와 그 행정구를 파이썬의 dic형으로 선언
si_name = [None] * len(pop)

tmp_gu_dict = {'수원':['장안구', '권선구', '팔달구', '영통구'],
               '성남':['수정구', '중원구', '분당구'],
               '안양':['만안구', '동안구'],
               '안산':['상록구', '단원구'],
               '고양':['덕양구', '일산동구', '일산서구'],
               '용인':['처인구', '기흥구', '수지구'],
               '청주':['상당구', '서원구', '흥덕구', '청원구'],
               '천안':['동남구', '서북구'],
               '전주':['완산구', '덕진구'],
               '포항':['남구', '북구'],
               '창원':['의창구', '성산구', '진해구', '마산합포구', '마산회원구'],
               '부천':['오정구', '원미구', '소사구']}


for n in pop.index:
    if pop['광역시도'][n][-3:] not in ['광역시', '특별시', '자치시']:
        if pop['시도'][n][:-1] == '고성' and pop['광역시도'][n] == '강원도':
            si_name[n] = '고성(강원)'
        elif pop['시도'][n][:-1] == '고성' and pop['광역시도'][n] == '경상남도':
            si_name[n] = '고성(경남)'
        else:
            si_name[n] = pop['시도'][n][:-1]

        for keys, values in tmp_gu_dict.items():
            if pop['시도'][n] in values:
                if len(pop['시도'][n]) == 2:
                    si_name[n] = keys + ' ' + pop['시도'][n]
                elif pop['시도'][n] in ['마산합포구', '마산회원구']:
                    si_name[n] = keys + ' ' + pop['시도'][n][2:-1]
                else:
                    si_name[n] = keys + ' ' + pop['시도'][n][:-1]

    elif pop['광역시도'][n] == '세종특별자치시':
        si_name[n] = '세종'

    else:
        if len(pop['시도'][n]) == 2:
            si_name[n] = pop['광역시도'][n][:2] + ' ' + pop['시도'][n]
        else:
            si_name[n] = pop['광역시도'][n][:2] + ' ' + pop['시도'][n][:-1]

si_name

# 지도 시각화에 사용하기 위해 위 과정에서 만들어진 행정구역의 고유한 이름을 ID로 지정한다.
pop['ID'] = si_name


del pop['20-39세남자']
del pop['65세이상남자']
del pop['65세이상여자']

pop.head()
