from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from bs4 import BeautifulSoup
import pandas as pd



#Chrome Options Docs : https://peter.sh/experiments/chromium-command-line-switches/

#make_options() set Options for Chrome Driver
def make_options():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])   #로그 끄기
    chrome_options.add_argument("incognito")   #Secret mode
    chrome_options.add_argument('disable-gpu') #GPU하드웨어 가속 끄기 -> 속도가 빨라진다고 함
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.67 Safari/537.36')
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--log-level=3") #최소 로그레벨 3(FATAL)로 설정. Critical한거 아니면 로그 안찍힘
#    chrome_options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.javascript': 2}) #javascript disable
#    chrome_options.add_argument('--headless') #UI를 띄우지 않고 Background에서 동작
#    chrome_options.add_argument("--disable-extensions")
#    chrome_options.add_argument('--ignore-certificate-errors-spki-list')
#    chrome_options.add_argument("--ignore-ssl-errors")
#    chrome_options.add_argument("--ignore-certificate-error")
#    chrome_options.add_argument("start-maximized") #브라우저 최대화면으로 띄움
#    chrome_options.add_argument("disable-infobars")    
    return chrome_options

#make_driver() returns Webdriver 
def make_driver():
    chrome_options = make_options()
    driver = webdriver.Chrome('./chromedriver.exe',options=chrome_options)
    return driver


#Example Sites url : https://coincodex.com
driver = make_driver()
driver.get('https://coincodex.com/')

# login 수행
driver.find_element_by_xpath('//*[@id="navbar"]/div[1]/header-user/div/ul/li[6]/span').click() #Signin 버튼 클릭
driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/ngbd-modal-content/div/div[2]/form/input[1]').send_keys('bobai')
driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/ngbd-modal-content/div/div[2]/form/input[2]').send_keys('bobai_pw')
driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/ngbd-modal-content/div/div[2]/form/button').click()
#driver.find_element_by_class_name('modal-content').find_element_by_tag_name('button').click()


#find_element_by_id()
element = driver.find_element_by_id("mobile_search_input").click()

#find_element_by_class_name()
element = driver.find_element_by_class_name('ticker') #일치하는 클래스가 여러개면 가장 첫번째 element
elements = driver.find_elements_by_class_name('ticker') #elements 는 리스트.
for element in elements:
    print(element.text)

#find_element_by_tag_name()
li = driver.find_element_by_tag_name('li')
li.text
lis = driver.find_elements_by_tag_name('li')
for li in lis:
    print(li.text)

#find_element_by_link_text
driver.find_element_by_link_text("News").click()
driver.find_element_by_partial_link_text("Portfo").text

# 응용 : 게시글 긁어보기 같은 class_name이면 list형태로 반환
for i in range(100):
    driver.find_elements_by_class_name("ticker")[i].text
    driver.find_elements_by_class_name("full-name")[i].text

#find_element_by_css_selector()
driver.find_element_by_css_selector('#homepage > app-hostspot > div > div > div.hotspot-lists.ng-star-inserted > div:nth-child(2) > div.hotspot-list-header > span').text

