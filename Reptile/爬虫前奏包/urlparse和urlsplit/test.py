# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/8/29 0029 10:42'

'''
一个url由以下几部分组成：
    scheme://host.port/path/?query-string=xxx&anchor
参数：
    scheme://host.port/path/?query-string=xxx&anchor
    scheme: 代表访问的协议，一般为http、ftp或https等
    host: 代表主机号，域名，例如: www.baidu.com
    port: 代表端口号，访问网站默认为80端口
    path: 代表查找路径
    query-string: 代表查询字符串
    anchor: 锚点，一般前端用来做页面定位
urlparse和urlsplit函数
    用法：
        有时候拿到一个url，想要对这个url中的各个组成部分进行分解，就需要用urlparse和urlsplit进行分割
    区别：urlsplit少个“params（url + ;params + ？）”参数
        
'''

from urllib import parse

url = "https://www.cnblogs.com/yunlongaimeng/p/10291356.html;hello?p=1"
# 分解
result = parse.urlparse(url)
print(result)
print("scheme: {} ---  netloc：{} --- path：{}".format(result.scheme,result.netloc,result.path))

