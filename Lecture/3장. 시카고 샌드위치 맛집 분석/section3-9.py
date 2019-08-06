### section 3-9 (맛집 위치를 지도에 표기하기)

# 모듈 준비하기
import folium
import pandas as pd
import googlemaps
import numpy as np

# 데이터 불러오기
df = pd.read_csv('Lecture/Data/03. best_sandwiches_list_chicago2.csv',
                 encoding = 'utf-8',
                 index_col = 'Rank')
df.head()
df.columns

# googlemaps을 키를 이용해서 읽기
gmaps_key = " ******************** "        # google maps platform 사이트에서 받기
gmaps = googlemaps.Client(key=gmaps_key)

# 50개 맛집에 대한 위도, 경도 정보 받아오기
lat = []
lng = []

for n in df.index:
    if df['Address'][n] != 'Multiple':
        target_name = df['Address'][n] + ', ' + 'Chicago'
        gmaps_output = gmaps.geocode(target_name)
        location_output = gmaps_output[0].get('geometry')
        lat.append(location_output['location']['lat'])
        lng.append(location_output['location']['lng'])

    else:
        lat.append(np.nan)
        lng.append(np.nan)

# 위도, 경도 확인하고 df에 위도, 경도 추가하기
len(lat), len(lng)

df['lat'] = lat
df['lng'] = lng
df.head()

# 위도, 경도의 평균값을 중앙에 둠
mapping = folium.Map(location=[df['lat'].mean(), df['lng'].mean()],
                     zoom_start=11)
folium.Marker([df['lat'].mean(), df['lng'].mean()],
              popup='center').add_to(mapping)
mapping

# 지도맵에 표기하기
mapping = folium.Map(location=[df['lat'].mean(), df['lng'].mean()],
                     zoom_start=11)

for n in df.index:
    if df['Address'][n] != 'Multiple':
        folium.Marker([df['lat'][n], df['lng'][n]],
                                      popup=df['Cafe'][n]).add_to(mapping)

mapping