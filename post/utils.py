# 뷰에 쓰는 크롤링함수 모았음
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

driver = webdriver.Chrome('../chromedriver')
driver.implicitly_wait(3)
driver.get('https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%ED%83%9D%EB%B0%B0%EC%A1%B0%ED%9A%8C')

def postview(company='CJ대한통훈', post_number='349159576510'):
    #select클래스를 이용하여 쉽게 요소들중에서 찾을수있다.
    select = Select(driver.find_element_by_class_name('_select'))

    # select by visible text
    select.select_by_visible_text(company)

    # select by value
    driver.find_element_by_name('numb').send_keys(post_number)

    driver.find_element_by_xpath('//*[@id="_doorToDoor"]/div[1]/div[2]/input[2]').click()

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    post_detail = soup.select('#_doorToDoor > div._output > div.artb > table > tbody > tr')


    post_list = []

    for x in post_detail:
        post_list.append(x.text.strip())

    return post_list


