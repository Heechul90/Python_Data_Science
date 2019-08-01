### section 1-7 (파이썬의대표 시각화 도구 - Matplotlib)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline              # 그래프의 결과를 출력 세션에 나타나게 하는 설정


plt.figure()
plt.plot([1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0])
plt.show()
plt.plot([1, 2, 3])

# numpy를 이용해서 sin을 만들고 그래프 그리기
t = np.arange(0, 12, 0.01)    # 0부터 12까지 0.01 간격으로 데이터 생성
y = np.sin(t)                 # np.sin에 t값을 넣어 y를 생성

plt.figure(figsize = (10, 6))
plt.plot(t, y)
plt.show


# 옵션 사용하기
plt.figure(figsize = (10, 6))         # 화면 크기 조정
plt.plot(t, y)                        # 데이터 입력
plt.grid()                            # 배경(격자 무늬)
plt.xlabel('Time')                    # x축 label
plt.ylabel('Amplitud')                # y축 label
plt.title('Example of sinewave')      # 그래프 title
plt.show()


# 두개의 그래프 그리기
plt.figure(figsize = (10,6))
plt.plot(t, np.sin(t), label = 'sin')  # label 옵션으로 텍스트 수정
plt.plot(t, np.cos(t), label = 'cos')
plt.grid()                             # 명령을 주고 화면에 시각화
plt.legend()
plt.xlabel('Time')                     # x축 label
plt.ylabel('Amplitud')                 # y축 label
plt.title('Example of sinewave')       # 그래프 title
plt.show()


# 옵션 추가
plt.figure(figsize = (10, 6))
plt.plot(t, np.sin(t), lw = 3, label = 'sin')       # lw 선의 굵기
plt.plot(t, np.cos(t), color = 'r', label = 'cos')  # color 색 지정
plt.grid()                             # 명령을 주고 화면에 시각화
plt.legend()
plt.xlabel('Time')                     # x축 label
plt.ylabel('Amplitud')                 # y축 label
plt.title('Example of sinewave')       # 그래프 title
plt.show()


# 그래프 그리기
t = [0, 1, 2, 3, 4, 5, 6]
y = [1, 4, 5, 8, 9, 5, 3]


# lw, color 옵션 사용
plt.figure(figsize = (10, 6))
plt.plot(t, y,
         lw = 2,                       # 선의 굵기
         color = 'green')              # 선 색 지정
plt.show()


# color, linestyle 옵션 사용
plt.figure(figsize = (10, 6))
plt.plot(t, y,
         color = 'green',              # 선 색 지정
         linestyle = 'dashed')         # linestyle 옵션으로 선 스타일 지정
plt.show()


# color, linestyle, marker 옵션 사용
plt.figure(figsize = (10, 6))
plt.plot(t, y,
         color = 'green',              # 선 색 지정
         linestyle = 'dashed',         # linestyle 옵션으로 선 스타일 지정
         marker = 'o')                 # marker 옵션으로 마킹
plt.show()


# color, linestyle, marker 옵션 사용
# markerfacecolor 옵션과 markersize 옵션으로 크기와 색상 지정
plt.figure(figsize = (10, 6))
plt.plot(t, y,
         color = 'green',
         linestyle = 'dashed',
         marker = 'o',
         markerfacecolor = 'blue',     # marker 색 지정
         markersize = 12)              # marker 크기 지정
plt.show()


# 그래프 그리기
t = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([9, 8, 7, 9, 8, 3, 2, 4, 3, 4])


# scatter 명령
plt.figure(figsize = (10, 6))
plt.scatter(t, y)
plt.show()


# marker 옵션 사용
plt.figure(figsize = (10, 6))
plt.scatter(t, y, marker = '>')
plt.show()


# x축 값인 t에 따라 색상을 바꾸는 color map 옵션 사용
colormap = t

plt.figure(figsize = (10, 6))
plt.scatter(t, y,
            s = 45,          # marker의 크기 조정
            c = colormap,    # color map 지정
            marker = '>')    # 마킹
plt.colorbar()               # color map bar
plt.show()


# numpy의 랜덤변수 함수를 이용해서 데이터 만들기
# loc 옵션으로 평균값과 scale 옵션으로 표준편차 지정
s1 = np.random.normal(loc = 0, scale = 1, size =1000)     # 평균0, 표준편차1, 크기1000
s2 = np.random.normal(loc = 5, scale = 0.5, size =1000)   # 평균5, 표준편차0.5, 크기1000
s3 = np.random.normal(loc = 10, scale = 2, size =1000)    # 평균10, 표준편차2, 크기1000


# 그래프 그리기
plt.figure(figsize = (10,6))
plt.plot(s1, label = 's1')
plt.plot(s2, label = 's2')
plt.plot(s3, label = 's3')
plt.legend()
plt.show()


# boxplot 명령
plt.figure(figsize = (10, 6))
plt.boxplot((s1, s2, s3))
plt.grid()
plt.show()




##### 잘 모르겠어
plt.figure(figsize=(10,6))

plt.subplot(221)
plt.subplot(222)
plt.subplot(212)

plt.show()


plt.figure(figsize=(10,6))

plt.subplot(411)
plt.subplot(423)
plt.subplot(424)
plt.subplot(413)
plt.subplot(414)

plt.show()



t = np.arange(0,5,0.01)

plt.figure(figsize=(10,12))

plt.subplot(411)
plt.plot(t,np.sqrt(t))
plt.grid()

plt.subplot(423)
plt.plot(t,t**2)
plt.grid()

plt.subplot(424)
plt.plot(t,t**3)
plt.grid()

plt.subplot(413)
plt.plot(t,np.sin(t))
plt.grid()

plt.subplot(414)
plt.plot(t,np.cos(t))
plt.grid()

plt.show()