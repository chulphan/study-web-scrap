import re
import requests as req
import lxml.html

def main():
    session = req.Session()
    res = session.get('https://www.ntis.go.kr/rndgate/eg/un/ra/mng.do')

    urls = scrape_list_page(res)

    for url in urls:
        res = session.get(url)
        info = scrape_detail_page(res)
        print(info)

def scrape_list_page(res):
    root = lxml.html.fromstring(res.content)
    root.make_links_absolute(res.url)

    for a in root.cssselect('.left a'):
        url = a.get('href')
        yield url

def scrape_detail_page(res):
    root = lxml.html.fromstring(res.content)
    info = {
        'url': res.url,
        'type': normalize_spaces(root.cssselect('.summary1 li')[0].text_content()),
        'part': normalize_spaces(root.cssselect('.summary1 li')[1].text_content()),
        'announce_part': normalize_spaces(root.cssselect('.summary1 li')[2].text_content()),
        'announce_date': normalize_spaces(root.cssselect('.summary2 li')[0].text_content()),
        'create_date': normalize_spaces(root.cssselect('.summary2 li')[1].text_content()),
        'end_date': normalize_spaces(root.cssselect('.summary2 li')[2].text_content()),
        'end_time': normalize_spaces(root.cssselect('.summary2 li')[3].text_content()),
        'class': normalize_spaces(root.cssselect('.summary1 li')[3].text_content()),
        'price': normalize_spaces(root.cssselect('.summary1 li')[4].text_content()),
        'tel': normalize_spaces(root.cssselect('.summary2 li')[4].text_content()),
        'business_name': normalize_spaces(root.cssselect('.summary1 li')[5].text_content()),
        'title': normalize_spaces(root.cssselect('.ditail_tit')[0].text_content()),
        'content': [normalize_spaces(p.text_content()) for p in root.cssselect('.notice_cont') if normalize_spaces(p.text_content()) != '']
        
    }
    return info

def normalize_spaces(s):
    eliminate_span = s
    if re.match(r'<.*?>.*?</.*?>', eliminate_span):
        eliminate_span = re.sub(r'<.*?>.*?</.*?>', ' ', eliminate_span)
        print('@@@@@@@', eliminate_span)
    return re.sub(r'\s+', ' ', eliminate_span).strip()


if __name__ == '__main__':
    main()
