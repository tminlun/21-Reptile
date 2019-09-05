# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/8/29 0029 10:21'

from urllib import parse,request

'''
url的参数出现中文时，要对中文进行编码
所以编码用 urlencode()函数 解码用 （parse_qs）
'''
# 对字典进行编码和解码
params = {"name": "小明", "age": 18}
# 编码
qs = parse.urlencode(params)
print(qs)
# 解码
result = parse.parse_qs(qs)
print(result)




# 例子：
url = 'https://www.baidu.com/s'
# 参数
params1 = {"wd": "刘德华"}
# 解码
qs = parse.urlencode(params)
# 拼接
url = url + "?" + qs
#请求
r = request.urlopen(url)
print(r.read())

