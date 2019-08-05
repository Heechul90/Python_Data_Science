### 02. Analysis for crime in Seoul - Review

# 패키지, 모듈, 함수 준비하기
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import folium
import json

# 한글 사용하기
import platform

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

## 1. 데이터 불러오기
crime_anal_police = pd.read_csv('Lecture/Data/02. crime_in_Seoul.csv',
                                thousands = ',',
                                encoding = 'euc-kr')
crime_anal_police.head()

## 2. google maps platform 이용해서 관서명을 구별로 바꾸기



## 3. 정리된 데이더 불러오기
crime_anal_raw = pd.read_csv('Lecture/Data/02. crime_in_Seoul_include_gu_name.csv',
                             encoding = 'utf-8',
                             index_col = 0)
crime_anal_raw.head()

# 구별로 pivot_table이용하여 바꾸기
crime_anal = pd.pivot_table(crime_anal_raw,
                            index = '구별',         # 구별로 pivot_table
                            aggfunc = np.sum)      # 중복된 구별로 합하기
crime_anal.head()

# 강간, 강도, 살인, 절도, 폭력검거율 컬럼 만들기(강간검거율 = 강간 검거 / 강간 발생 * 100)
crime_anal['강간검거율'] = crime_anal['강간 검거'] / crime_anal['강간 발생'] * 100
crime_anal['강도검거율'] = crime_anal['강도 검거'] / crime_anal['강도 발생'] * 100
crime_anal['살인검거율'] = crime_anal['살인 검거'] / crime_anal['살인 발생'] * 100
crime_anal['절도검거율'] = crime_anal['절도 검거'] / crime_anal['절도 발생'] * 100
crime_anal['폭력검거율'] = crime_anal['폭력 검거'] / crime_anal['폭력 발생'] * 100

del crime_anal['강간 검거']
del crime_anal['강도 검거']
del crime_anal['살인 검거']
del crime_anal['절도 검거']
del crime_anal['폭력 검거']
crime_anal.head()
crime_anal.columns

# 검거율이 100이 넘는것들을 100으로 만들기
con_list = ['강간검거율', '강도검거율', '살인검거율', '절도검거율', '폭력검거율']

for i in con_list:
    crime_anal.loc[crime_anal[i] > 100, i] = 100

crime_anal

# 발생이라는 컬럼 이름 삭제하기
crime_anal.rename(columns = {'강간 발생': '강간',
                             '강도 발생': '강도',
                             '살인 발생': '살인',
                             '절도 발생': '절도',
                             '폭력 발생': '폭력'},
                  inplace = True)
crime_anal.head()
crime_anal.columns

## 4. 데이터 표현을 위해 다듬기
# 데이터 정규화하기
from sklearn import preprocessing

col = ['강간', '강도', '살인', '절도', '폭력']
x = crime_anal[col].values
min_max_scaler = preprocessing.MinMaxScaler()

x_scaled = min_max_scaler.fit_transform(x.astype(float))
crime_anal_norm = pd.DataFrame(x_scaled,
                               columns = col,
                               index = crime_anal.index)

crime_anal_norm

col2 = ['강간검거율', '강도검거율', '살인검거율', '절도검거율', '폭력검거율']
crime_anal_norm[col2] = crime_anal[col2]
crime_anal_norm.head()

# CCTV 데이터 불러오기
result_cctv = pd.read_csv('Lecture/Data/01. CCTV_result.csv',
                          encoding = 'utf-8',
                          index_col = '구별')
crime_anal_norm[['인구수', 'CCTV']] = result_cctv[['인구수', '소계']]
crime_anal_norm.head()

# 강간, 강도, 살인, 절도, 폭력을 범죄로 합하기
crime_anal_norm['범죄'] = np.sum(crime_anal_norm[['강간', '강도', '살인', '절도', '폭력']], axis = 1)
crime_anal_norm

# '강간검거율','강도검거율','살인검거율','절도검거율','폭력검거율'을 검거로 합하기
col = ['강간검거율','강도검거율','살인검거율','절도검거율','폭력검거율']
crime_anal_norm['검거'] = np.sum(crime_anal_norm[col], axis=1)
crime_anal_norm.head()


## 5. 범죄 데이터 시각화하기

# 강도, 살인, 폭력간의 상관관계 그래프 그리기
sns.pairplot(crime_anal_norm,
             vars = ['강도', '살인', '폭력'],
             kind = 'reg',
             size = 3)
plt.show()

# x축은 인구수, cctv, y축은 살인, 강도 상관관계 그래프 그리기
sns.pairplot(crime_anal_norm,
             x_vars = ['인구수', 'CCTV'],
             y_vars = ['살인', '강도'],
             kind = 'reg',
             size= 3)

# x축은 인구수, cctv, y축은 살인검거율, 폭력검거율 상관관계 그래프 그리기
sns.pairplot(crime_anal_norm,
             x_vars = ['인구수', 'CCTV'],
             y_vars = ['살인검거율', '폭력검거율'],
             kind = 'reg',
             size= 3)

# 검거율의 합계인 검거 항목 최고값을 100으로 한정하고 그 값으로 정렬
tmp_max = crime_anal_norm['검거'].max()
crime_anal_norm['검거'] = crime_anal_norm['검거'] / tmp_max * 100
crime_anal_norm_sort = crime_anal_norm.sort_values(by = '검거', ascending = False)
crime_anal_norm_sort

# 정규화된 검거의 합으로 정렬해서 heapmap 보기

target_col = ['강간검거율', '강도검거율', '살인검거율', '절도검거율', '폭력검거율']

plt.figure(figsize = (10,10))
sns.heatmap(crime_anal_norm_sort[target_col],
            annot=True,
            fmt='f',
            linewidths=.5,
            cmap='RdPu')
plt.title('범죄 검거 비율 (정규화된 검거의 합으로 정렬)')
plt.show()

# 정규화된 발생 건수로 정렬해서 heatmap 보기
target_col = ['강간', '강도', '살인', '절도', '폭력', '범죄']

crime_anal_norm['범죄'] = crime_anal_norm['범죄'] / 5
crime_anal_norm_sort = crime_anal_norm.sort_values(by='범죄', ascending=False)

plt.figure(figsize = (10,10))
sns.heatmap(crime_anal_norm_sort[target_col],
            annot=True,
            fmt='f',
            linewidths=.5,
            cmap='RdPu')
plt.title('범죄비율 (정규화된 발생 건수로 정렬)')
plt.show()


## 6. 서울시 범죄율에 대한 지도 시각화
geo_path = 'Lecture/Data/02. skorea_municipalities_geo_simple.json'
geo_str = json.load(open(geo_path, encoding = 'utf-8'))

# 서울시의 중심의 위도와 경도 정보를 입력하고 결계선을 그리는데, 컬러맵은 살인 발생건수로 지정
# 살인 발생건수에 대해서 지도에 그리기
map = folium.Map(location=[37.5502, 126.982],    # 위도, 경도
                 zoom_start=11,                  # 줌 11
                 tiles='Stamen Toner')


map.choropleth(geo_data = geo_str,
               data = crime_anal_norm['살인'],   # 컴러맵은 살인
               columns = [crime_anal_norm.index, crime_anal_norm['살인']],
               fill_color = 'PuRd',             #PuRd, YlGnBu
               key_on = 'feature.id')

# 강간 발생건수에 대해서 지도에 그리기
map = folium.Map(location=[37.5502, 126.982],    # 위도, 경도
                 zoom_start=11,                  # 줌 11
                 tiles='Stamen Toner')

map.choropleth(geo_data = geo_str,
               data = crime_anal_norm['강간'],   # 컴러맵은 살인
               columns = [crime_anal_norm.index, crime_anal_norm['살인']],
               fill_color = 'PuRd',             #PuRd, YlGnBu
               key_on = 'feature.id')

# 범죄 전체 발생 건수에 인구수를 나누고 소수점 밑으로 가서 적절한 값을 곱하기
# 인구대비 살인 발생건수 지도화하기
tmp_criminal = crime_anal_norm['살인'] / crime_anal_norm['인구수'] * 1000000

map = folium.Map(location=[37.5502, 126.982],
                 zoom_start=11,
                 tiles='Stamen Toner')

map.choropleth(geo_data = geo_str,
               data = tmp_criminal,
               columns = [crime_anal.index, tmp_criminal],
               fill_color = 'PuRd',           #PuRd, YlGnBu
               key_on = 'feature.id')
map

# 인구대비 범죄 발생건수 지도화하기
tmp_criminal = crime_anal_norm['범죄'] /  crime_anal_norm['인구수'] * 1000000

map = folium.Map(location=[37.5502, 126.982], zoom_start=11,
                 tiles='Stamen Toner')

map.choropleth(geo_data = geo_str,
               data = tmp_criminal,
               columns = [crime_anal.index, tmp_criminal],
               fill_color = 'PuRd', #PuRd, YlGnBu
               key_on = 'feature.id')

# 인구대비 검거 발생건수 지도화하기
map = folium.Map(location=[37.5502, 126.982], zoom_start=11,
                 tiles='Stamen Toner')

map.choropleth(geo_data = geo_str,
               data = crime_anal_norm['검거'],
               columns = [crime_anal_norm.index, crime_anal_norm['검거']],
               fill_color = 'YlGnBu', #PuRd, YlGnBu
               key_on = 'feature.id')
map



# 7 서울시 경찰서별 검거율과 구별 범죄 발생율을 동시에 시각화하기
crime_anal_raw['lat'] = station_lat
crime_anal_raw['lng'] = station_lng

col = ['살인 검거', '강도 검거', '강간 검거', '절도 검거', '폭력 검거']
tmp = crime_anal_raw[col] / crime_anal_raw[col].max()

crime_anal_raw['검거'] = np.sum(tmp, axis=1)

crime_anal_raw.head()



############################
map = folium.Map(location=[37.5502, 126.982], zoom_start=11)

for n in crime_anal_raw.index:
    folium.Marker([crime_anal_raw['lat'][n],
                   crime_anal_raw['lng'][n]]).add_to(map)

map



#############################
map = folium.Map(location=[37.5502, 126.982], zoom_start=11)

for n in crime_anal_raw.index:
    folium.CircleMarker([crime_anal_raw['lat'][n], crime_anal_raw['lng'][n]],
                        radius=crime_anal_raw['검거'][n] * 10,
                        color='#3186cc', fill_color='#3186cc', fill=True).add_to(map)

map



#############################
map = folium.Map(location=[37.5502, 126.982], zoom_start=11)

map.choropleth(geo_data=geo_str,
               data=crime_anal_norm['범죄'],
               columns=[crime_anal_norm.index, crime_anal_norm['범죄']],
               fill_color='PuRd',  # PuRd, YlGnBu
               key_on='feature.id')

for n in crime_anal_raw.index:
    folium.CircleMarker([crime_anal_raw['lat'][n], crime_anal_raw['lng'][n]],
                        radius=crime_anal_raw['검거'][n] * 10,
                        color='#3186cc', fill_color='#3186cc', fill=True).add_to(map)

map

