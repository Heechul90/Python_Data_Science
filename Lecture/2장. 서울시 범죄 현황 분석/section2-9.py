### section 2-9 지도 시각화 도구 - Folium

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium

map_osm = folium.Map(location = [45.5236, -122.6750])
map_osm

# zoom_start 확대 비율을 정의
stamen = folium.Map(location=[45.5236, -122.6750],
                    zoom_start=13)
stamen


# tiles 옵션으로 지도 모양 바꾸기
stamen = folium.Map(location=[45.5236, -122.6750],  # 위도, 경도
                    tiles='Stamen Toner',           #
                    zoom_start=13)                  # 줌
stamen


# 마커 넣기
map_1 = folium.Map(location=[45.372, -121.6972],
                   zoom_start=12,
                   tiles='Stamen Terrain')
folium.Marker([45.3288, -121.6625],
              popup='Mt. Hood Meadows',                         #
              icon=folium.Icon(icon='cloud')).add_to(map_1)     # 마커 모양 icon 구름모양

folium.Marker([45.3311, -121.7113],
              popup='Timberline Lodge',
              icon=folium.Icon(icon='cloud')).add_to(map_1)
map_1


# 마커 다양하게 넣기
map_1 = folium.Map(location=[45.372, -121.6972],
                   zoom_start=12,
                   tiles='Stamen Terrain')

folium.Marker([45.3288, -121.6625],
              popup='Mt. Hood Meadows',
              icon=folium.Icon(icon='cloud')).add_to(map_1)

folium.Marker([45.3311, -121.7113],
              popup='Timberline Lodge',
              icon=folium.Icon(color='green')).add_to(map_1)

folium.Marker([45.3300, -121.6823],
              popup='Some Other Location',
              icon=folium.Icon(color='red',icon='info-sign')).add_to(map_1)
map_1


##############
map_2 = folium.Map(location=[45.5236, -122.6750],
                   tiles='Stamen Toner',
                   zoom_start=13)

folium.Marker([45.5244, -122.6699],
              popup='The Waterfront' ).add_to(map_2)

folium.CircleMarker([45.5215, -122.6261],
                    radius=50,
                    popup='Laurelhurst Park',
                    color='#3186cc',
                    fill_color='#3186cc', ).add_to(map_2)
map_2


################
map_5 = folium.Map(location=[45.5236, -122.6750],
                   zoom_start=13)

folium.RegularPolygonMarker([45.5012, -122.6655],
                            popup='Ross Island Bridge',
                            fill_color='#132b5e',
                            number_of_sides=3,
                            radius=10).add_to(map_5)

folium.RegularPolygonMarker([45.5132, -122.6708],
                            popup='Hawthorne Bridge',
                            fill_color='#45647d',
                            number_of_sides=4,
                            radius=10).add_to(map_5)

folium.RegularPolygonMarker([45.5275, -122.6692],
                            popup='Steel Bridge',
                            fill_color='#769d96',
                            number_of_sides=6,
                            radius=10).add_to(map_5)

folium.RegularPolygonMarker([45.5318, -122.6745],
                            popup='Broadway Bridge',
                            fill_color='#769d96',
                            number_of_sides=8,
                            radius=10).add_to(map_5)
map_5



# 데이터 불러오기
state_unemployment = 'Lecture/Data/02. folium_US_Unemployment_Oct2012.csv'

state_data = pd.read_csv(state_unemployment)
state_data.head()

# json 파일 불러오기
state_geo = 'Lecture/Data/02. folium_us-states.json'

map = folium.Map(location=[40, -98],
                 zoom_start=4)

map.choropleth(geo_data=state_geo,
               data=state_data,
               columns=['State', 'Unemployment'],
               key_on='feature.id',
               fill_color='YlGn',
               legend_name='Unemployment Rate (%)')
map
