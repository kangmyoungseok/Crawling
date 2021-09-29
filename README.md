Selenium Studying
=================

## 🔎 Selenium이란?
 - Selenium은 주로 웹앱을 테스트하는데 이용하는 프레임워크다. webdriver라는 API를 통해 운영체제에 설치된 Chrome등의 브라우저를 제어하게 된다.
 - 브라우저를 직접 동작시킨다는 것은 JavaScript를 이용해 비동기적으로 혹은 뒤늦게 불러와지는 컨텐츠들을 가져올 수 있다는 것이다. 즉, ‘눈에 보이는’ 컨텐츠라면 모두 가져올 수 있다는 뜻이다. 우리가 requests에서 사용했던 .text의 경우 브라우저에서 ‘소스보기’를 한 것과 같이 동작하여, JS등을 통해 동적으로 DOM이 변화한 이후의 HTML을 보여주지 않는다. 반면 Selenium은 실제 웹 브라우저가 동작하기 때문에 JS로 렌더링이 완료된 후의 DOM결과물에 접근이 가능하다.

## installation
    pip install selenium

## Download ChromeDriver
  크롬을 사용하려면 크롬이 로컬에 설치되어 있어야 하며, Chrome Driver를 추가적으로 설치하여야 한다.    
  https://sites.google.com/chromium.org/driver/downloads?authuser=0
  
  ![image](https://user-images.githubusercontent.com/33647663/135202233-61d738a4-0945-42f1-a852-3b1c825efd55.png)
  ![image](https://user-images.githubusercontent.com/33647663/135202465-35480b98-ec53-4047-9a07-fffe9da907df.png)
  <br>
  위의 파일을 받아 Selenium 객체를 실행할 때 지정해 주어야 한다.
  
  

## Selenium 사용해보기
    from selenium import webdriver
    
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.get("https://www.naver.com")
    #해당 url로 접근을 한다.
### 로드된 페이지에서 element들에 접근하는 메소드 목록
#### -  모든 메소드들에 대해서 find_elements로 호출하여 List형태로 반환받을 수 있다.
 - *driver.find_element(By.ID,"foo")*
 - *driver.find_element_by_id("foo")*
 - *driver.find_element_by_name("passwd")*
 - *driver.find_element_by_link_text("Sign In")*
 - *driver.find_element_by_partial_link_text("Sign")*
 - *driver.find_element_by_class_name("ticker")*
 - *driver.find_element_by_tag_name("h1")*
 - *driver.find_element_by_xpath("//*[@id="react-app"]")* 
 - *driver.find_element_by_css_selector('#table-container')*


## 📰 1. Example Code
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

Form Element는 다음과 같이 찾을 수 있다:    

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

Username&Password는 다음과 같이 찾을 수 있다:    

    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    
같은 Name이 여러개 있다면 가장 첫번째 Element를 찾는다.<br>
다음의 코드는 'Clear' 가 아닌 'Login' Element를 반환한다:    

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

Continue.html,Cancel.html link의 Element는 다왐과 같이 찾는다:    

    continue_link = driver.find_elemnet_by_link_text('continue')
    cancel_link = driver.find_element_by_partial_link_text('Can')
<br>


### 1.4 **Locating Elements by Class Name**
    <html>
     <body>
      <p class="content">Site content goes here.</p>
     </body>
    </html>

"p" Element는 다음과 같이 찾는다:    

    content = driver.find_element_by_class_name("content")
<br>

### 1.5 **Locationg Elements by Tag Name**
    <html>
     <body>
      <h1>Welcome</h1>
      <p>Site content goes here.</p>
     </body>
    </html>

Heading Element(h1)은 다음과 같이 찾는다:    

    Head1 = driver.find_elements_by_tag_name('h1')
<br>


### 1.6 **Locating by Xpath**
id,name으로 특정하기 어려운 경우가 많이 있다. 이경우 XPATH를 이용하여 쉽게 해당 Element를 찾을 수 있다.    
1. 찾고자 하는 페이지의 Element위에서 마우스 우클릭 -> 검사    
![image](https://user-images.githubusercontent.com/33647663/135217864-77171457-01e5-4e9d-99d0-5a09d050691e.png)


2. 해당하는 HTML 코드에서 Copy -> Copy Xpath로 해당 Element의 경로를 복사해 온다.    <br>
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



    
Form Element는 다음과 같이 찾을 수 있다.    

    login_form = driver.find_element_by_xpath("/html/body/form[1]")
    login_form = driver.find_element_by_xpath("//form[1]")
    login_form = driver.find_element_by_xpath("//form[@id='loginForm']")    
<br>
    1. 절대경로( HTML이 조금이라도 바뀌면 틀려진다.)    
    2. HTML에서 첫번째 Form Element    
    3. Form Element에서 id값이 'loginForm'으로 설정된 Form(가장 정확)    
<br>

### 1.7 **Locationg Element by CSS Selectors**
    <html>
     <body>
      <h1>Welcome</h1>
      <p>Site content goes here.</p>
     </body>
    </html>

Heading Element(h1)은 다음과 같이 찾는다:    

    Head1 = driver.find_elements_by_tag_name('h1')
<br>



## 2. Selenium 응용

### 2.1 send_keys() / click()

![image](https://user-images.githubusercontent.com/33647663/135210985-6b22c41a-cf8d-46bf-9d27-5f54db03619c.png)
    
    driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/ngbd-modal-content/div/div[2]/form/input[1]').send_keys('bobai') <br>
    driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/ngbd-modal-content/div/div[2]/form/input[2]').send_keys('bobai_pw')<br>
    driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/ngbd-modal-content/div/div[2]/form/button').click()<br>
    
### 2.2 find_elements
    #게시글 긁어보기 같은 class_name이면 list형태로 반환
    for i in range(100):
      driver.find_elements_by_class_name("ticker")[i].text
      driver.find_elements_by_class_name("full-name")[i].text
