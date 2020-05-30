import requests
from bs4 import BeautifulSoup

raw = requests.get("https://www.imdb.com/list/ls016522954/?ref_=nv_tvv_dvd",
                    headers={"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

# 컨테이너: div.lister-item-content
# 제목: h3.lister-item-header a
# 감독: p.text-muted a
# 배우: p.text-muted a

container = html.select("div.lister-item-content")
#
for con in container:
    title = con.select_one("h3.lister-item-header a").text
    stars = con.select("p.text-muted a")
#
#     print(title.text)
#     print(director.text)
#     print(stars.text)
#     print("="*50)


#(심화) action장르만 출력하기

    genre = con.select_one("span.genre").text

    if "Action" not in genre:
        continue

    print(title)
    # print(stars)
    # for d in director:
    #     print(d, ",")

    for s in stars:
        print(s.text, ",")


    print("="*50)