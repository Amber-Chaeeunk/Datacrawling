#동적페이지 반복

from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver")
driver.get("https://v4.map.naver.com/")

search_box = driver.find_element_by_css_selector("input#search-input")
search_box.send_keys("치킨")

search_button = driver.find_element_by_css_selector("button.spm")
search_button.click()



for n in range(1,20):
    time.sleep(1) #지연시간도 for문안에 같이 넣어주어야함

    cont = driver.find_elements_by_css_selector("dl.lsnx_det")
    for c in cont:
        name = c.find_element_by_css_selector("dt>a").text
        addr = c.find_element_by_css_selector("dd.addr").text
        try:
            tel = c.find_element_by_css_selector("dd.tel").text
        except:
            tel = "전화번호 없음"

        print(name)
        print(addr)
        #print(tel)
        print("="*50)

        #페이지버튼: div.paginate > *
    page_bar = driver.find_elements_by_css_selector("div.paginate > *")
    #page_bar[n+1].click()

    try:
        if n%5 != 0:
            page_bar[n%5+1].click()
        else:
            page_bar[6].click()
    except:
        print("수집완료")
        break

