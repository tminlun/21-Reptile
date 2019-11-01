# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/10/21 0021 13:50'

import requests
import time
import re

from lxml import etree



'''
headers：
    反爬虫：
        X-Anit-Forge-Code: 0
        X-Anit-Forge-Token: None
    
    是否为ajax请求：
        X-Requested-With: XMLHttpRequest


'''



def get_url(data):
    '''
    列表的json数据
    :param data: post参数
    '''
    print(data)
    url = r'https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
        'Referer': 'https://www.lagou.com/jobs/list_python/p-city_213?px=default',
        'Origin': 'https://www.lagou.com',
        'X-Anit-Forge-Code': "0",
        'X-Anit-Forge-Token': "None",
        'X-Requested-With': "XMLHttpRequest",
        'Cookie': '_ga=GA1.2.1277441612.1566993708; user_trace_token=20190828200024-6b520847-c98b-11e9-a507-5254005c3644; LGUID=20190828200024-6b520ae7-c98b-11e9-a507-5254005c3644; JSESSIONID=ABAAABAAAGFABEFFF5FE0D1B38AE4648EF51322791E29CC; WEBTJ-ID=20191021133231-16deccd7628691-0a6af3f2e5e4fc-b363e65-1327104-16deccd76295c4; _gid=GA1.2.110465316.1571635952; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1571635952; index_location_city=%E5%85%A8%E5%9B%BD; sajssdk_2015_cross_new_user=1; LGSID=20191021142901-122ecfc3-f3cc-11e9-9f35-525400f775ce; TG-TRACK-CODE=search_code; gate_login_token=7e4e916235b59435b88880a5e4e6b9ef7e5693fce91722d172fe82baa8fffa1b; _putrc=3CBB67977E11EB99123F89F2B170EADC; login=true; unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B73905; privacyPolicyPopup=false; hasDeliver=0; SEARCH_ID=f047f358299b435eaf79c2fe0d5ce1a8; X_HTTP_TOKEN=cfcdaefdd9ebafd7381346175166333232d92d583f; _gat=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216deccd958417d-078b45e4e6ac1d-b363e65-1327104-16deccd9585af2%22%2C%22%24device_id%22%3A%2216deccd958417d-078b45e4e6ac1d-b363e65-1327104-16deccd9585af2%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1571643280; LGRID=20191021153303-044eea0d-f3d5-11e9-9f3a-525400f775ce'
    }
    response = requests.post(url,headers=headers,data=data)
    text = response.json()
    get_detail_url(text)


def get_detail_url(text):
    """
    获取详情页面url
    :param text: 列表的json数据
    """

    # 获取详情url
    results = text['content']['positionResult']['result']  # type：列表
    for result in results:
        positionId = result.get('positionId', '')  # detail_pk
        detail_url = f'https://www.lagou.com/jobs/{positionId}.html?show=188ecdcec2d94c40b3431b4587c62bd8'

        # 解析详情
        parse_detail_page(detail_url)

        break


def parse_detail_page(detail_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
        'Referer': 'https://www.lagou.com/jobs/list_python/p-city_213?px=default',
        'cookie': '_ga=GA1.2.1277441612.1566993708; user_trace_token=20190828200024-6b520847-c98b-11e9-a507-5254005c3644; LGUID=20190828200024-6b520ae7-c98b-11e9-a507-5254005c3644; JSESSIONID=ABAAABAAAGFABEFFF5FE0D1B38AE4648EF51322791E29CC; WEBTJ-ID=20191021133231-16deccd7628691-0a6af3f2e5e4fc-b363e65-1327104-16deccd76295c4; _gid=GA1.2.110465316.1571635952; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1571635952; index_location_city=%E5%85%A8%E5%9B%BD; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216deccd958417d-078b45e4e6ac1d-b363e65-1327104-16deccd9585af2%22%2C%22%24device_id%22%3A%2216deccd958417d-078b45e4e6ac1d-b363e65-1327104-16deccd9585af2%22%7D; sajssdk_2015_cross_new_user=1; LGSID=20191021142901-122ecfc3-f3cc-11e9-9f35-525400f775ce; TG-TRACK-CODE=search_code; gate_login_token=7e4e916235b59435b88880a5e4e6b9ef7e5693fce91722d172fe82baa8fffa1b; _putrc=3CBB67977E11EB99123F89F2B170EADC; login=true; unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B73905; privacyPolicyPopup=false; hasDeliver=0; _gat=1; SEARCH_ID=8c3e52c520504e669205537d8f486682; X_HTTP_TOKEN=cfcdaefdd9ebafd7786246175166333232d92d583f; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1571642784; LGRID=20191021152447-dca10f14-f3d3-11e9-9f38-525400f775ce'
    }
    response = requests.get(url=detail_url, headers=headers)
    text = response.text
    # 提取数据
    html = etree.HTML(text)
    name = html.xpath('//h1[@class="name"]//text()')[0]  # 标题

    span_list = html.xpath('//dd[@class="job_request"]//span')
    # 薪资
    salary = span_list[0].xpath('.//text()')[0].strip()
    # 城市
    city = span_list[1].xpath('.//text()')[0].strip()
    city = re.sub(r'[\s/]', '', city)
    # 经验
    experience = span_list[2].xpath('.//text()').strip()
    experience = re.sub(r'[\s/]', '', experience)
    # 学历
    degree = span_list[3].xpath('.//text()').strip()
    degree = re.sub(r'[\s/]', '', degree)
    print(degree)

    desc = "".join(html.xpath('//dd[@class="job_bt"]//text()')).strip()  # 转为字符串，再去空格
    print(desc)
    work_addr = "".join(html.xpath('//div[@class="work_addr"]//text()')).strip()
    print(work_addr)





def main():
    for page in range(1,2):

        time.sleep(1)
        print(f"爬取第{page}页！")

        data = {
            'first': 'false',
            'pn': page,
            'kd': 'python',
            'sid': '2b2e4b9d1c5d44f29068e0034128f7aa'
        }
        # if page == 1:
        #     data['first'] = "true"
        get_url(data)




if __name__ == '__main__':
    main()


