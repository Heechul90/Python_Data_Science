### 02. Analysis for crime in Seoul - Review

# 패키지, 모듈, 함수 준비하기
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

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