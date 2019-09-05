# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/9/2 0002 22:23'

import requests


'''

1、编码方式：
     r.content：直接从为了上爬取得数据，没有经过任何解码，所以是个bytes类型。
                其实磁盘上和网络上的默认字符串类型都为bytes类型
                        
    r.text：requests库会自动猜测解码方式，所以会出现误差，从而出现乱码。
            为了避免乱码，需要手动使用 r.content.decode('utf-8')
    
2、添加header和查询参数：
    GET请求：
        r = requests.get("https://www.baidu.com/", params=)
    POST请求：
        requests.post("https://www.baidu.com/", data=) 
        
3、requests不信任证书（url的https有个×符号）：使用 verify=False
'''
url = "https://www.baidu.com/s"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}
params = {
    "wd": "中国"
}

r = requests.get('https://www.baidu.com/s',params=params,headers=headers)  # 对params自动编码
with open("baidu.html", "w", encoding="utf-8") as f:
    # open(encoding="utf-8") 文件写入磁盘格式 utf-8
    f.write(r.content.decode('utf-8'))  # 数据写入文件格式 utf-8

'''
# 出现乱码，则使用  r.content.decode("utf-8")
print(type(r.content))  # <class 'bytes'>
# print(r.content.decode("utf-8"))

print(r.url)  # https://www.baidu.com/
print(r.encoding)  # r.text  默认编码方式
print(r.status_code)  # 状态码：200

'''

