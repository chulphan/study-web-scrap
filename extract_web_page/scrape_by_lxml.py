import lxml.html
from urllib.request import urlopen

# HTML 파일을 읽어들이고, getroot() 메서드로 HtmlElement 객체를 생성함.
tree = lxml.html.parse(urlopen('https://www.ntis.go.kr/rndgate/eg/un/ra/mng.do'))
html = tree.getroot()

# cssselect() 메서드로 a 요소의 리스트를 추출하고 반복을 돌림.
for a in html.cssselect('a'):
    # href속성과 글자를 추출.
    print(a.get('href'), a.text)


