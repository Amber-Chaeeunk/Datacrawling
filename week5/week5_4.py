import requests
from bs4 import BeautifulSoup

from urllib.request import urlretrieve
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

raw = requests.get ("https://movie.naver.com/movie/running/current.nhn",
                    headers={"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

movies = html.select("dl.lst_dsc")

for m in movies:
    title = m.select_one("dt.tit > a")
    url = title.attrs["href"]
    print("="*50)
    print(title.text)
    #print("https://movie.naver.com"+url)

    each_raw = requests.get("https://movie.naver.com"+url,headers={"User-Agent":"Mozilla/5.0"})
    each_html = BeautifulSoup(each_raw.text, 'html.parser')

    # container = each_html.select("div.score_result ul li")
    #
    # for cont in container:
    #     stars = cont.select_one("div.star_score em").text.strip()
    #     reple = cont.select_one("div.score_reple p").text.strip()
    #
    #     print(stars, reple)
    # print("=" * 50)

    poster = each_html.select_one("div.mv_info_area div.poster img")
    poster_src = poster.attrs["src"]
    # print(poster_src)
    urlretrieve(poster_src, "poster/"+title.text[:2]+".png")