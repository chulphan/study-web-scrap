from voluptuous import Schema, Match

# 다음 4개의 규칙을 갖는 스키마를 정의
schema = Schema({
    'name': str,
    'price': Match(r'^[0-9,]+$'),

}, required=True) # dict의 키는 필수.

# Schema 객체는 함수처럼 호출해서 사용.
# 매개변수에 대상을 넣으면 유효성 검사를 수행.
schema({
    'name': '포도',
    'price': '3,000',
})

schema({
    'name': None,
    'price': '3,000'
})


