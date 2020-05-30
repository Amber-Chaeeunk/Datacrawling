import requests
from bs4 import BeautifulSoup
import openpyxl

keyword = input("검색어를 입력해주세요: ")

try:
    wb = openpyxl.load_workbook("navernews.xlsx")
    sheet = wb.active
    print("불러오기 완료")

except:
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(["제목","언론사"])
    print("새로운 파일을 만들었습니다.")

page = 1
for page in range(1, 100, 10):   #page에 1부터 100까지 10의 간격으로 반복해줘
    raw = requests.get ("https://search.naver.com/search.naver?where=news&sm=tab_jum&query="+keyword+"&start="+str(page),
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
    # title = articles[0].select_one("a._sp_each_title").text
    # source = articles[0].select_one("span._sp_each_source").text
    # print(title, source)

    #3. 반복하기
    for ar in articles:
        title = ar.select_one("a._sp_each_title").text
        source = ar.select_one("span._sp_each_source").text

        print(title, source)
        sheet.append([title,source])

wb.save("navernews.xlsx")