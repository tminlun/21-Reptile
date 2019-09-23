# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/9/12 0012 12:40'

import re

'''
匹配单个字符：
    match：
         从起始位置匹配一个规则，起始位置匹配失败返回None
'''

# 1. 匹配某个字符
text = "hello"
ret = re.match('he', text)  # 对字符串进行规则（匹配字符串起始位置），匹配需要的字符

print(ret.group())  # he  # 匹配成功的字符


# 2、 .匹配任意单个字符（匹配不到换行符  \n）。所以.*匹配多个任意字符
text = "abcc"
ret = re.findall('.*', text)
print(ret)  # a


# 3. \d（0-9）   匹配数字
text = "66sixsix"
ret = re.match('\d*', text)
print(ret.group())

# 3.1  匹配非数字
text = "a+"
ret = re.match('\D', text)
print(ret.group())  # a

# 4.  \s  匹配空白字符（\n \t \r 空格）
text = "\t"
ret = re.match('\s', text)
print(ret.group())  # \t


# 5、 \w  匹配 a-z、A-Z、数字和下划线
text = "_aZ3"
ret = re.match('\w', text)
print(ret.group())  # _

# 5.1  \W 和\w相反
text = "="
ret = re.match("\W", text)
print(ret.group())  # =

# 6、组合方式[]  匹配[]中的字符
text = "0753-8888ada"
'''
[\d 所有数字； \- 匹配-（可能是特殊字符，所以加\进行转义）]  只匹配单个字符
+  匹配出现1至多的字符
'''
ret = re.match("[\d\-]+", text)
print(ret.group())  # 0753-8888


# 7、^ 非 （[^0-9]  ^\d  匹配非0-9的数字）
text = "abc"
ret = re.match("[^0-9]", text)
print(ret.group())


# 8、中括号代替 \w
text = "_bc"
ret = re.match("[a-zA-Z0-9_]", text)
print(ret.group())

# 8、中括号代替 \W
text = "=bc"
ret = re.match("[^a-zA-Z0-9_]", text)
print(ret.group())
