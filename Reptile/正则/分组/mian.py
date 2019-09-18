# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/9/16 0016 11:54'

import re

'''
分组：
正则默认有个大分组，即匹配全部
group() = group(0)
'''
# 匹配两个价格
text = "a1 price is $99，a2 price is $79"
# 正则白话文： 任意字符 . ，并为多个 * (价格 \$\d+) 任意字符，并为多个 (价格)
ret = re.search('.*(\$\d+).*(\$\d+)', text)
print("大分组 ：%s" % ret.group(0))  # 大分组
print("分组1 ：%s" % ret.group(1))  # 大分组
print("分组2 ：%s" % ret.group(2))  # 大分组
print(ret.group(1, 2))  # 多个分组  ('$99', '$79')
print(ret.groups())  # 所有子分组