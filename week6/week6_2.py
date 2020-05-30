#selenium 브라우저자동화도구 : 실제 웹브라우저 켜는 과정을 거치므로 동적페이지 데이터도 수집가능 (request대신 사용할 것)
#selenium설치할 때는 chrome web driver 설치해야함

from selenium import webdriver
import time #지연시간

driver = webdriver.Chrome("./chromedriver")  #./은 현재 디렉토리에 있는 크롬드라이버켜줘라는 뜻
driver.get("https://v4.map.naver.com/")

#<절차>
#1. 네이버 지도 페이지 접속
#2. 검색창에 검색어 입력
#3. 검색어 버튼 누르기
#4. 검색결과 수집하기

# 검색창:input#search-input
# 검색어 입력하기
search_box = driver.find_element_by_css_selector("input#search-input")
search_box.send_keys("치킨")  # 검색어 입력 (key핵심어를 send전송해라)
# 검색버튼 누르기
search_button = driver.find_element_by_css_selector("button.spm")
search_button.click()

time.sleep(1) #지연시간 1초

#컨테이너:dl.lsnx_det
#가게명:dl.lsnx_det dt>a
#가게주소:dl.lsnx_det dd.addr
#가게번호:dl.lsnx_det dd.tel

cont = driver.find_elements_by_css_selector("dl.lsnx_det")
for c in cont:
    name = c.find_element_by_css_selector("dt>a").text
    addr = c.find_element_by_css_selector("dd.addr").text
    tel = c.find_element_by_css_selector("dd.tel").text

    print(name)
    print(addr)
    print(tel)
    print("="*50)

    #웹페이지 뜨고 느리고 잘 안 됨
    #import time 넣어주고 버튼클릭한 이후에 time.sleep(1) 지연시간 1초 넣어줌으로써 해결가능


driver.close()