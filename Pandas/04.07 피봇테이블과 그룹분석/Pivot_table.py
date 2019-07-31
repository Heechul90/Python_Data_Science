### 피봇테이블과 그룹분석

import pandas as pd
import numpy as np

## pivot_table
## pivot_table 명령은 groupby 명령처럼 그룹분석을 하지만
## 최종적으로는 pivot 명령처럼 피봇테이블을 만든다.
## 즉 groupby 명령의 결과에 unstack을 자동 적용하여 2차원적인 형태로 변형한다

# pivot_table(data,                   # 분석할 데이터프레임 (메서드일 때는 필요하지 않음)
#             values=None,            # 분석할 데이터프레임에서 분석할 열
#             index=None,             # 행 인덱스로 들어갈 키 열 또는 키 열의 리스트
#             columns=None,           # 열 인덱스로 들어갈 키 열 또는 키 열의 리스트
#             aggfunc='mean',         # 분석 메서드
#             fill_value=None,        # NaN 대체 값
#             margins=False,          # 모든 데이터를 분석한 결과를 오른쪽과 아래에 붙일지 여부
#             margins_name='All')     # 마진 열(행)의 이름

# 만약 조건에 따른 데이터가 유일하게 선택되지 않으면 그룹연산을 하며
# 이 때 aggfunc 인수로 정의된 함수를 수행하여 대표값을 계산

# pivot_table를 메서드로 사용할 때는 객체 자체가 데이터가 되므로 data 인수가 필요하지 않다

data = {
    "도시": ["서울", "서울", "서울", "부산", "부산", "부산", "인천", "인천"],
    "연도": ["2015", "2010", "2005", "2015", "2010", "2005", "2015", "2010"],
    "인구": [9904312, 9631482, 9762546, 3448737, 3393191, 3512547, 2890451, 263203],
    "지역": ["수도권", "수도권", "수도권", "경상권", "경상권", "경상권", "수도권", "수도권"]
}
columns = ["도시", "연도", "인구", "지역"]
df1 = pd.DataFrame(data, columns=columns)
df1

df1.pivot_table('인구', '도시', '연도')


# margins=True 인수를 주면 aggfunc로 주어진 분석 방법을
# 해당 열의 모든 데이터,
# 해당 행의 모든 데이터
# 그리고 전체 데이터에 대해 적용한 결과를 같이 보여준다.
# aggfunc가 주어지지 않았으면 평균을 계산한다.
df1.pivot_table('인구', '도시', '연도',
                margins = True,
                margins_name = '합계')     # aggfunc 주어지지 않아 평균으로 계산됨
df1['인구'].mean()


# 행 인덱스나 열 인덱스에 리스트를 넣으면 다중 인덱스 테이블을 만든다
df1.pivot_table('인구', index = ['연도', '도시'])



## TIP 데이터 예제
## 식당에서 식사 후 내는 팁(tip)과 관련된 데이터를 이용하여
## 좀더 구체적으로 그룹분석 방법을 살펴본다.
## 우선 Seaborn 패키지에 설치된 샘플 데이터를 로드한다.

# total_bill: 식사대금
# tip:        팁
# sex:        성별
# smoker:     흡연/금연 여부
# day:        요일
# time:       시간
# size:       인원

import seaborn as sns

tips = sns.load_dataset('tips')
tips.tail()

# 식사 대금 대비 팁의 비율이 어떤 경우에 가장 높아지지는 찾는 것이다.
# 우선 식사대금와 팁의 비율을 나타내는 tip_pct를 추가
tips['tip_pct'] = tips['tip'] / tips['total_bill']
tips.tail()

# 각 열의 데이터에 대해 간단히 분포를 알아본다.
tips.describe()



## 그룹별 통계
# 성별로 나누어 데이터 갯수를 세어본다.
tips.groupby('sex').count()

# 데이터 갯수의 경우 NaN 데이터가 없다면 모두 같은 값이 나올 것이다.
# 이 때는 size 명령을 사용하면 더 간단히 표시된다.
# size 명령은 NaN이 있어도 상관하지 않는다.
tips.groupby('sex').size()

# 성별과 흡연유무로 나누어 데이터의 갯수를 알아본다.
tips.groupby(['sex', 'smoker']).size()

# 좀 더 보기 좋도록 피봇 데이블 형태로 바꿀 수도 있다.
tips.pivot_table('tip_pct', 'sex', 'smoker',
                 aggfunc = 'count',
                 margins = True,
                 margins_name = 'All')


# 성별과 흡연 여부에 따른 평균 팁 비율
tips.groupby('sex')[['tip_pct']].mean()
tips.groupby('sex').mean()['tip_pct']

tips.groupby('smoker')[['tip_pct']].mean()
tips.groupby('smoker').mean()['tip_pct']


# pivot_table 명령을 사용할 수도 있다.
tips.pivot_table('tip_pct', 'sex')
tips.pivot_table('tip_pct', ['sex', 'smoker'])
tips.pivot_table('tip_pct', 'sex', 'smoker')


# 이 데이터에는 평균을 제외한 분산(variance) 등의 다른 통계값이 없으므로
# describe 명령으로 여러가지 통계값을 한 번에 알아본다.
tips.groupby('sex')[['tip_pct']].describe()
tips.groupby('smoker')[['tip_pct']].describe()
tips.groupby(['sex', 'smoker'])[['tip_pct']].describe()


# 각 그룹에서 가장 많은 팁과 가장 적은 팁의 차이를 알아보자.
# 이 계산을 해 줄 수 있는 그룹연산 함수가 없으므로 함수를 직접 만들고 agg 메서드를 사용
def peak_to_peak(x):
    return x.max() - x.min()

tips.groupby(['sex', 'smoker'])[['tip']].agg(peak_to_peak)

# 여러가지 그룹연산을 동시에 하고 싶다면 다음과 같이 리스트를 이용
tips.groupby(['sex', 'smoker']).agg(['mean', peak_to_peak])[['total_bill']]

# 데이터 열마다 다른 연산을 하고 싶다면 열 라벨과 연산 이름(또는 함수)를 딕셔너리로 넣는다.
tips.groupby(['sex', 'smoker']).agg({'tip_pct': 'mean',
                                     'total_bill': peak_to_peak})

# pivot_table 명령으로 더 복잡한 분석을 한 예
tips.pivot_table(values = ['tip_pct', 'size'],
                 index = ['sex', 'day'],
                 columns = 'smoker')

tips.pivot_table(values = 'size',
                 index = ['time', 'sex', 'smoker'],
                 columns = 'day',
                 aggfunc = 'sum',
                 fill_value = 0)

# pivot_table(data,                   # 분석할 데이터프레임 (메서드일 때는 필요하지 않음)
#             values=None,            # 분석할 데이터프레임에서 분석할 열
#             index=None,             # 행 인덱스로 들어갈 키 열 또는 키 열의 리스트
#             columns=None,           # 열 인덱스로 들어갈 키 열 또는 키 열의 리스트
#             aggfunc='mean',         # 분석 메서드
#             fill_value=None,        # NaN 대체 값
#             margins=False,          # 모든 데이터를 분석한 결과를 오른쪽과 아래에 붙일지 여부
#             margins_name='All')     # 마진 열(행)의 이름