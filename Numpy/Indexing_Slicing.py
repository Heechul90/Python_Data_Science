### 4. Indexing & slicing
import numpy as np

## Indexing
# List와 달리 이차원 배열에서 [0, 0]과 같은 표기법을 제공함
# Matrix일 경우 앞은 행(row) 뒤는 열(column)을 의미함

a = np.array([[1, 2, 3],
              [4, 5, 6]], int)
print(a)
print(a[0, 0])     # 2차원 배열 표기법 1
print(a[0][0])     # 2차원 배열 표기법 2
a[0, 0]


## Slicing
# List와 달리 행과 열 부분을 나눠서 slicing이 가능함
# Matrix의 부분 집합을 추출할 때 유용함

a = np.array([[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10]], int)
print(a)
a[:, 2:]     # 전체 row의 2열 이상
a[1, 1:3]    # row 1의 1~2열
a[1:3]       # 1 row ~ 2 row 전체, column은 무시
a[:, ::2]    # step 가능