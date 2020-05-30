#컨테이너: div.wrap_cont
#제목: div.wrap_cont a.f_link_b
#기사요약: div.wrap_cont p.f_eb.desc

import requests
from bs4 import BeautifulSoup

for n in range(1,4):
    raw = requests.get("https://search.daum.net/search?w=news&q=코알라&p="+str(n))
    html = BeautifulSoup(raw.text, 'html.parser')

    article = html.select("div.wrap_cont")

    for n in article:
        title = n.select_one("a.f_link_b").text
        summary = n.select_one("p.f_eb.desc").text

        print(title)
        print(summary)
        print("="*50)