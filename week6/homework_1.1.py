from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.facebook.com/")

#아이디 입력하기
input_id = driver.find_element_by_css_selector("input#email")
input_id.send_keys("chaechae1214")

#비밀번호 입력하기
input_pw = driver.find_element_by_css_selector("input#pass")
input_pw.send_keys("coala")

#로그인버튼: input.btn_global
log_button = driver.find_element_by_css_selector("label#loginbutton")
log_button.click()

time.sleep(1)