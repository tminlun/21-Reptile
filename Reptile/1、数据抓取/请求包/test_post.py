# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/9/3 0003 15:38'

'''
requests的post
'''
import requests

url = "https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false"
# 请求头
headers = {
    # 上一次url
    'Referer': 'https://www.lagou.com/jobs/list_python?px=default&city=%E5%B9%BF%E5%B7%9E',
    # 浏览器名称
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'Cookie': '_ga=GA1.2.1277441612.1566993708; user_trace_token=20190828200024-6b520847-c98b-11e9-a507-5254005c3644; LGUID=20190828200024-6b520ae7-c98b-11e9-a507-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAAADEAAFI0EB275602550DC080845DEE1F0E69BD4; WEBTJ-ID=20190903153729-16cf60e9ff41e5-064070ecd7f939-5373e62-1327104-16cf60e9ff69e0; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1566993708,1567161613,1567496249; _gid=GA1.2.1684896333.1567496249; TG-TRACK-CODE=search_code; X_HTTP_TOKEN=cfcdaefdd9ebafd7431994765166333232d92d583f; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1567499219; LGRID=20190903162534-669877a9-ce24-11e9-8ec0-525400f775ce; SEARCH_ID=4b3ba840628843f2abe8039ccee442f4'
}
'''
    'Cookie': '_ga=GA1.2.1277441612.1566993708; user_trace_token=20190828200024-6b520847-c98b-11e9-a507-5254005c3644; LGUID=20190828200024-6b520ae7-c98b-11e9-a507-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAAADEAAFI0EB275602550DC080845DEE1F0E69BD4; WEBTJ-ID=20190903153729-16cf60e9ff41e5-064070ecd7f939-5373e62-1327104-16cf60e9ff69e0; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1566993708,1567161613,1567496249; _gid=GA1.2.1684896333.1567496249; TG-TRACK-CODE=search_code; X_HTTP_TOKEN=cfcdaefdd9ebafd7681694765166333232d92d583f; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1567496271; LGRID=20190903153626-8988f95c-ce1d-11e9-a508-5254005c3644; SEARCH_ID=cdc65c24820e4bd29cfceb5a4db19e60',
    "Host": "www.lagou.com",
    "Origin": "https://www.lagou.com",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "X-Anit-Forge-Code": "0",
    "X-Anit-Forge-Token": "None",
    "X-Requested-With": "XMLHttpRequest",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "25",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
'''
data = {
    "first": "true",
    "pn": "1",
    "kd": "python"
}
# 使用代理
proxies={
    'https': '58.253.154.89:9999'
}

response = requests.post(url=url,data=data,headers=headers,proxies=proxies,verify=False)
print(response.json())
