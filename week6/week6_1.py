import requests
from bs4 import BeautifulSoup

raw = requests.get("https://v4.map.naver.com/",
                    headers={"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

#지도컨테이너: dl.lsnx_det

cont = html.select("dl.lsnx_det")
print(cont)  #비어있음 검색어 입력에 따라 url이 변하지 않음 url과 관련없이 웹페이지 위에서 데이터 불러옴 : 동적페이지

#검사코드에서는 치킨이라는 검색어가 나오지만 소스코드로 보면 치킨이라는 검색어를 찾을 수 없음 : 동적페이지
#request는 url주소에 저장된 소스코드에 나와있는 데이터만 가져올 수 있으므로 다른 방법으로 접근해야함 (week6_2에서!)
