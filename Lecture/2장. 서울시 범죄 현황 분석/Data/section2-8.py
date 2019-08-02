### section 2-8 범죄 데이터 시각화하기

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 그래프에 대한 한글 폰트 문제 해결하기
import platform
path = "c:/Windows/Fonts/malgun.ttf"
from matplotlib import font_manager, rc
if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')


# 데이터 불러오기
crime_anal_norm = pd.read_csv('Lecture/Data/02. crime_anal_norm.csv')
crime_anal_norm = crime_anal_norm.set_index('구별')
crime_anal_norm.head()
crime_anal_norm.columns

# pairplot으로 강도, 살인, 폭력 간의 상관관계 그래프 그리기
sns.pairplot(data = crime_anal_norm,
             vars = ['강도', '살인', '폭력'],
             kind = 'reg',
             size = 3)
plt.title('강도, 살인, 폭력간의 상관관계: pairplot')
plt.show()

# 인구수와 CCTV개수, 그리고 살인과 강도에 대한 상관관계 그래프 그리기
sns.pairplot(data = crime_anal_norm,
             x_vars = ['인구수', 'CCTV'],
             y_vars = ['살인', '강도'],
             kind = 'reg',
             size = 3)
plt.title('인구수, CCTV, 살인, 강도 상관관계: pairplot')
plt.show()

# 인구수와 CCTV개수, 그리고 살인검거율, 폭력검거율 대한 상관관계 그래프 그리기
sns.pairplot(crime_anal_norm,
             x_vars = ['인구수', 'CCTV'],
             y_vars = ['살인검거율', '폭력검거율'],
             kind = 'reg',
             size = 3)
plt.title('인구수, CCTV, 살인, 강동 상관관계: pairplot')
plt.show()

# 검거율의 합계인 검거 항목 최고 값을 100으로 한정하고 그 값으로 정렬하기
tmp_max = crime_anal_norm['검거'].max()
crime_anal_norm['검거'] = crime_anal_norm['검거'] / tmp_max * 100
crime_anal_norm_sort = crime_anal_norm.sort_values(by = '검거', ascending = False)

# heatmap 그래프 그리기
target_col = ['강간검거율', '강도검거율', '살인검거율', '절도검거율', '폭력검거율']

plt.figure(figsize = (10, 10))
sns.heatmap(data = crime_anal_norm_sort[target_col],
            annot = True,
            fmt = 'f',
            linewidths = .5)
plt.title('범죄 검거 비율(정규화된 검거의 합으로 정렬')
plt.show()

# 발생건수의 합으로 정렬해서 heatmap 그래프 그리기
target_col = ['강간', '강도', '살인', '절도', '폭력', '범죄']

crime_anal_norm['범죄'] = crime_anal_norm['범죄'] / 5   # 범죄는 다섯개 합한 값임
crime_anal_norm_sort = crime_anal_norm.sort_values(by = '범죄', ascending = False)

plt.figure(figsize = (10,10))
sns.heatmap(crime_anal_norm_sort[target_col],
            annot=True,
            fmt='f',
            linewidths=.5,
            cmap='RdPu')
plt.title('범죄비율 (정규화된 발생 건수로 정렬)')
plt.show()

