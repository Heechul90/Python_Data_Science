### 2. ndarray(Numpy Dimensional Array)

## import
import numpy as np           # 표준화되어 있음


## Array 생성
test_array = np.array([1, 4,5, 8], float)

print(test_array)
print(test_array[3])
print(test_array.dtype)      # Array 전체의 데이터 타입을 반환함
print(test_array.shape)      # Array 의 shape(차원 구성)을 반환함

# numpy는 np.array 함수를 활용하여 배열을 생성함  ndarray
# numpy는 하나의 데이터 타입만 배열에 넣을 수 있음
# List와 가장 큰 차이점, Dynamic typing(예, [1, 2, “5”, 4.2]) not supported
# C의 Array를 사용하여 배열을 생성함

