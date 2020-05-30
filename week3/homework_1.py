#컨테이너: div.lst_thum_wrap li
#제목: div.lst_thum_wrap li a strong
#저자: div.lst_thum_wrap li span.writer

import requests
from bs4 import BeautifulSoup

raw = requests.get("https://series.naver.com/ebook/top100List.nhn", headers={"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

book = html.select("div.lst_thum_wrap li")
for i in book:
    title = i.select_one("a strong").text
    author = i.select_one("span.writer").text

    print(title, author)