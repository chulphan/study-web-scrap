import requests
import lxml.html

res = requests.get('http://hanbit.co.kr/store/books/new_book_list.html')

root = lxml.html.fromstring(res.content)

root.make_links_absolute(res.url)

for a in root.cssselect('.view_box .book_tit a'):
    url = a.get('href')
    print(url)
