### Array operation
import numpy as np

## Operations btw arrays (기본적인 사칙 연산 지원)
test_a = np.array([[1, 2, 3],
                   [4, 5, 6]], float)

test_a + test_a
test_a - test_a
test_a * test_a      # Matrix element들 간의 곱, shape이 같을 때


## Dot product
test_a = np.arange(1, 7).reshape(2, 3)     # Matrix 곱셈
test_b = np.arange(7, 13).reshape(3, 2)    # (l,m) x (m,n)  (l,n)
test_a.dot(test_b)


## Transpose
test_a = np.arange(1, 7).reshape(2, 3)
test_a.tranpose()
test_a.T


## Broadcasting (Shape이 다른 배열간 연산 지원)
test_matrix = np.array([[1, 2, 3],
                        [4, 5, 6]], float)
scalar = 3
test_matrix + scalar              # Matrix - Scalar 덧셈
test_matrix - scalar
test_matrix * scalar
test_matrix / scalar              # 나누기
test_matrix // scalar             # 몫
test_matrix ** 2                  # 제곱

# Matrix와 Vector 간의 연산도 가능
test_matrix = np.arange(1, 13).reshape(4, 3)
test_vector = np.arange(10, 40, 10)

test_matrix + test_vector