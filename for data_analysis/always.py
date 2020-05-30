import requests
from bs4 import BeautifulSoup

raw = requests.get("url주소",
                    headers={"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

#컨테이너: ul.type01>li
#기사제목: span._sp_each_title
#언론사:span._sp_each_source

#1. 컨테이너 수집
#2. 기사 데이터 수집
#3. 반복하기

#1 컨테이너 수집
articles = html.select("ul.type01 > li")

#2. 기사 데이터 수집
title = articles[0].select_one("a._sp_each_title").text
source = articles[0].select_one("span._sp_each_source").text

print(title, source)