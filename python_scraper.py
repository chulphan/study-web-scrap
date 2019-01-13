import re
import sqlite3
from urllib.request import urlopen
from html import unescape

def main():
    """
     메인처리.
     fetch(), scrape(), save() 함수를 호출(스크레핑은 나열순으로 이루어 짐.)
    """
    html = fetch("http://www.hanbit.co.kr/store/books/full_book_list.html")
    books = scrape(html)
    save('books.db', books)


def fetch(url):
    """
    매개변수로 전달받은 url을 기반으로 웹페이지를 추출.
    웹페이지의 인코딩 형식은 Content-Type 헤더 기반으로 알아냄.
    반환값: str 자료형의 HTML
    """
    f = urlopen(url)
    # HTTP 헤더를 기반으로 인코딩 형식을 추출.
    encoding = f.info().get_content_charset(failobj='utf-8')
    # 추출한 인코딩 형식을 기반으로 문자열을 디코딩.
    html = f.read().decode(encoding)

    return html

def scrape(html):
    """
    매개변수 html 로 받은 HTML을 기반으로 정규표현식을 사용해 도서정보를 추출.
    반환값: 도서(dict)리스트.
    """

    books = []
    
    #re.findall()을 사용해서 도서 하나에 해당하는 HTML을 추출.
    for partial_html in re.findall(r'<td class="left"><a.*?</td>', html, re.DOTALL):
        # 도서의 URL을 추출.
        url = re.search(r'<a href="(.*?)">', partial_html).group(1)
        url = 'http://www.hanbit.co.kr' + url
        # 태그를 제거해서 도서의 제목을 추출.
        title = re.sub(r'<.*?>', '', partial_html)
        title = unescape(title)

        books.append({'url': url, 'title': title})

    return books

def save(db_path, books):
    """
    매개변수 books로 전달된 도서목록을 SQLite 데이터베이스에 저장.
    데이터베이스의 경로는 매개변수 db_path로 지정한다.
    반환값: None
    """

    # 데이터베이스를 열고 연결을 확립.
    conn = sqlite3.connect(db_path)
    # 커서를 추출.
    cursor = conn.cursor()
    # execute() 메소드로 SQL을 실행.
    # 스크립트를 여러 번 실행할 수 있으므로 기존의 books 테이블을 제거.
    cursor.execute('DROP TABLE IF EXISTS books')
    # books 테이블을 생성.
    cursor.execute('''
        CREATE TABLE books(
            title text,
            url text
        )
    ''')
    # executemany() 메서드를 사용하면 매개변수로 리스트를 지정할 수 있다.
    cursor.executemany('INSERT INTO books VALUES (:title, :url)', books)
    # 변경사항을 커밋.
    conn.commit()
    # 연결종료
    conn.close()

    # python 명령어로 실행한 경우 main()함수를 호출.
    # 이는 모듈로써 다른 파일에서 읽어들였을 때 main() 함수가 호출되지 않게 하는 것.
    # 파이썬 프로그램의 일반적인 작성방법.
if __name__ == '__main__':
    main()

