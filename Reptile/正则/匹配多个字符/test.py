# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/9/15 0015 23:10'


import re

# 1、匹配手机号码
'''
1、已"1"开头
2、第二位号码：在"[34587]"区间
3、其他9位任意数字
'''
moblie = "17623476496"
ret = re.match('1[34587]\d{9}', moblie)
print(ret.group())

# 2、匹配邮箱
'''
1、@ 前面可以由字符、数字、_ （可以1个或多个）
2、@
3、域名可以：数字、字母
4、. 进行转义：\.
5、com  [a-z]
'''
email = "tml88@163.com"
ret = re.match('\w+@[a-z0-9]+\.[a-z]+', email)
print(ret.group())

# 3、匹配url
'''
1、协议：(http|https|ftp)
2、://  固定
3、// 后面为非空白字符  [^\s]+ 
'''
url = "https://www.dogedoge.com"
ret = re.match('(http|https|ftp)://[^\s]+', url)
print(ret.group())


# 验证身份证号码
'''
总有18位
1、前17位是数字
2、最后一位可以  [数字、xX]
'''
card = "39123318986512316X"
ret = re.match('\d{17}[\dxX]', card)
print(ret.group())
