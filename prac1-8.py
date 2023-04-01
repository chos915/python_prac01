"""
inplace 옵션을 사용하는 대신, 21라인을 df3 = df3.drop(['우현', '인아'])라고 입력해도 결과는 같다. 반환된 객체를 기존 변수에 저장하여 대체하는 방법이다.
다음은 drop() 메소드를 이용하여 열을 삭제하는 방법이다. 반드시 축 옵션을 axis=1로 설정한다. 축 옵션을 누락하거나 잘못 지정하면 오류 메시지가 출력된다.
<예제1-7>의 시험 점수 데이터를 정리한 데이터프레임 df를 다시 사용한다. 비교를 위해 df를 복제하여 df4와 df5를 만든다. df4에서 '수학' 과목의 열 데이터를 삭제하고, df5에서 ['영어', '음악'] 리스트를 전달하여 2 과목의 열 데이터를 삭제한다. 이때 축 옵션(axis=1)을 잊지 않는다.
"""
# -*- coding: utf-8 -*-

import pandas as pd

# DataFrame() 함수로 데이터 프레임 변환, 변수 df에 저장
exam_data = {'수학' : [90, 80, 70], '영어' : [98, 89, 95],
             '음악' : [85, 95, 100], '체육' : [100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df)
print('\n')

# 데이터 프레임 df를 복제하여 변수 df4에 저장. df4의 1개 열(column) 삭제
df4 = df.copy()
df4.drop('수학', axis=1, inplace=True)
print(df4)
print('\n')

# 데이터프레임 df를 복제하여 변수 df5에 저장, df의 2개의 열(column) 삭제
df5 = df.copy()
df5.drop(['영어', '음악'], axis=1, inplace=True)
print(df5)