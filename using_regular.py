# 정규표현식을 이용한 스크레이핑
# 제대로 마크업 되지 않은 웹페이지에서도 문자열의 특징을 파악하여 쉽게 스크레이핑 할 수 있다.
# unescape는 escape로 이스케이핑 된 문자열을 정상적인 문자열로 되돌려 주는 역할을 함.

import re
from html import unescape

# 이전 절에서 다운로드 한 파일을 열고 html이라는 변수에 저장.
with open('dp.html') as f:
    html = f.read()

# re.findall() 을 사용해 도서 하나에 해당하는 HTML을 추출.
for partial_html in re.findall(r'<td class="left"><a.*?</td>', html, re.DOTALL):
# 도서의 URL을 추출.
    url = re.search(r'<a href="(.*?)">', partial_html).group(1)
    url = 'http://hanbit.co.kr' + url
# 태그를 제거해서 도서의 제목을 추출.
    title = re.sub(r'<.*?>', '', partial_html)
    title = unescape(title)
    print('url: ', url)
    print('title: ', title)
    print('----')


