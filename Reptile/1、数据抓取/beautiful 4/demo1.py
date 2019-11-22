# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/9/8 0008 23:28'


'''
bs4的类型  
'''

from bs4 import BeautifulSoup
from bs4.element import Tag

html = """
<div>
我是div
</div>
<p><!--  我是注释 --></p>
"""

soup = BeautifulSoup(html, "lxml")  # lxml 解析器，底层有c编写


div = soup.find('div')
print(type(div))  # 标签：Tag

print(type(div.string))  # 标签子内容：NavigableString

print(type(div.stripped_strings))  # 标签子孙内容 generator

print('='*90)
# 注释

div_ = soup.find('p')
print(div_.string)  # 当标签有多行字符，string则无法获取字符
print(type(div_.string))  # 注释字符串类型  Comment

