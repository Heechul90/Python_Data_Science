### 6. Operation function
import numpy as np

## Sum
test_array = np.arange(1, 11)
test_array.sum(dtype = np.float)


## Axis
# 모든 operation function을 실행할 때, 기준이 되는 dimension 축

test_array = np.arange(1, 13).reshape(3, 4)
test_array.sum(axis = 1)
test_array.sum(axis = 0)


## mean & std

test_array = np.arange(1, 13).reshape(3, 4)
test_array.mean()             # 평균(mean)
test_array.mean(axis = 0)
test_array.mean(axis = 1)

test_array.std()              # 표준편차(standard deviation)
test_array.std(axis = 0)
test_array.std(axis = 1)


## Mathemtical functions
# 지수 함수: exp, expml, exp2, log, log10, loglp, log2, power, sqrt
# 삼각 함수: sin, cos, tan, arcsin, arccos, arctan
# Hyperbolic: shnh, cosh, tanh, arcsinh, arccosh, arctanh

np.exp(test_array)
np.sqrt(test_array)


## Concatenate (Numpy array를 합치는 함수)
a = np.arange(1, 5).reshape(2, 2)
b = np.array([[5, 6]])

np.vstack((a, b))                    # 행으로 붙임(밑으로)
np.concatenate((a, b), axis = 0)     # 위의 결과와 동일

a = np.arange(1, 4).reshape(3, 1)
b = np.arange(2, 5).reshape(3, 1)
np.hstack((a, b))                    # 열로 붙임(옆으로)
np.concatenate((a, b), axis = 1)

a = np.arange(1, 5).reshape(2, 2)
b = np.arange(5, 7).reshape(1, 2)
np.concatenate((a, b.T), axis = 1)   # T: Transpose