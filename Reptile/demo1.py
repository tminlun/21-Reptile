# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/8/30 0030 18:45'

from urllib import request,parse


class getLaGou(object):
    def __init__(self):
        self.url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
        self.headers = {
            # 浏览器名称
            'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
            'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
            'Cookie': ' _ga=GA1.2.1277441612.1566993708; user_trace_token=20190828200024-6b520847-c98b-11e9-a507-5254005c3644; LGUID=20190828200024-6b520ae7-c98b-11e9-a507-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAAAGFABEF58C43DB8DB84DE01684ACB7178BFA4B7; WEBTJ-ID=20190830184012-16ce21c79bc220-0dc23f5931f2a-5373e62-1327104-16ce21c79bd4e; _gid=GA1.2.1003581546.1567161613; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1566993708,1567161613; LGSID=20190830183850-5ac79581-cb12-11e9-8dc9-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; TG-TRACK-CODE=index_search; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1567162007; LGRID=20190830184524-457efcf2-cb13-11e9-a507-5254005c3644; SEARCH_ID=87c8707b963a40d1b3d131cb9b9dd916; X_HTTP_TOKEN=cfcdaefdd9ebafd7739161765166333232d92d583f'

        }
        # data需要编码、转换为字节（python默认为str）：utf-8
        self.data = {
            'first': 'true',
            'pn': 1,
            'kd': 'python'
        }

    def get_url(self):
        data = parse.urlencode(self.data).encode('utf-8')
        # 创建Request对象
        req = request.Request(url=self.url, headers=self.headers, data=data, method='POST')
        result = request.urlopen(req)
        print(result.read().decode('utf-8'))

    def run(self):
        self.get_url()


if __name__ == '__main__':
    get_la_gou = getLaGou()
    get_la_gou.run()









