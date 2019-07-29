### 10. Numpy data I/O
import numpy as np

## loadtxt & savetxt (Text type의 데이터를 읽고 저장하는 기능)
a = np.loadtxt('Numpy/filename.txt')              # 파일 호출
a[:10]

a_int = a.astype(int)
a_int[:3]

np.savetxt('Numpy/filename.csv', a_int)   # csv 파일로 저장


## numpy object - npy
# Numpy object(pickle) 형태로 데이터를 저장하고 불러옴
# Binary 파일 형태

np.save('npy_test', arr = a_int)
npy_array = np.load(file = 'npy_test.npy')

