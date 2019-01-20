import re
import requests as req
import lxml.html

def main():
    # 여러 페이지에서 크롤링 => session 사용.
    session = req.Session()
    res = session.get('http://www.hanbit.co.kr/store/books/new_book_list.html')
    urls = scrape_list_page(res)
    
    for url in urls:
        res = session.get(url) # session을 이용해 상세페이지를 추출.
        ebook = scrape_detail_page(res) # 상세페이지에서 상세정보를 추출.
        print(ebook) # 책 관련 정보를 추출.
        break # 책 한권이 제대로 출력되는지 확인 후 종료.

def scrape_list_page(res):
    root = lxml.html.fromstring(res.content)
    root.make_links_absolute(res.url)

    for a in root.cssselect('.view_box .book_tit a'):
        url = a.get('href')
        yield url
def scrape_detail_page(res):
    """
    상세페이지의 res에서 책 정보를 dict 형태로 추출.
    """
    root = lxml.html.fromstring(res.content)
    ebook = {
        'url': res.url,
        'title': root.cssselect('.store_product_info_box h3')[0].text_content(),
        'price': root.cssselect('.pbr strong')[0].text_content(),
        'content': [normalize_spaces(p.text_content()) for p in root.cssselect('#tabs_3 .hanbit_edit_view p') if normalize_spaces(p.text_content()) != '']
    }

    return ebook

def normalize_spaces(s):
    """
    연결돼 있는 공백을 하나의 공백으로 변경
    """
    return re.sub(r'\s+', ' ', s).strip()

if __name__ == '__main__':
    main()
