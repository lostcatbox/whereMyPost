# 뷰에 쓰는 크롤링함수 모았음
# 뷰에 쓰는 크롤링함수 모았음
from selenium import webdriver
from bs4 import BeautifulSoup


def postview(post_number='349159576510'):
    driver = webdriver.Chrome('/Users/lostcatbox/myproject/whereMyPost/chromedriver')
    driver.implicitly_wait(15)
    driver.get('https://www.cjlogistics.com/ko/tool/parcel/tracking')


    driver.find_element_by_id('paramInvcNo').send_keys(post_number)

    driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    post_detail = soup.select('#statusDetail > tr')


    post_list = []

    for x in post_detail:
        post_list.append(x.text.strip())

    print(post_list)
    return post_list
