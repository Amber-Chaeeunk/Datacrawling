from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver")
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fnid.naver.com%2Fuser2%2Fapi%2Froute.nhn%3Fm%3DroutePcMyInfo")

#아이디창: input#id
#비밀번호창: input#pw

#아이디 입력하기
input_id = driver.find_element_by_css_selector("input#id")
input_id.send_keys("chaechae1214")

#비밀번호 입력하기
input_pw = driver.find_element_by_css_selector("input#pw")
input_pw.send_keys("coala")

#로그인버튼: input.btn_global
log_button = driver.find_element_by_css_selector("input.btn_global")
log_button.click()

time.sleep(1)




