# 뷰에 쓰는 크롤링함수 모았음
# 뷰에 쓰는 크롤링함수 모았음
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests


def postview(post_company='CJ대한통운', post_number='349159576510'):

    if post_company == 'CJ대한통운':

        driver = webdriver.Chrome('/Users/lostcatbox/myproject/whereMyPost/chromedriver')
        driver.implicitly_wait(15)
        driver.get('https://www.cjlogistics.com/ko/tool/parcel/tracking')

        driver.find_element_by_id('paramInvcNo').send_keys(post_number)

        driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()

        driver.switch_to.frame(iframe[0])

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        post_detail = soup.select('#statusDetail > tr')

        post_list = []

        for x in post_detail:
            post_list.append(x.text.strip())

        driver.close()

        print(post_list)
        return post_list



    if post_company == 'CU편의점택배':

        driver = webdriver.Chrome('/Users/lostcatbox/myproject/whereMyPost/chromedriver')
        driver.implicitly_wait(15)
        driver.get('https://www.cupost.co.kr/postbox/delivery/local.cupost')


        driver.find_element_by_id('invoice_no').send_keys(post_number)

        driver.find_element_by_xpath('//*[@id="form"]/div/div/a').click()

        iframe = driver.find_elements_by_tag_name('iframe')
        driver.switch_to.frame(iframe[0])

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        post_detail = soup.select('body > div > table.tepTb.mt20 > tbody > tr')

        post_list = []

        for x in post_detail:
            post_list.append(x.text.strip())

        driver.close()

        print(post_list)
        return post_list

    if post_company == 'CVSNet':    #363217073274

        driver = webdriver.Chrome('/Users/lostcatbox/myproject/whereMyPost/chromedriver')
        driver.implicitly_wait(15)
        driver.get('https://www.cvsnet.co.kr/reservation-inquiry/delivery/index.do')


        driver.find_element_by_id('domestic_invoice_no').send_keys(post_number)

        driver.find_element_by_xpath('//*[@id="frm"]/div/div[1]/div/a[2]').click()

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        post_detail = soup.select('#div_result > div > div > div.deliveryInfo2 > ul > li')

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



    if post_company == '로젠택배':   #95638397046

        driver = webdriver.Chrome('/Users/lostcatbox/myproject/whereMyPost/chromedriver')
        driver.implicitly_wait(15)
        driver.get('https://www.ilogen.com/m/personal/tkSearch')


        driver.find_element_by_id('slipNo').send_keys(post_number)

        driver.find_element_by_xpath('//*[@id="slipNoBtn"]').click()

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        post_detail = soup.select('body > div > div > table.horizonTable > tbody > tr > td')

        post_list = []

        for x in post_detail:
            post_list.append(x.text.strip())

        driver.close()

        print(post_list)
        return post_list

    if post_company == 'EMS':    # EB709865140CN

        driver = webdriver.Chrome('/Users/lostcatbox/myproject/whereMyPost/chromedriver')
        driver.implicitly_wait(15)
        driver.get('https://service.epost.go.kr/trace.RetrieveEmsRigiTrace.comm')


        driver.find_element_by_id('POST_CODE').send_keys(post_number)

        driver.find_element_by_xpath('//*[@id="frmEmsRigiTrace"]/div/dl/dd/a').click()

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        post_detail = soup.select('#print > table.table_col.detail_off.ma_t_5 > tbody > tr > td')


        post_list = []

        for x in post_detail:
            post_list.append(x.text.strip())

        driver.close()

        print(post_list)
        return post_list

    if post_company == 'DHL express':    #7694274276 #GM295322752002026135

        driver = webdriver.Chrome('/Users/lostcatbox/myproject/whereMyPost/chromedriver')
        driver.implicitly_wait(15)
        driver.get('http://www.dhl.co.kr/ko/express.html')


        driver.find_element_by_id('AWB_containerleftpar_minitaskkcenter_transparsys_expandablelink_fb5b_insideparsys_fasttrack_984e').send_keys(post_number)

        driver.find_element_by_xpath('//*[@id="trackbut_containerleftpar_minitaskkcenter_transparsys_expandablelink_fb5b_insideparsys_fasttrack_984e"]').click()
        time.sleep(10)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        post_detail = soup.select('body > div.main.facelift.tracking-progress > div.main_area > div.content_main_container > div.content_main_index > div.container > div > div.section.shipmenttracking.tracking.dhl_classes_comp_tracking_params > div.tracking-results.dhl_classes_comp_tracking_results > div.tracking-result.express > table.result-checkpoints.show.result-has-pieces > tbody > tr')


        post_list = []

        for x in post_detail:
            post_list.append(x.text.strip())

        driver.close()

        print(post_list)
        return post_list













        # 참고 사이트
        # https: // www.logistics.dhl / kr - ko / home / tracking / tracking - express.html?submit = 1 & tracking - id =
        # https: // www.logistics.dhl / utapi?trackingNumber = GM295322752002026135 & language = ko & requesterCountryCode = KR
        #


        #headers = {
        #     'Referer': 'https://www.logistics.dhl/kr-ko/home/tracking/tracking-express.html?submit=1&tracking-id=7694274276',
        #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        # }
        #
        #
        # params = (
        #     ('trackingNumber', post_number),
        #     ('language', 'ko'),
        #     ('requesterCountryCode', 'KR'),
        # )
        #
        # json_data = requests.get('https://www.logistics.dhl/utapi', headers=headers, params=params)
        #
        # print(json_data)
        #
        # #
        #
        # post_list = []
        #
        # for x in post_detail:
        #     post_list.append(x.text.strip())
        #
        # print(post_list)
        # return post_list

    if post_company == 'Fedex':    #110738916651

        driver = webdriver.Chrome('/Users/lostcatbox/myproject/whereMyPost/chromedriver')
        driver.implicitly_wait(15)
        driver.get('https://www.fedex.com/ko-kr/tracking.html')


        driver.find_element_by_id('track_inbox_track_numbers_area').send_keys(post_number)

        driver.find_element_by_xpath('//*[@id="number"]/div/form/div/div/form/div[1]/div/button').click()
        time.sleep(6)

        html = driver.page_source
        # http://www.dhl-usa.com/en/express/tracking/tracking_tools.html
        # 오픈 api 주소
        soup = BeautifulSoup(html, 'html.parser')
        post_detail = soup.select('#container > div > div > div.trackingRootViewMain_TrackingView > div > div.tvc_detailPage_area > div:nth-child(2) > div.tvc_trackDetailView_area > div > div.trackDetailViewController_area.trackDetailSection > div > div.dp_snapshot_area > div > div.redesignSnapshotTVC.fxg-wrapper.container > h1 > div')


        post_list = []

        for x in post_detail:
            post_list.append(x.text.strip())

        driver.close()

        print(post_list)
        return post_list


