# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/9/5 0005 10:13'


from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''


def get_text():
    '''
    解析字符串：字符串无需解码
    :return:
    '''
    # 初始化,使用此对象执行xpath语法
    html = etree.HTML(text)
    # 解析字符串时候使用encoding编码，再进行utf-8解码
    result = etree.tostring(html, encoding='utf-8').decode('utf-8')
    print(result)


def get_file():
    '''
    解析文件：parse
        etree函数默认使用XML解析器，如果遇到html代码不规范时，代码解析会出错。
        这时候要自己parser：创建HTML解析器
    '''

    # 使用HTML解析器，当html代码不规范的时候
    parser = etree.HTMLParser(encoding='utf-8')
    html = etree.parse('../daPeng.html', parser=parser)
    result = etree.tostring(html, encoding='utf-8').decode('utf-8')
    print(result)


if __name__ == '__main__':
    get_file()
