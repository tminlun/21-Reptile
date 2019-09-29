# _*_ encoding:utf-8 _*_
import requests
__author__: '田敏伦'
__date__: '2019/9/25 0025 16:51'


'''
逻辑：
    1.获取城市的ID，并存入csv等等。以key，value形式存入
    2、获取城市的所有酒店信息
    3、获取酒店详情的url
    4、根据详情url，获取酒店的具体信息。
    
参数：
    offset：页数
    startDay=20190925&endDay=20190925：入住时间

'''

page1_url = 'https://ihotel.meituan.com/hbsearch/HotelSearch?utm_medium=pc&' \
            'version_name=999.9&cateId=20&attr_28=129&uuid=DA6517961BC38FF29DAEBDAB7804E2B54D1C4D11CC32AB2A2BA2D41178E9E9A1%401569400985918&cityId=92&offset=0&limit=20&startDay=20190925&endDay=20190925' \
            '&q=&sort=defaults&' \
            'price=100~200&X-FOR-WITH=AYNarGAr47990%2BQdnlZGAcXcAB%2B5IxUQnbAzgZ%2BAHkCFCJQhp8JvprOGPEHWiY9EDb2eGQyNSxPBJKXf73Zdquiy55JBHearcJbZD5o6hSVSnZUhGrEXhX3PK5FhEgXqqvCdz2rsjOAyEKbPrLlN9Q%3D%3D'

page2_url = 'https://ihotel.meituan.com/hbsearch/HotelSearch?utm_medium=pc&version_name=999.9&' \
            'cateId=20&attr_28=129&uuid=DA6517961BC38FF29DAEBDAB7804E2B54D1C4D11CC32AB2A2BA2D41178E9E9A1%401569401548937&cityId=92&' \
            'offset=20&limit=20&startDay=20190925&endDay=20190925&q=&' \
            'sort=defaults&X-FOR-WITH=6dgO4tyqHQfWCXJcGD%2BPjkfMFqlEvPblYd6X9E5kVEB%2Bi1BJCm7RvkoZN6qmzgP1uT%2FjrfgN0QU7sR3Hr7PbPPDMloCb8n36gqX7f9ksJHZCcmaPyfTVNga%2FHi%2BqMDnDXPUrOvvobvYROFZaEuivig%3D%3D'

city_url = 'https://hotel.meituan.com/dist/search-client.js?1569402746'

if __name__ == '__main__':

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        'Referer': 'https://hotel.meituan.com/guangzhou/'

    }

    response = requests.get(url=city_url, headers=headers)
    # text = response.content.decode('utf-8')
    text = response.text

    # import chardet
    #
    # print(chardet.detect(response.content))

    import re

    city_js = r'[t("map-info", {attrs: {pois: e.poi}})], 1)])},staticRenderFns: []};n.a=i}, function(e, n) {e.exports={data: [.*]}}, function(e, n, t) {"use strict";Object.defineProperty(n, "__esModule", {value: !0});var i, a=t(6), r=(i=a) & & i.__esModule ? i: {'

    ret = re.findall(r'.*?data:\s+(.*?)}.*', text, re.DOTALL)

    print(ret)
