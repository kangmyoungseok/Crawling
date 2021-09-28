Selenium Studying
=================

# Crawling
Selenium을 이용한 크롤링 정리


![image](https://user-images.githubusercontent.com/33647663/135061392-2034f0c9-1abe-460a-9eee-0d1553475397.png)
이렇게 있으면 저부분을 어떻게 누를까?

![image](https://user-images.githubusercontent.com/33647663/135061336-bfded43e-a2a3-4f07-bae8-65f794b286ea.png)

1.driver.find_element_by_partial_link_text("News").click()


![image](https://user-images.githubusercontent.com/33647663/135061561-bff3030c-f319-41f8-a2d0-b167cacbe773.png)

코인들 이름 쭉 긁어오기

![image](https://user-images.githubusercontent.com/33647663/135061677-87f55891-57c9-4369-a311-aea83cdb8bbc.png)

![image](https://user-images.githubusercontent.com/33647663/135061708-d8ab8c41-8dce-4951-b770-3fef5e9b9bd4.png)

driver.find_elements_by_class_name("ticker") -> list배열로 해당 클래스 네임들이 전부 넘어온다.

for ticker in driver.find_elements_by_class_name("ticker"):
  print(ticker)
  
  
