# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/9/5 0005 11:00'

from lxml import etree  # lxml使用c语言，所以导入库会显示红色，且不提示

'''
    xpath： 1、返回的是列表，所以要遍历
            2、下标为1开始
'''



# 获取所有的span标签
# spans = html.xpath('//span')
# for span in spans:
#     print(etree.tostring(span, encoding='utf-8').decode('utf-8'))

# # 获取第二个span标签
# span = html.xpath('//span[2]')[0]
# print(etree.tostring(span, encoding='utf-8').decode('utf-8'))

# # 获取所有class为icon-collection的span元素
# spans = html.xpath("//span[@class='icon-collection']")
# for span in spans:
#     print(etree.tostring(span, encoding='utf-8').decode('utf-8'))


# # 获取a标签中的href的值（值返回的是字符串，所以不需要解码）
# aHrefs = html.xpath("//a/@href")
# for href in aHrefs:
#     print(href)




def get_position():
    parser = etree.HTMLParser(encoding='utf-8')
    html = etree.parse("tenxun.html", parser=parser)

    # 储存值
    positions = []

    # 获取文本数据
    divList = html.xpath("//div[@class='recruit-list']")

    for div in divList:
        '''
        xpath内嵌xpath：如使用//a还是在整个页面找全部a标签，
        所以必须使用.（如“.//a 表示当前div下面的所有子孙a标签”。或./span表示当前div下的子标签）
        '''


        # 获取href
        # aList = div.xpath('.//a/@href')[0]


        # if any(div) == False:
        #     # 对象是否为空
        #     continue
        # 获取a标签
        aList = div.xpath('./a')[0]
        # print(etree.tostring(aList, encoding='utf-8').decode('utf-8'))

        # 获取a标签中的，第一个h4标签的，文本
        title = aList.xpath('./h4[1]/text()')[0]

        # 获取城市
        city = aList.xpath('./p[1]/span[2]/text()')[0]

        # 类型
        category = aList.xpath('./p/span[3]/text()')[0]

        # 时间
        pub_time = aList.xpath('./p/span[4]/text()')[0]

        # 描述
        desc = aList.xpath('./p[@class="recruit-text"]/text()')[0]

        # 是否收藏
        # is_fav = div.xpath('./div[1]/span[2]/text()')[0]
        is_fav = div.xpath('.//span[@class="collection-text"]//text()')[0]
        print(is_fav)

        # 定义值
        position = {
            '职位': title,
            '城市': city,
            '类型': category,
            '发表时间': pub_time,
            '描述': desc
        }
        positions.append(position)

    return is_fav

if __name__ == '__main__':
    positon = get_position()
    print(positon)
