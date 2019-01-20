from bs4 import BeautifulSoup
from urllib.request import urlopen

#with open('https://www.ntis.go.kr') as f:
#    soup = BeautifulSoup(f, 'html.parser')

soup = BeautifulSoup(urlopen("https://www.ntis.go.kr/rndgate/eg/un/ra/mng.do"), 'html.parser')

for a in soup.find_all('a'):
    print(a.get('href'), a.text)
