### Exercise 5-1

import pandas as pd
import numpy as np


## 연습 문제 5-1
## 여러가지 함수를 사용하여 아래 조건에 맞는 그래프를 그린다.

# xlabel, ylabel, title을 모두 갖추고 있어야 한다.
# 하나의 Figure(일단, 그림이라고 이해한다. 아래에 자세한 설명이 있다.)에 3개 이상의 Plot을 그린다.
# 각 Plot은 다른 선, 마크, 색 스타일을 가진다.
# legend는 그래프와 겹치지 않는 곳에 위치 시키도록 한다.

plt.plot([1, 2,3, 4, 5], [11, 25, 11, 3, 9],
         c = 'b',
         lw = 3,
         ls = 'dashed',
         marker = '>',
         ms = 10,
         mec = 'm',
         mew = 2,
         mfc = 'r',
         label="배추")
plt.plot([1, 2,3, 4, 5], [30, 12, 21, 7, 52],
         c = 'b',
         lw = 4,
         ls = '-.',
         marker = '1',
         ms = 15,
         mec = 'y',
         mew = 3,
         mfc = 'g',
         label="상추")
plt.plot([1, 2,3, 4, 5], [9, 35, 14, 2, 15],
         c = 'b',
         lw = 5,
         ls = ':',
         marker = '1',
         ms = 5,
         mec = 'k',
         mew = 4,
         mfc = 'b',
         label="양상추")
plt.xlabel("x축 label")
plt.ylabel("y축 label")
plt.title("title 입니다")
plt.show()






## 연습 문제 5-2
## 여러가지 함수를 사용하여 위와 같이 subplot들로 구성된 그림을 그려보자.
## 모든 subplot에 대해 xlabel, ylabel, title이 있어야 한다.






## 연습 문제 5-3
# 1. Matplotlib 갤러리 웹사이트에서 관심있는 예제 코드를 하나 고른다.
#    http://matplotlib.org/gallery.html


# 2. 예제 코드에 사용된 Matplotlib API 명령의 목록을 만들고
#    Matplotlib 웹사이트에서 관련 링크를 찾아 내용을 정리한다.



# 3. 변형된 형태의 플롯을 만들어본다.