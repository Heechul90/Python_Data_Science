### 시각화 패키지 Matplotlib 소개

# 모듈 준비하기
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import pandas as pd

# 한글 사용하기(둘 중 하나)
mpl.reParams['axes.unicode_minus'] = False
[(f.namn f.fname) for f in fm.fontManager.ttflist if 'Malgun' in f.name]

plt.rcParams["font.family"] = 'NanumBarunGothic'
plt.rcParams["font.size"] = 10
