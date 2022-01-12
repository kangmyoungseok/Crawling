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
#    chrome_options.add_argument("incognito")   #Secret mode
#    chrome_options.add_argument('disable-gpu') #GPU하드웨어 가속 끄기 -> 속도가 빨라진다고 함
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.67 Safari/537.36')
#    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
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

driver = make_driver()
driver.get('https://etherscan.io/token/0x5152e1cb69a2ffa3997e89cbb4aba76a01d82141#comments')

driver.find_element_by_xpath('//*[@id="form"]/form/div/div[3]/div[2]/div/div[1]/div[1]')
driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div[1]/h1/div/span').text
driver.find_element_by_id('disqus_thread').text
element = driver.find_element_by_tag_name('iframe')
driver.switch_to_frame(element)
driver.
for i in range(1,201):
#    data= {}
    name = driver.find_element_by_xpath('//*[@id="pushable"]/div/main/section/div[4]/div[2]/div[{}]/div/div[1]/a'.format(i))
    function = driver.find_element_by_xpath('//*[@id="pushable"]/div/main/section/div[4]/div[2]/div[{}]/div/div[4]/span'.format(i))
    chain = driver.find_element_by_xpath('//*[@id="pushable"]/div/main/section/div[4]/div[2]/div[{}]/div/div[2]'.format(i))
    date = driver.find_element_by_xpath('//*[@id="pushable"]/div/main/section/div[4]/div[2]/div[{}]/div/div[6]'.format(i))
   # print(name.text)
#    data['name'] = name.text
#    data['function'] = function.text
#    data['date'] = date.text
    result.append({'name' : name.text , 'function' : function.text ,'chain' : chain.text, 'date' : date.text})



len(result)


pd.DataFrame(result).to_csv('result.csv',encoding='utf-8')
