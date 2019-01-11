# ElementTree 모듈 import
from xml.etree import ElementTree

# parse() 함수로 파일을 읽어들이고 ElementTree 객체를 만듦.
tree = ElementTree.parse('weather.xml')

# getroot() 메서드로 XML의 루트 요소를 추출.
root = tree.getroot()

# findall() 메서드로 요소 목록을 추출.
# 태그를 찾는다(자세한 내용은 RSS를 열어서 참고)
for item in root.findall('channel/item/description/body/location/data'):
    # find() 메서드로 요소를 찾고 text 속성으로 값을 추출.
    tm_ef = item.find('tmEf').text
    tmn = item.find('tmn').text
    tmx = item.find('tmx').text
    wf = item.find('wf').text

    print(tm_ef, tmn, tmx, wf) # 출력
