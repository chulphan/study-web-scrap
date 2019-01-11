import sys
from urllib.request import urlopen

f = urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109")

encoding = f.info().get_content_charset(failobj='utf-8')

print('encoding: ', encoding, file=sys.stderr)

text = f.read().decode(encoding)
print(text)
