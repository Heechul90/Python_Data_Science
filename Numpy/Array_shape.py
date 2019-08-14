### 3. Array shape
import numpy as np

## Vector (1차원)
test_array = np.array([1, 4, 5, 8], float)

# shape은 (4, ) : 1차원에 4개의 element가 있는 벡터
test_array.shape


## Matrix (2차원)
matrix = [[1,2,5,8],
          [2,3,4,9],
          [4,5,6,7]]

# shape은 (3, 4) : 행이 3개, 열이 4개인 매트릭스
np.array(matrix, int).shape


## Tensor (3차원)

tensor = [[[1,2,5,8], [2,3,4,9], [4,5,6,7]],
          [[1,2,5,8], [2,3,4,9], [4,5,6,7]],
          [[1,2,5,8], [2,3,4,9], [4,5,6,7]],
          [[1,2,5,8], [2,3,4,9], [4,5,6,7]]]

# shape은 (4, 3, 4) : 평면이 4개, 행이 3개, 열이 4개인 텐서

np.array(tensor, int).shape


## ndim % size

np.array(tensor, int).ndim     # 3, number of dimension
np.array(tensor, int).size     # 48


## dtype
# Single element가 가지는 데이터 타입
# C의 데이터 타입과 호환
# nbytes – ndarray object의 메모리 크기를 바이트 단위로 반환함

np.array([[1, 2, 3], [4.5, '5', '6']], dtype = np.float32)


## reshape
# Array의 shape을 변경함 (element의 개수는 동일)

test_matrix = [[1, 2, 3, 4],
               [5, 6, 7, 8]]
np.array(test_matrix).shape
np.array(test_matrix).reshape(8,)
np.array(test_matrix).reshape(8,).shape

# Array의 shape을 변경함 (element의 개수는 동일)
# Array의 size만 같다면 다차원으로 자유로이 변형가능

np.array(test_matrix).reshape(2, 4).shape
np.array(test_matrix).reshape(-1, 2).shape   # -1: size를 기반으로 row 개수 선정
np.array(test_matrix).reshape(2, 2, 2).shape


## flatten
# 다차원 array를 1차원 array로 변환
test_matrix = [[[1,2,3,4],
                [5,6,7,8]],
               [[2,3,4,5],
                [6,7,8,9]]]
np.array(test_matrix).flatten()
