import requests
from bs4 import BeautifulSoup

#csv형식으로 저장하기
f = open("navertv.csv","w",encoding='UTF-8')
f.write("제목, 채널명, 재생수, 좋아요\n")


raw = requests.get("https://tv.naver.com/r/")
# print(raw)  #웹잘열렸는지
# print(raw.text)  #코드
# print(raw.elapsed) #소요시간

#파싱_일련이 문자열을 유의미한 단위로 구분(텍스트 -> 소스코드로)
html = BeautifulSoup(raw.text, 'html.parser')
#print(html)  #선택자사용가능해짐

#1-3위 컨테이너: div.inner
#제목: dt.title
#체널명: dd.chn
#재생수: span.hit
#좋아요수: span.like

#1. 컨테이너 수집
container = html.select("div.inner")    #리스트형태로 저장
# print(container)
# print(container[0])

#2. 영상데이터 수집
title = container[0].select_one("dt.title").text.strip()   #한 컨테이너에 영상은 하나니까 select.one
chn = container[0].select_one("dd.chn").text.strip()
hit = container[0].select_one("span.hit").text.strip()
like = container[0].select_one("span.like").text.strip()

# print(title)          #태그도 포함
# print(title.text)     #태그 제외한 텍스트 데이터만
# print(chn.text)
# print(hit.text)
# print(like.text)

#공백제거
# print(title.text.strip())
# print(chn.text.strip())
# print(hit.text.strip())
# print(like.text.strip())


#리스트 활용한 반복하기
for cont in container:
    title = cont.select_one("dt.title").text.strip()  # 한 컨테이너에 영상은 하나니까 select.one
    chn = cont.select_one("dd.chn").text.strip()
    hit = cont.select_one("span.hit").text.strip()
    like = cont.select_one("span.like").text.strip()

    title = title.replace(",", "")
    chn = chn.replace(",", "")
    hit = hit.replace(",", "")
    like = like.replace(",", "")
    # print(title.text.strip())
    # print(chn.text.strip())
    # print(hit.text.strip())
    # print(like.text.strip())
    # print("="*50)
    f.write(title + ',' + chn + ',' + hit + ',' + like + '\n')

f.close()