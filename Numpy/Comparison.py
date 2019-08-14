### Comparison
import numpy as np

## All & Any
a = np.arange(10)

np.any(a > 5)     # any: 하나라도 조건에 만족하면 True
np.any(a < 0)

np.all(a > 5)     # all: 모두가 조건을 만족해야 True
np.all(a < 10)

a > 5

test_a = np.array([1, 3, 0], float)
test_b = np.array([5, 2, 1], float)
test_a > test_b     # 배열의 크기가 동일할 때 원소간 비교 가능

test_a == test_b
(test_a > test_b).any()


## Logical operation
a = np.array([1, 3, 0], float)
b = np.logical_and(a > 0, a < 3)  # and 조건

c = np.logical_not(b)
np.logical_or(b, c)
np.logical_and(b, c)

# 0보다 크면 True면 3, False면 2
np.where(a > 0, 3, 2)             # where(condition, True, False

a = np.arange(10, 20)
np.where(a > 15)                  # index 값 반환

a = np.array([1, np.NaN, np.Inf], float)
np.isnan(a)                       # is Not a Number?
np.isinf(a)                       # in finite Number?


## argmax & argmin (array내 최대값 또는 최소값의 index를 리턴)
a = np.array([1, 2, 4, 5, 8, 78, 23, 3])
np.argmax(a), np.argmin(a)

a = np.array([[1, 2, 4, 7],
              [9, 88, 6, 45],
              [8, 78, 23, 3]])
np.argmax(a, axis = 1)
np.argmin(a, axis = 1)

np.argmax(a, axis = 0)
np.argmin(a, axis = 1)