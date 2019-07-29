### 11. 연습 문제
import numpy as np

## 1. 길이가 10인 0-벡터를 만드세요.
one = np.zeros(shape = (10, ), dtype = np.int8)
one

# 풀이
np.zeros(10)


## 2. 길이가 10이며 다섯번째 원소만 1이고 나머지 원소는 모두 0인 벡터를 만드세요.
two = np.eye(1, 10, k= 4)

# 풀이
np.where(np.arange(10) == 4, 1, 0)
np.eye(1, 10, k = 4)


## 3. 10 부터 49까지의 값을 가지는 벡터를 만드세요.
three = np.arange(10, 50).reshape(1, 40)

# 풀이
np.arange(10, 50)


## 4. 위(3번) 벡터의 순서를 바꾸세요.
four = three.transpose()

# 풀이
np.arange(49, 9, -1)


## 5. 0부터 8까지의 값을 가지는 3x3 행렬을 만드세요.
five = np.arange(9).reshape(3, 3)

# 풀이
np.arange(9).reshape(3, 3)


## 6. 벡터 [1,2,0,0,4,0] 에서 원소의 값이 0이 아닌 원소만 선택한 벡터를 만드세요.
six = np.array([1, 2, 0, 0, 4, 0], int)
six[six != 0]

# 풀이
a = np.array([1, 2, 0, 0, 4, 0], int)
a[a != 0]


## 7. 3x3 단위 행렬(identity matrix)을 만드세요
np.identity(n = 3, dtype = int)

# 풀이
np.identity(3)


## 8. 난수 원소를 가지는 3x3 행렬을 만드세요
eight = np.random.uniform(0, 1, 9).reshape(3,3)

# 풀이
a = np.random.random(9).reshape(3, 3)


## 9. 위(8번)에서 만든 난수 행렬에서 최대값/최소값 원소를 찾으세요.
nine = np.argmax(eight), np.argmin(eight)
nine

# 풀이
a[np.argmax(a) // 3, np.argmax(a) % 3], np.argmin(a)
np.argmax(a), np.argmin(a)


## 10. 위(8번)에서 만든 난수 행렬에서 행 평균, 열 평균을 계산하세요.
eight.mean(axis = 0)
eight.mean(axis = 1)

# 풀이
np.mean(a, axis = 0)
a.mean(axis = 0)
np.mean(a, axis = 1)
a.mean(axis = 1)