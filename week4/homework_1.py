import requests
from bs4 import BeautifulSoup
#네이버 시리즈 e북 인기 TOP100

#컨테이너: ul.lst_thum.v1 li
#제목: a>strong
#저자: span.writer

import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(["제목","저자"])


page = 1
for page in range(1, 6, 1):
    raw = requests.get("https://series.naver.com/ebook/top100List.nhn?page="+str(page),headers={"User-Agent":"Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')

#컨테이너
    container = html.select("ul.lst_thum.v1 li")
#제목
# title = html.select("a>strong")
# #저자
# author = html.select("span.writer")

    for cont in container:
        title = cont.select_one("a>strong").text.strip()
        author = cont.select_one("span.writer").text.strip()


        sheet.append([title,author])

wb.save("naverebook.xlsx")
