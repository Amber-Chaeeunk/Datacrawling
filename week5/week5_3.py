import requests
from bs4 import BeautifulSoup

raw = requests.get ("https://movie.naver.com/movie/running/current.nhn",
                    headers={"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

movies = html.select("dl.lst_dsc")

for m in movies:
    title = m.select_one("dt.tit > a")
    print(title.text)
    url = title.attrs["href"]
    # print("="*50)
    # print(title.text)
    #print("https://movie.naver.com"+url)

    each_raw = requests.get("https://movie.naver.com"+url,headers={"User-Agent":"Mozilla/5.0"})
    each_html = BeautifulSoup(each_raw.text, 'html.parser')

#컨테이너: div.score_result ul li
#평점: div.score_result ul li div.star_score em
#리뷰: div.score_result ul li div.score_reple p

    container = each_html.select("div.score_result ul li")

    for cont in container:
        stars = cont.select_one("div.star_score em").text.strip()
        reple = cont.select_one("div.score_reple p").text.strip()

        print(stars, reple)
    print("="*50)