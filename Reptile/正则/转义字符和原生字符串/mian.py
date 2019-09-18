# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/9/16 0016 11:16'

import re


# 转义字符：
# 1、匹配价格  $299

price = "thing price is $299"
ret = re.search('\$\d+', price)
print(ret.group())


# 原生字符串（r）：将特殊字符转换为普通字符。让字符串不进行Python转义，输出原来的字符串，给正则匹配
#  python转义 \ ：如：\n 特殊字符；在python中 \\n 将变成 \n
text = r"\n \t "
print(text)

test = "\\n"  # 特殊字符：\\n 变成 \n
 # '\\n' 会进行转义变成 \n；（两个\转为一个\）
# 所以要匹配 \\ ： \\\\
ret = re.match('\\\\n', test)
print(ret.group())

test2 = "\n"  # 普通字符：相对于 \\c
ret = re.match("\\n", test2)
print(ret.group())

