# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/8/30 0030 22:23'


'''
    大鹏人人网url：http://www.renren.com/880506098/profile
    最直接的模拟登陆：直接拷贝抓包的cookie数据
    
'''
from urllib import request


# 不使用cookie请求大鹏网页
da_peng_url = 'http://www.renren.com/880506098/profile'
headers = {
    'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'Cookie': 'anonymid=jzy733hj5sveak; depovince=GW; _r01_=1; ick_login=4eddc750-4318-4142-adab-6190b24194bf; XNESSESSIONID=abcB42Ne5-joT5wSz3IZw; JSESSIONID=abcMjzcTsZx7G_O824IZw; ick=7c2e6dac-d88a-4388-8fc8-e13fb277e935; t=129e8688c0e01c8e4de45912599ae33c2; societyguester=129e8688c0e01c8e4de45912599ae33c2; id=972104082; xnsid=1d1b8b90; WebOnLineNotice_972104082=1; jebecookies=f2502186-382e-443f-aa4f-85ca7d8da71e|||||; ver=7.0; loginfrom=null; jebe_key=3fdb73e1-d41b-4460-a3d6-87a886ddaf9b%7C30653039c5ec0fcc93dabb7cffee4923%7C1567174847286%7C1%7C1567174931294; jebe_key=3fdb73e1-d41b-4460-a3d6-87a886ddaf9b%7C30653039c5ec0fcc93dabb7cffee4923%7C1567174847286%7C1%7C1567174931298; wp_fold=0'

}

req = request.Request(url=da_peng_url,headers=headers)

resp = request.urlopen(req)
with open('renren.html', 'w', encoding='utf-8') as f:
    # open()将数据写入磁盘类型默认为bytes
    '''
    py3的write函数必须写入str类型
    resp.read()读出来是bytes类型
    bytes -> decode() -> str
    str -> encode() -> bytes
    '''
    # 将数据转为str，但open()将数据写入磁盘类型默认为bytes，所以将open写入磁盘的格式设置为str
    f.write(resp.read().decode('utf-8'))
