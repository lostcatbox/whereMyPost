# 뷰에 쓰는 크롤링함수 모았음
# 뷰에 쓰는 크롤링함수 모았음
from selenium import webdriver
from bs4 import BeautifulSoup
import time


def postview(post_company='CJ대한통운', post_number='349159576510'):

    if post_company == 'CJ대한통운':

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

        driver.close()

        print(post_list)
        return post_list


    if post_company == 'CU':

        driver = webdriver.Chrome('/Users/lostcatbox/myproject/whereMyPost/chromedriver')
        driver.implicitly_wait(15)
        driver.get('https://www.cupost.co.kr/postbox/delivery/local.cupost')


        driver.find_element_by_id('invoice_no').send_keys(post_number)

        driver.find_element_by_xpath('//*[@id="form"]/div/div/a').click()

        iframe = driver.find_elements_by_tag_name('iframe')
        driver.switch_to.frame(iframe[0])

        print(driver.page_source)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        post_detail = soup.select('body > div > table.tepTb.mt20 > tbody > tr')

        post_list = []

        for x in post_detail:
            post_list.append(x.text.strip())

        driver.close()

        print(post_list)
        return post_list

    if post_company == '우체국택배':   #1415705137861
        '''
        #print > div.h4_wrap.ma_t_5 > table > tbody > tr:nth-child(1)
        
        '''


        driver = webdriver.Chrome('/Users/lostcatbox/myproject/whereMyPost/chromedriver')
        driver.implicitly_wait(15)
        driver.get('https://service.epost.go.kr/iservice/usr/trace/usrtrc001k01.jsp')


        driver.find_element_by_id('sid1').send_keys(post_number)

        driver.find_element_by_xpath('//*[@id="frmDomRigiTrace"]/div/dl/dd/a').click()

        html = driver.page_source
        print(html)
        soup = BeautifulSoup(html, 'html.parser')
        post_detail = soup.select('#print > div.h4_wrap.ma_t_5 > table > tbody > tr > td')


        post_list = []

        for x in post_detail:
            post_list.append(x.text.strip())

        driver.close()

        print(post_list)
        return post_list

    if post_company == '한진택배':   #507696243040

        driver = webdriver.Chrome('/Users/lostcatbox/myproject/whereMyPost/chromedriver')
        driver.implicitly_wait(15)
        driver.get('https://www.hanjin.co.kr/Delivery_html/inquiry/personal_inquiry.jsp')


        driver.find_element_by_id('wbl_num').send_keys(post_number)

        driver.find_element_by_xpath('//*[@id="form1"]/div[2]/a[1]').click()

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        post_detail = soup.select('#result_waybill2 > table > tbody > tr > td')

        post_list = []

        for x in post_detail:
            post_list.append(x.text.strip())

        driver.close()

        print(post_list)
        return post_list


    if post_company == '롯데택배':   #233548940306

        driver = webdriver.Chrome('/Users/lostcatbox/myproject/whereMyPost/chromedriver')
        driver.implicitly_wait(15)
        driver.get('https://www.lotteglogis.com/home/reservation/tracking/index')


        driver.find_element_by_id('InvNo').send_keys(post_number)

        driver.find_element_by_xpath('//*[@id="contents"]/div/div[2]/div[3]/button').click()

        time.sleep(7)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        post_detail = soup.select('#contents > div > div.contArea > table > tbody > tr > td')

        post_list = []

        for x in post_detail:
            post_list.append(x.text.strip())

        driver.close()

        print(post_list)
        return post_list



    if post_company == '한진택배':   #507696243040

        driver = webdriver.Chrome('/Users/lostcatbox/myproject/whereMyPost/chromedriver')
        driver.implicitly_wait(15)
        driver.get('https://www.hanjin.co.kr/Delivery_html/inquiry/personal_inquiry.jsp')


        driver.find_element_by_id('wbl_num').send_keys(post_number)

        driver.find_element_by_xpath('//*[@id="form1"]/div[2]/a[1]').click()

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        post_detail = soup.select('')

        post_list = []

        for x in post_detail:
            post_list.append(x.text.strip())

        driver.close()

        print(post_list)
        return post_list

    if post_company == '한진택배':   #507696243040

        driver = webdriver.Chrome('/Users/lostcatbox/myproject/whereMyPost/chromedriver')
        driver.implicitly_wait(15)
        driver.get('https://www.hanjin.co.kr/Delivery_html/inquiry/personal_inquiry.jsp')


        driver.find_element_by_id('wbl_num').send_keys(post_number)

        driver.find_element_by_xpath('//*[@id="form1"]/div[2]/a[1]').click()

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        post_detail = soup.select('#result_waybill2 > table > tbody > tr > td')

        post_list = []

        for x in post_detail:
            post_list.append(x.text.strip())

        driver.close()

        print(post_list)
        return post_list


    if post_company == '한진택배':   #507696243040

        driver = webdriver.Chrome('/Users/lostcatbox/myproject/whereMyPost/chromedriver')
        driver.implicitly_wait(15)
        driver.get('https://www.hanjin.co.kr/Delivery_html/inquiry/personal_inquiry.jsp')


        driver.find_element_by_id('wbl_num').send_keys(post_number)

        driver.find_element_by_xpath('//*[@id="form1"]/div[2]/a[1]').click()

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        post_detail = soup.select('#result_waybill2 > table > tbody > tr > td')

        post_list = []

        for x in post_detail:
            post_list.append(x.text.strip())

        driver.close()

        print(post_list)
        return post_list


    if post_company == '한진택배':   #507696243040

        driver = webdriver.Chrome('/Users/lostcatbox/myproject/whereMyPost/chromedriver')
        driver.implicitly_wait(15)
        driver.get('https://www.hanjin.co.kr/Delivery_html/inquiry/personal_inquiry.jsp')


        driver.find_element_by_id('wbl_num').send_keys(post_number)

        driver.find_element_by_xpath('//*[@id="form1"]/div[2]/a[1]').click()

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        post_detail = soup.select('#result_waybill2 > table > tbody > tr > td')

        post_list = []

        for x in post_detail:
            post_list.append(x.text.strip())

        driver.close()

        print(post_list)
        return post_list


    if post_company == '한진택배':   #507696243040

        driver = webdriver.Chrome('/Users/lostcatbox/myproject/whereMyPost/chromedriver')
        driver.implicitly_wait(15)
        driver.get('https://www.hanjin.co.kr/Delivery_html/inquiry/personal_inquiry.jsp')


        driver.find_element_by_id('wbl_num').send_keys(post_number)

        driver.find_element_by_xpath('//*[@id="form1"]/div[2]/a[1]').click()

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        post_detail = soup.select('#result_waybill2 > table > tbody > tr > td')

        post_list = []

        for x in post_detail:
            post_list.append(x.text.strip())

        driver.close()

        print(post_list)
        return post_list