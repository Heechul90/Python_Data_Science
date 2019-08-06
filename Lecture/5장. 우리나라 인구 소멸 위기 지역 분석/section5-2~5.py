### section 5-2 (인구 데이터 확보하고 정리하기)

# 모듈 준비하기
import pandas as pd
import numpy as np
import platform
import matplotlib.pyplot as plt
import urllib.request
import json
import bs4
import seaborn as sns
import folium


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



### section 5-6 Cartogram으로 우리나라 지도 만들기

# 데이터 불러오기
draw_korea_raw = pd.read_excel('Lecture/Data/05. draw_korea_raw.xlsx',
                               encoding = 'euc-kr')
draw_korea_raw

# 각 행정구역의 좌표를 얻기 위해 pivot_table 반대 개념인 .stack() 명령 사용
draw_korea_raw_stacked = pd.DataFrame(draw_korea_raw.stack())

# 인덱스를 재설정하고 컬럼의 이름을 다시 설정
draw_korea_raw_stacked.reset_index(inplace = True)
draw_korea_raw_stacked.rename(columns = {'level_0': 'y',
                                         'level_1': 'x',
                                         0: 'ID'},
                              inplace = True)
draw_korea_raw_stacked

# ID컬럼에서 지도에 표기할때 시 이름 구 이름으로 줄을 나누기 위해 분리
draw_korea = draw_korea_raw_stacked

# 경계선 설정
BORDER_LINES = [
    [(5, 1), (5,2), (7,2), (7,3), (11,3), (11,0)], # 인천
    [(5,4), (5,5), (2,5), (2,7), (4,7), (4,9), (7,9),
     (7,7), (9,7), (9,5), (10,5), (10,4), (5,4)], # 서울
    [(1,7), (1,8), (3,8), (3,10), (10,10), (10,7),
     (12,7), (12,6), (11,6), (11,5), (12, 5), (12,4),
     (11,4), (11,3)], # 경기도
    [(8,10), (8,11), (6,11), (6,12)], # 강원도
    [(12,5), (13,5), (13,4), (14,4), (14,5), (15,5),
     (15,4), (16,4), (16,2)], # 충청북도
    [(16,4), (17,4), (17,5), (16,5), (16,6), (19,6),
     (19,5), (20,5), (20,4), (21,4), (21,3), (19,3), (19,1)], # 전라북도
    [(13,5), (13,6), (16,6)], # 대전시
    [(13,5), (14,5)], #세종시
    [(21,2), (21,3), (22,3), (22,4), (24,4), (24,2), (21,2)], #광주
    [(20,5), (21,5), (21,6), (23,6)], #전라남도
    [(10,8), (12,8), (12,9), (14,9), (14,8), (16,8), (16,6)], #충청북도
    [(14,9), (14,11), (14,12), (13,12), (13,13)], #경상북도
    [(15,8), (17,8), (17,10), (16,10), (16,11), (14,11)], #대구
    [(17,9), (18,9), (18,8), (19,8), (19,9), (20,9), (20,10), (21,10)], #부산
    [(16,11), (16,13)], #울산
#     [(9,14), (9,15)],
    [(27,5), (27,6), (25,6)],
]

# 지역 이름 표시
plt.figure(figsize=(8, 11))


for idx, row in draw_korea.iterrows():

    # 광역시는 구 이름이 겹치는 경우가 많아서 시단위 이름도 같이 표시한다.
    # (중구, 서구)
    if len(row['ID'].split()) == 2:
        dispname = '{}\n{}'.format(row['ID'].split()[0], row['ID'].split()[1])
    elif row['ID'][:2] == '고성':
        dispname = '고성'
    else:
        dispname = row['ID']

    # 서대문구, 서귀포시 같이 이름이 3자 이상인 경우에 작은 글자로 표시한다.
    if len(dispname.splitlines()[-1]) >= 3:
        fontsize, linespacing = 9.5, 1.5
    else:
        fontsize, linespacing = 11, 1.2

    plt.annotate(dispname, (row['x'] + 0.5, row['y'] + 0.5), weight='bold',
                 fontsize=fontsize, ha='center', va='center',
                 linespacing=linespacing)

# 시도 경계 그린다.
for path in BORDER_LINES:
    ys, xs = zip(*path)
    plt.plot(xs, ys, c='black', lw=1.5)

plt.gca().invert_yaxis()
# plt.gca().set_aspect(1)

plt.axis('off')

plt.tight_layout()
plt.show()


# 인구에 대한 분석 결과인 pop과 지도를 그리기 위한 draw_korea의 대이터를 합칠 때
# 사용할 key인 ID 컬럼의 내용이 문제가 없는지 확인하자
set(draw_korea['ID'].unique()) - set(pop['ID'].unique())
set(pop['ID'].unique()) - set(draw_korea['ID'].unique())

# 위 결과에 따르면, pop에 행정구를 가진 시들의 데이터가 더 있다는 것을 알 수 있다.
# 어차피 지도에서는 표시되지 못하니 삭제한다
tmp_list = list(set(pop['ID'].unique()) - set(draw_korea['ID'].unique()))

for tmp in tmp_list:
    pop = pop.drop(pop[pop['ID'] == tmp].index)

print(set(pop['ID'].unique()) - set(draw_korea['ID'].unique()))

pop.head()

# 이제 pop과 draw_korea의 ID 컬럼이 일치했다고 보고, ID를 key로 merge를 시키도록 한다.
pop = pd.merge(pop, draw_korea, how='left', on=['ID'])

pop.head()

# 이제 위 pop 데이터에서 지도에 표현하고자 하는 데이터가 인구수합계라면
# 이 값들이 아까 만든 각 해당 행정구역에 위치하면 된다.
mapdata = pop.pivot_table(index='y', columns='x', values='인구수합계')
masked_mapdata = np.ma.masked_where(np.isnan(mapdata), mapdata)

mapdata

masked_mapdata

# 위 내용과 colormap을 완성하는 명령을 추가해서 함수로 만들자
def drawKorea(targetData, blockedMap, cmapname):
    gamma = 0.75

    whitelabelmin = (max(blockedMap[targetData]) -
                     min(blockedMap[targetData])) * 0.25 + \
                    min(blockedMap[targetData])

    datalabel = targetData

    vmin = min(blockedMap[targetData])
    vmax = max(blockedMap[targetData])

    mapdata = blockedMap.pivot_table(index='y', columns='x', values=targetData)
    masked_mapdata = np.ma.masked_where(np.isnan(mapdata), mapdata)

    plt.figure(figsize=(9, 11))
    plt.pcolor(masked_mapdata, vmin=vmin, vmax=vmax, cmap=cmapname,
               edgecolor='#aaaaaa', linewidth=0.5)

    # 지역 이름 표시
    for idx, row in blockedMap.iterrows():
        # 광역시는 구 이름이 겹치는 경우가 많아서 시단위 이름도 같이 표시한다.
        # (중구, 서구)
        if len(row['ID'].split()) == 2:
            dispname = '{}\n{}'.format(row['ID'].split()[0], row['ID'].split()[1])
        elif row['ID'][:2] == '고성':
            dispname = '고성'
        else:
            dispname = row['ID']

        # 서대문구, 서귀포시 같이 이름이 3자 이상인 경우에 작은 글자로 표시한다.
        if len(dispname.splitlines()[-1]) >= 3:
            fontsize, linespacing = 10.0, 1.1
        else:
            fontsize, linespacing = 11, 1.

        annocolor = 'white' if row[targetData] > whitelabelmin else 'black'
        plt.annotate(dispname, (row['x'] + 0.5, row['y'] + 0.5), weight='bold',
                     fontsize=fontsize, ha='center', va='center', color=annocolor,
                     linespacing=linespacing)

    # 시도 경계 그린다.
    for path in BORDER_LINES:
        ys, xs = zip(*path)
        plt.plot(xs, ys, c='black', lw=2)

    plt.gca().invert_yaxis()

    plt.axis('off')

    cb = plt.colorbar(shrink=.1, aspect=10)
    cb.set_label(datalabel)

    plt.tight_layout()
    plt.show()



### section 5-7 (인구 현황 및 인구 소멸 지역 확인하기)
drawKorea('인구수합계', pop, 'Blues')

# 인구 소멸 위기 지역에 대한 표현
pop['소멸위기지역'] = [1 if con else 0 for con in pop['소멸위기지역']]
drawKorea('소멸위기지역', pop, 'Reds')




### section 5-8 (인구 현황에서 여성 인구 비율 확인하기)
def drawKorea(targetData, blockedMap, cmapname):
    gamma = 0.75

    whitelabelmin = 20.

    datalabel = targetData

    tmp_max = max([np.abs(min(blockedMap[targetData])),
                   np.abs(max(blockedMap[targetData]))])
    vmin, vmax = -tmp_max, tmp_max

    mapdata = blockedMap.pivot_table(index='y', columns='x', values=targetData)
    masked_mapdata = np.ma.masked_where(np.isnan(mapdata), mapdata)

    plt.figure(figsize=(9, 11))
    plt.pcolor(masked_mapdata, vmin=vmin, vmax=vmax, cmap=cmapname,
               edgecolor='#aaaaaa', linewidth=0.5)

    # 지역 이름 표시
    for idx, row in blockedMap.iterrows():
        # 광역시는 구 이름이 겹치는 경우가 많아서 시단위 이름도 같이 표시한다.
        # (중구, 서구)
        if len(row['ID'].split()) == 2:
            dispname = '{}\n{}'.format(row['ID'].split()[0], row['ID'].split()[1])
        elif row['ID'][:2] == '고성':
            dispname = '고성'
        else:
            dispname = row['ID']

        # 서대문구, 서귀포시 같이 이름이 3자 이상인 경우에 작은 글자로 표시한다.
        if len(dispname.splitlines()[-1]) >= 3:
            fontsize, linespacing = 10.0, 1.1
        else:
            fontsize, linespacing = 11, 1.

        annocolor = 'white' if np.abs(row[targetData]) > whitelabelmin else 'black'
        plt.annotate(dispname, (row['x'] + 0.5, row['y'] + 0.5), weight='bold',
                     fontsize=fontsize, ha='center', va='center', color=annocolor,
                     linespacing=linespacing)

    # 시도 경계 그린다.
    for path in BORDER_LINES:
        ys, xs = zip(*path)
        plt.plot(xs, ys, c='black', lw=2)

    plt.gca().invert_yaxis()

    plt.axis('off')

    cb = plt.colorbar(shrink=.1, aspect=10)
    cb.set_label(datalabel)

    plt.tight_layout()
    plt.show()


pop.head()

pop['여성비'] = (pop['인구수여자']/pop['인구수합계'] - 0.5)*100
drawKorea('여성비', pop, 'RdBu')

pop['2030여성비'] = (pop['20-39세여자']/pop['20-39세합계'] - 0.5)*100
drawKorea('2030여성비', pop, 'RdBu')



### section 5-9 (Folium에서 인구 소멸 위기 지역 표현하기)
pop_folium = pop.set_index('ID')
pop_folium.head()

import folium
import json
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

geo_path = 'Lecture/Data/05. skorea_municipalities_geo_simple.json'
geo_str = json.load(open(geo_path, encoding='utf-8'))

map = folium.Map(location=[36.2002, 127.054], zoom_start=7)
map.choropleth(geo_data = geo_str,
               data = pop_folium['인구수합계'],
               columns = [pop_folium.index, pop_folium['인구수합계']],
               fill_color = 'YlGnBu', #PuRd, YlGnBu
               key_on = 'feature.id')

map


map = folium.Map(location=[36.2002, 127.054], zoom_start=7)
map.choropleth(geo_data = geo_str,
               data = pop_folium['소멸위기지역'],
               columns = [pop_folium.index, pop_folium['소멸위기지역']],
               fill_color = 'PuRd', #PuRd, YlGnBu
               key_on = 'feature.id')

map



draw_korea.to_csv("Lecture/Data/05. draw_korea.csv", encoding='utf-8', sep=',')