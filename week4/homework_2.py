#자율과제 2

#컨테이너: div#rso>g
#기사제목
#기사요약

import requests
from bs4 import BeautifulSoup
import openpyxl

try:
    wb = openpyxl.load_workbook("navernews.xlsx")
    sheet = wb.active

except:
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(["기사제목","기사요약"])

keyword = input("검색어를 입력해주세요: ")
page = 1
for page in range(1, 11, 1):   #page에 1부터 100까지 10의 간격으로 반복해줘
    raw = requests.get ("https://search.daum.net/search?w=news&DA=PGD&enc=utf8&cluster=y&cluster_page=1&q="+keyword+"&p="+str(page),
                    headers={"User-Agent":"Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')

    #컨테이너: ul.list_info>li
    #기사제목: div.wrap_tit
    #언론사:div.cont_inner p

    #1. 컨테이너 수집
    #2. 기사 데이터 수집
    #3. 반복하기

    #1 컨테이너 수집
    articles = html.select("ul.list_info>li")


    #3. 반복하기
    for ar in articles:
        title = ar.select_one("div.wrap_tit").text
        source = ar.select_one("div.cont_inner p").text

        print(title, source)
        sheet.append([title,source])

wb.save("daumrnews.xlsx")