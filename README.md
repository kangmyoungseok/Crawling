Selenium Studying
=================

## ๐ Selenium์ด๋?
 - Selenium์ ์ฃผ๋ก ์น์ฑ์ ํ์คํธํ๋๋ฐ ์ด์ฉํ๋ ํ๋ ์์ํฌ๋ค. webdriver๋ผ๋ API๋ฅผ ํตํด ์ด์์ฒด์ ์ ์ค์น๋ Chrome๋ฑ์ ๋ธ๋ผ์ฐ์ ๋ฅผ ์ ์ดํ๊ฒ ๋๋ค.
 - ๋ธ๋ผ์ฐ์ ๋ฅผ ์ง์  ๋์์ํจ๋ค๋ ๊ฒ์ JavaScript๋ฅผ ์ด์ฉํด ๋น๋๊ธฐ์ ์ผ๋ก ํน์ ๋ค๋ฆ๊ฒ ๋ถ๋ฌ์์ง๋ ์ปจํ์ธ ๋ค์ ๊ฐ์ ธ์ฌ ์ ์๋ค๋ ๊ฒ์ด๋ค. ์ฆ, โ๋์ ๋ณด์ด๋โ ์ปจํ์ธ ๋ผ๋ฉด ๋ชจ๋ ๊ฐ์ ธ์ฌ ์ ์๋ค๋ ๋ป์ด๋ค. ์ฐ๋ฆฌ๊ฐ requests์์ ์ฌ์ฉํ๋ .text์ ๊ฒฝ์ฐ ๋ธ๋ผ์ฐ์ ์์ โ์์ค๋ณด๊ธฐโ๋ฅผ ํ ๊ฒ๊ณผ ๊ฐ์ด ๋์ํ์ฌ, JS๋ฑ์ ํตํด ๋์ ์ผ๋ก DOM์ด ๋ณํํ ์ดํ์ HTML์ ๋ณด์ฌ์ฃผ์ง ์๋๋ค. ๋ฐ๋ฉด Selenium์ ์ค์  ์น ๋ธ๋ผ์ฐ์ ๊ฐ ๋์ํ๊ธฐ ๋๋ฌธ์ JS๋ก ๋ ๋๋ง์ด ์๋ฃ๋ ํ์ DOM๊ฒฐ๊ณผ๋ฌผ์ ์ ๊ทผ์ด ๊ฐ๋ฅํ๋ค.

## installation
    pip install selenium

## Download ChromeDriver
  ํฌ๋กฌ์ ์ฌ์ฉํ๋ ค๋ฉด ํฌ๋กฌ์ด ๋ก์ปฌ์ ์ค์น๋์ด ์์ด์ผ ํ๋ฉฐ, Chrome Driver๋ฅผ ์ถ๊ฐ์ ์ผ๋ก ์ค์นํ์ฌ์ผ ํ๋ค.    
  https://sites.google.com/chromium.org/driver/downloads?authuser=0
  
  ![image](https://user-images.githubusercontent.com/33647663/135202233-61d738a4-0945-42f1-a852-3b1c825efd55.png)
  ![image](https://user-images.githubusercontent.com/33647663/135202465-35480b98-ec53-4047-9a07-fffe9da907df.png)
  <br>
  ์์ ํ์ผ์ ๋ฐ์ Selenium ๊ฐ์ฒด๋ฅผ ์คํํ  ๋ ์ง์ ํด ์ฃผ์ด์ผ ํ๋ค.
  
  

## Selenium ์ฌ์ฉํด๋ณด๊ธฐ
    from selenium import webdriver
    
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.get("https://www.naver.com")
    #ํด๋น url๋ก ์ ๊ทผ์ ํ๋ค.
### ๋ก๋๋ ํ์ด์ง์์ element๋ค์ ์ ๊ทผํ๋ ๋ฉ์๋ ๋ชฉ๋ก
#### -  ๋ชจ๋  ๋ฉ์๋๋ค์ ๋ํด์ find_elements๋ก ํธ์ถํ์ฌ Listํํ๋ก ๋ฐํ๋ฐ์ ์ ์๋ค.
 - *driver.find_element(By.ID,"foo")*
 - *driver.find_element_by_id("foo")*
 - *driver.find_element_by_name("passwd")*
 - *driver.find_element_by_link_text("Sign In")*
 - *driver.find_element_by_partial_link_text("Sign")*
 - *driver.find_element_by_class_name("ticker")*
 - *driver.find_element_by_tag_name("h1")*
 - *driver.find_element_by_xpath("//*[@id="react-app"]")* 
 - *driver.find_element_by_css_selector('#table-container')*


## ๐ฐ 1. Example Code
### 1.1 **Locating by Id**
    <html>
    <body>
      <form id="loginForm">
      <input name="username" type="text" />
      <input name="password" type="password" />
      <input name="continue" type="submit" value="Login" />
      </form>
    </body>
    </html>

Form Element๋ ๋ค์๊ณผ ๊ฐ์ด ์ฐพ์ ์ ์๋ค:    

    login_form = driver.find_elements_by_id('loginForm')
<br>

### 1.2 **Locating by Name**
    <html>
     <body>
      <form id="loginForm">
       <input name="username" type="text" />
       <input name="password" type="password" />
       <input name="continue" type="submit" value="Login" />
       <input name="continue" type="button" value="Clear" />
      </form>
     </body>
    </html>

Username&Password๋ ๋ค์๊ณผ ๊ฐ์ด ์ฐพ์ ์ ์๋ค:    

    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    
๊ฐ์ Name์ด ์ฌ๋ฌ๊ฐ ์๋ค๋ฉด ๊ฐ์ฅ ์ฒซ๋ฒ์งธ Element๋ฅผ ์ฐพ๋๋ค.<br>
๋ค์์ ์ฝ๋๋ 'Clear' ๊ฐ ์๋ 'Login' Element๋ฅผ ๋ฐํํ๋ค:    

    continue = driver.find_element_by_name("continue")
<br>

### 1.3 **Locating Hyperlinks by Link Text**
    <html>
     <body>
      <p>Are you sure you want to do this?</p>
      <a href="continue.html">Continue</a>
      <a href="cancel.html">Cancel</a>
     </body>
    </html>

Continue.html,Cancel.html link์ Element๋ ๋ค์๊ณผ ๊ฐ์ด ์ฐพ๋๋ค:    

    continue_link = driver.find_elemnet_by_link_text('continue')
    cancel_link = driver.find_element_by_partial_link_text('Can')
<br>


### 1.4 **Locating Elements by Class Name**
    <html>
     <body>
      <p class="content">Site content goes here.</p>
     </body>
    </html>

"p" Element๋ ๋ค์๊ณผ ๊ฐ์ด ์ฐพ๋๋ค:    

    content = driver.find_element_by_class_name("content")
<br>

### 1.5 **Locationg Elements by Tag Name**
    <html>
     <body>
      <h1>Welcome</h1>
      <p>Site content goes here.</p>
     </body>
    </html>

Heading Element(h1)์ ๋ค์๊ณผ ๊ฐ์ด ์ฐพ๋๋ค:    

    Head1 = driver.find_elements_by_tag_name('h1')
<br>


### 1.6 **Locating by Xpath**
id,name์ผ๋ก ํน์ ํ๊ธฐ ์ด๋ ค์ด ๊ฒฝ์ฐ๊ฐ ๋ง์ด ์๋ค. ์ด๊ฒฝ์ฐ XPATH๋ฅผ ์ด์ฉํ์ฌ ์ฝ๊ฒ ํด๋น Element๋ฅผ ์ฐพ์ ์ ์๋ค.    
1. ์ฐพ๊ณ ์ ํ๋ ํ์ด์ง์ Element์์์ ๋ง์ฐ์ค ์ฐํด๋ฆญ -> ๊ฒ์ฌ    
![image](https://user-images.githubusercontent.com/33647663/135217864-77171457-01e5-4e9d-99d0-5a09d050691e.png)


2. ํด๋นํ๋ HTML ์ฝ๋์์ Copy -> Copy Xpath๋ก ํด๋น Element์ ๊ฒฝ๋ก๋ฅผ ๋ณต์ฌํด ์จ๋ค.    <br>
![image](https://user-images.githubusercontent.com/33647663/135218214-00d7f25d-9357-4875-ad45-93f451d04f77.png)    
    
        <html>
         <body>
          <form id="loginForm">
           <input name="username" type="text" />
           <input name="password" type="password" />
           <input name="continue" type="submit" value="Login" />
           <input name="continue" type="button" value="Clear" />
          </form>
         </body>
        </html>



    
Form Element๋ ๋ค์๊ณผ ๊ฐ์ด ์ฐพ์ ์ ์๋ค.    

    login_form = driver.find_element_by_xpath("/html/body/form[1]")
    login_form = driver.find_element_by_xpath("//form[1]")
    login_form = driver.find_element_by_xpath("//form[@id='loginForm']")    
<br>
    1. ์ ๋๊ฒฝ๋ก( HTML์ด ์กฐ๊ธ์ด๋ผ๋ ๋ฐ๋๋ฉด ํ๋ ค์ง๋ค.)    
    2. HTML์์ ์ฒซ๋ฒ์งธ Form Element    
    3. Form Element์์ id๊ฐ์ด 'loginForm'์ผ๋ก ์ค์ ๋ Form(๊ฐ์ฅ ์ ํ)    
<br>

### 1.7 **Locationg Element by CSS Selectors**
    <html>
     <body>
      <h1>Welcome</h1>
      <p>Site content goes here.</p>
     </body>
    </html>

Heading Element(h1)์ ๋ค์๊ณผ ๊ฐ์ด ์ฐพ๋๋ค:    

    Head1 = driver.find_elements_by_tag_name('h1')
<br>



## 2. Selenium ์์ฉ

### 2.1 send_keys() / click()

![image](https://user-images.githubusercontent.com/33647663/135210985-6b22c41a-cf8d-46bf-9d27-5f54db03619c.png)
    
    driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/ngbd-modal-content/div/div[2]/form/input[1]').send_keys('bobai') <br>
    driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/ngbd-modal-content/div/div[2]/form/input[2]').send_keys('bobai_pw')<br>
    driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/ngbd-modal-content/div/div[2]/form/button').click()<br>
    
### 2.2 find_elements
    #๊ฒ์๊ธ ๊ธ์ด๋ณด๊ธฐ ๊ฐ์ class_name์ด๋ฉด listํํ๋ก ๋ฐํ
    for i in range(100):
      driver.find_elements_by_class_name("ticker")[i].text
      driver.find_elements_by_class_name("full-name")[i].text
