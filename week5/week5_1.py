import requests
from bs4 import BeautifulSoup

raw = requests.get("https://movie.naver.com/movie/running/current.nhn",
                    headers={"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

#컨테이너 dl.lst_dsc
movies = html.select("dl.lst_dsc")


for m in movies:
    # 제목 dt.tit > a
    title = m.select_one("dt.tit > a").text
    # 평점 div.star_t1 a span.num
    score = m.select_one("div.star_t1 a span.num").text
    # 장르 dl.lst_dsc dl.info_txt1 dd
    # 문제점 : 장르 선택자가 장르뿐만 아니라 다른 데이터에도 쓰이는 선택자임

    # Way1.
    # info = m.select("dl.info_txt1 dd")   #리스트 형태로 장르,감독 데이터가 저장됨
    # #장르
    # genre = info[0].select("a")   #select는 리스트 형태로 저장됨
    # #감독
    # director = info[1].select("a")
    # #출연
    # actor = info[2].select("a")
    #
    #Way2. 선택자 사용하는 방법 nth-of-type 첫번째 데이터는 1임 *빈 데이터에 대해 에러안남 *dd:으로 사용가능 class나 id있다면 불가능
    genre = m.select("dl.info_txt1 dd:nth-of-type(1) a")
    director = m.select("dl.info_txt1 dd:nth-of-type(2) a")
    actor = m.select("dl.info_txt1 dd:nth-of-type(3) a")

    if float(score) < 8.5:
        continue

    genre_all = m.select_one("dl.info_txt1 dd:nth-of-type(1) span.link_txt")
    #선택자에 단일 장르인 a가 아닌 장르 전체 포함하는 span.link_text들어가야 됨
    if "액션" not in genre_all.text:
        continue

    print(title)
    print(score)

    for g in genre:
        print(g.text)
    for d in director:
        print(d.text)
    for a in actor:
        print(a.text)

    print("="*50)


