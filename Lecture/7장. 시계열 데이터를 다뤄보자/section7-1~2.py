### sextion 7-1 (Numpy의 polyfit으로 회귀(regression)분석하기

# 모듈 준비하기
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import pandas_datareader.data as web
import numpy as np
import matplotlib.pyplot as plt

from fbprophet import Prophet
from datetime import datetime

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



# 데이터 불러오기
pinkwink_web = pd.read_csv('Lecture/Data/08. PinkWink Web Traffic.csv',
                           encoding='utf-8',
                           thousands=',',
                           names = ['date','hit'],
                           index_col=0)
pinkwink_web = pinkwink_web[pinkwink_web['hit'].notnull()]
pinkwink_web.head()

# 시계열 그래프 그려보기
pinkwink_web['hit'].plot(figsize=(12,4),
                         grid=True)

# 시간축을 만들고 트래픽의 자료를 traffic변수에 저장
time = np.arange(0,len(pinkwink_web))
traffic = pinkwink_web['hit'].values

fx = np.linspace(0, time[-1], 1000)

# 적합성을 확인하는 과정을 위해 참 값과 비교해서 에러를 계산
def error(f, x, y):
    return np.sqrt(np.mean((f(x)-y)**2))


# polyfit과 polyld를 사용해서 함수로 표현
fp1 = np.polyfit(time, traffic, 1)
f1 = np.poly1d(fp1)

f2p = np.polyfit(time, traffic, 2)
f2 = np.poly1d(f2p)

f3p = np.polyfit(time, traffic, 3)
f3 = np.poly1d(f3p)

f15p = np.polyfit(time, traffic, 15)
f15 = np.poly1d(f15p)

print(error(f1, time, traffic))
print(error(f2, time, traffic))
print(error(f3, time, traffic))
print(error(f15, time, traffic))

# 1, 2, 3, 15차 그래프 그려보기
plt.figure(figsize=(10,6))
plt.scatter(time, traffic, s=10)

plt.plot(fx, f1(fx), lw=4, label='f1')
plt.plot(fx, f2(fx), lw=4, label='f2')
plt.plot(fx, f3(fx), lw=4, label='f3')
plt.plot(fx, f15(fx), lw=4, label='f15')

plt.grid(True, linestyle='-', color='0.75')

plt.legend(loc=2)
plt.show()

# 결론: 1, 2, 3 가 거의 비슷해서 1차 사용하는것이 나음
#      15차 함수를 사용해서 표현하는 것은 과적합



### sextion 7-2 (Prophet 모듈을 이용한 forecast 예측)

# 날짜(index)와 방문수(hit)만 따로 저장
df = pd.DataFrame({'ds':pinkwink_web.index, 'y':pinkwink_web['hit']})
df.reset_index(inplace=True)

# to_datetime 명령으로 날짜라고 선언
df['ds'] =  pd.to_datetime(df['ds'], format="%y. %m. %d.")

del df['date']

# 주기성이 연(yearly_seasonality)라고 알려줌
m = Prophet(yearly_seasonality=True, daily_seasonality=True)
m.fit(df);

# 60일간의 데이터를 예측하기 위해 make_future_dataframe명령
future = m.make_future_dataframe(periods=60)
future.tail()

# 예측한 데이터를 forecast변수에 저장
forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

# 그래프 그려보기
m.plot(forecast)

# plot_components 명령으로 그려보기
m.plot_components(forecast);