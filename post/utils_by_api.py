# 뷰에 쓰는 크롤링함수 모았음
# 뷰에 쓰는 크롤링함수 모았음
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests


def postview(post_company, post_number):

    if (post_company == 'CJ대한통운') or (post_company == 'CU편의점택배'):

        s = requests.Session()
        req = s.get('https://www.cjlogistics.com/ko/tool/parcel/tracking')
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        csrf = soup.find('input', {'name': '_csrf'})
        print(csrf['value'])

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Origin': 'https://www.cjlogistics.com',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Referer': 'https://www.cjlogistics.com/ko/tool/parcel/tracking',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6',
        }

        data = {
            '_csrf': csrf['value'],
            'paramInvcNo': post_number
        }

        html = s.post('https://www.cjlogistics.com/ko/tool/parcel/tracking-detail', headers=headers,
                             data=data)
        s.cookies.clear()
        raw = html.json()
        detail = raw["parcelDetailResultMap"]["resultList"]
        print(detail)

        post_infor = detail[0]["crgNm"]
        post_arrived_time = detail[0]["dTime"]
        post_place = detail[0]["regBranNm"]
        post_status = detail[0]["scanNm"]

        post_all_detail = [post_infor, post_arrived_time ,post_place, post_status]

        return post_all_detail


    if post_company == '우체국택배':  # 1415705137861

        s = requests.Session()
        req = s.get('https://service.epost.go.kr/trace.RetrieveDomRigiTraceList.comm')

        data = {
            'sid1': post_number,
        }

        req = s.post('https://service.epost.go.kr/trace.RetrieveDomRigiTraceList.comm',
                     data=data)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        s.cookies.clear()
        post_detail = soup.select('#print > div.h4_wrap.ma_t_5 > table > tbody > tr > td')

        post_list = []

        for x in post_detail:
            post_list.append(
                x.text.replace("\t", "").replace("/n", "").replace("\n", "").replace("\xa0", "").replace(" ", ""))

        post_all_detail = post_list[-4:]

        print(post_all_detail)

        return post_all_detail

    if post_company == '한진택배':  # 507696243040

        s = requests.Session()
        req = s.get('https://www.hanjin.co.kr/Delivery_html/')

        data = {
            'sel_wbl_num1': '0',
            'wbl_num': '507696243040'
        }
        params = (
            ('wbl_num', '507696243040'),
        )

        req = s.post('https://www.hanjin.co.kr/Delivery_html/inquiry/result_waybill.jsp', params=params, data=data)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        s.cookies.clear()
        post_detail = soup.select('#result_waybill2 > table > tbody > tr > td')

        post_list = []

        for x in post_detail:
            post_list.append(x.text.strip())

        post_all_detail = post_list[-4:]

        print(post_all_detail)
        return post_all_detail

    if post_company == '롯데택배':  # 233548940306

        s = requests.Session()
        req = s.get('https://www.lotteglogis.com/home/reservation/tracking/')

        data = {
            'InvNo': post_number,
        }

        req = s.post('https://www.lotteglogis.com/home/reservation/tracking/linkView/',
                     data=data)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        post_detail = soup.select('#contents > div > div.contArea > table > tbody > tr > td')

        post_list = []

        for x in post_detail:
            post_list.append(
                x.text.replace("\r", "").replace("\t", "").replace("\n", "").replace("\xa0", "").replace(" ", ""))
        post_all_detail = post_list[-4:]

        print(post_all_detail)

        return post_all_detail

    if post_company == '로젠택배':  # 95638397046

        s = requests.Session()
        req = s.get('https://www.ilogen.com/web/personal/tkSearch')
        post_number = '/' + '95638397046'

        req = s.get('https://www.ilogen.com/m/personal/trace' + post_number)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        s.cookies.clear()
        post_detail = soup.select('tbody > tr> td')

        post_list = []

        for x in post_detail:
            post_list.append(
                x.text.replace("\r", "").replace("\t", "").replace("\n", "").replace(" ", ""))

        post_all_detail = post_list[-6:]

        print(post_all_detail)
        return post_all_detail

    if post_company == 'EMS':  # EB709865140CN

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

    if post_company == 'DHL express':  # 7694274276 #GM295322752002026135

        '''
        https://www.logistics.dhl/utapi?trackingNumber=7694274276&language=ko&requesterCountryCode=KR
        '''


        post_list = []

        for x in post_detail:
            post_list.append(x.text.strip())

        print(post_list)
        return post_list

        # 참고 사이트
        # https: // www.logistics.dhl / kr - ko / home / tracking / tracking - express.html?submit = 1 & tracking - id =
        # https: // www.logistics.dhl / utapi?trackingNumber = GM295322752002026135 & language = ko & requesterCountryCode = KR
        #

        # headers = {
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

    if post_company == 'Fedex':  # 110738916651

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
        post_detail = soup.select(
            '#container > div > div > div.trackingRootViewMain_TrackingView > div > div.tvc_detailPage_area > div:nth-child(2) > div.tvc_trackDetailView_area > div > div.trackDetailViewController_area.trackDetailSection > div > div.dp_snapshot_area > div > div.redesignSnapshotTVC.fxg-wrapper.container > h1 > div')

        post_list = []

        for x in post_detail:
            post_list.append(x.text.strip())

        driver.close()

        print(post_list)
        return post_list


