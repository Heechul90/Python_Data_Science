### 9. Boolean & fancy index
import numpy as np

## Boolean index
test_array = np.array([1, 4, 0, 2, 3, 8, 9, 7], float)
test_array > 3

test_array[test_array > 3]     # 조건이 True인 index의 element만 추출

condition = test_array < 3
condition
test_array[test_array < 3]
test_array[condition]


## Fancy index
a = np.array([2, 4, 6, 8], float)
b = np.array([0, 0, 1, 3, 2, 1], int) # 반드시 integer로 선언
a[b]                                  # b 배열의 값을 인덱스로 하여 a의 값들을 추출함

a.take(b)                             # take 함수: bracket index와 같은 효과

a = np.array([[1, 4],
              [9, 16]], float)
b = np.array([0, 0, 1, 1, 1], int)
c = np.array([0, 1, 1, 1, 0], int)

a[b, c]                               # b를 row index, c를 column index로 변환하여 표시
