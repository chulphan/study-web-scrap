# -*- coding: utf-8 -*-

# CSV(Comma-Seperated Values) 는 하나의 레코드를 한 줄에 나타내고 각 줄의 값을 쉼표로 구분하는 텍스트 형식.
# 행과 열로 구성되는 2차원 데이터를 저장할 때 사용.

print('rank,city,population')

# join() 메서드의 매개변수로 전달한 list는 str이어야 함.
print(','.join(['1', '상하이', '24150000']))
print(','.join(['2', '카라치', '23500000']))
print(','.join(['3', '베이징', '21516000']))
print(','.join(['4', '텐진', '14722100']))
print(','.join(['5', '이스탄불', '14160467']))

