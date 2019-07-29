### 5. Creation Funtion
import numpy as np

## arange
# List와 달리 행과 열 부분을 나눠서 slicing이 가능함
# Matrix의 부분 집합을 추출할 때 유용함

np.arange(10)                   # arange - List의 range와 같은 효과
np.arange(0, 5, 0.5)            # floating point도 표시가능
np.arange(0, 5, 0.5).tolist()   # List로 만들 수 있음
np.arange(30).reshape(5,6)      # size 가 같으면 가능


## ones, zeros and empty
# empty – shape만 주어지고 비어있는 ndarray 생성

np.zeros(shape = (10, ), dtype = np.int8)  # 원소가 10개인 벡터 생성
np.ones((2, 5))                            # 값이 1인 matrix 생성
np.empty((3, 5))                           # 메모리가 초기화되어 있지 않음

## Somethong like
# 기존 ndarray의 shape 크기 만큼 1, 0 또는 empty array를 반환

test_matrix = np.arange(30).reshape(5, 6)
np.ones_like(test_matrix)
np.zeros_like(test_matrix)


## idendity (단위 행렬 생성)
np.identity(n = 3, dtype = np.int8)        # n: number of rows
np.identity(5)


## eye (대각선이 1인 행렬)
np.eye(N = 3, M = 5, dtype = np.int8)
np.eye(5)
np.eye(3, 5, k = 2)                        # K: start index


## diag (대각 행렬의 값을 추출)
matrix = np.arange(9).reshape(3, 3)
np.diag(matrix)
np.diag(matrix, k = 1)                     # K: start index


## Random sampling(데이터 분포에 따른 sampling으로 array를 생성)

np.random.seed(seed = 1000) # 시드로 난수 생성 초기값 지정

# uniform(최소, 최대, 개수)
np.random.uniform(0, 1, 10).reshape(2, 5) # 균등 분포

# normal(평균, 표준편차, 개수)
np.random.normal(0, 1, 10).reshape(2, 5)  # 정규 분포

# 이항분포
# np.random.binomial(n, p, size)

# 포아송 분포
# np.random.poisson(lam. size)

# t-분포
# np.random.standard_t(df, size)

# F-분포
# np.random.f(dfnum, dfden, size)

import matplotlib.pyplot as plt
rand_norm = np.random.normal(0., 3., size = 1000) # 평균, 표준편차
count, bins, ignored = plt.hist(rand_norm, normed = False)

rand_pois = np.random.poisson(lam = 20, size = 1000)
unique, counts = np.unique(rand_pois, return_counts = True)
np.asarray((unique, counts)).T
plt.bar(unique, counts, width = 0.5, color = 'red', align = 'center')