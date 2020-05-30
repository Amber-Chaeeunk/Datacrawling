import requests
from bs4 import BeautifulSoup

raw = requests.get ("http://ticket2.movie.daum.net/Movie/MovieRankList.aspx",
                    headers={"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

#컨테이너  div.desc_boxthumb
container = html.select("div.desc_boxthumb")
for c in container:
    title = c.select_one("strong.tit_join a")
    print(title.text.strip())
    url = title.attrs["href"]
    # print(url)
    # print("="*40)

    each_raw = requests.get(url,headers={"User-Agent":"Mozilla/5.0"})
    each_html = BeautifulSoup(each_raw.text, 'html.parser')

    # each_container = each_html.select_one("div.movie_summary")


    scores = each_html.select_one("div.movie_summary em.emph_grade").text
    genre = each_html.select_one("dd.txt_main:nth-of-type(1)").text
    director = each_html.select("dl.list_movie dd:nth-of-type(5) a")
    actors = each_html.select("dl.list_movie dd:nth-of-type(6) a")

    print(scores)
    print(genre)
    for d in director:
        print(d.text)
    for a in actors:
        print(a.text)

    print("="*50)

#평점: em.emph_grade
#장르: dd.txt_main:nth-of-type(1)
#감독: dl.list_movie dd:nth-of-type(5) a
#배우: dl.list_movie dd:nth-of-type(6) a
