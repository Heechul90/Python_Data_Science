### section 1-7 (파이썬의대표 시각화 도구 - Matplotlib)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline              # 그래프의 결과를 출력 세션에 나타나게 하는 설정


plt.figure()
plt.plot([1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0])
plt.show()
plt.plot([1, 2, 3])