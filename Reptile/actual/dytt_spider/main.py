# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/9/6 0006 14:21'

'''
电影天堂2019新片精品的，列表的，电影详情的url
'''
import requests
from lxml import etree

BASE_DOMAIN = 'https://www.dytt8.net'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                  ' (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
}

urls = []


def get_detail_urls(url):
    global urls
    '''
    response.text：  默认会使用自己，猜测的编码方式将抓取下来的网页进行编码，储存到text中，
    在电影天堂因为编码方式不规范，requests库猜错了，所以出现乱码
    '''

    # 储存数据（如果在方法内定义空列表，则把数据返回给方法；如果定义全局变量，并且执行urls+=urls，则储存在全局的urls）
    urls += urls

    response = requests.get(url=url,headers=HEADERS)
    if response.status_code != 200:
        return False

    # 获取网页数据（ignore：忽略非法字符）
    text = response.content.decode('gbk', 'ignore')

    # xpath初始化
    html = etree.HTML(text)
    # print(etree.tostring(html,encoding='utf-8').decode('utf-8'))

    # 处理数据
    detail_urls = html.xpath('//table[@class="tbspan"]//a[@class="ulink"]/@href')

    # map：根据提供的函数，对指定的序列做映射
    # （遍历每个相对路径的url，用域名与其拼接），然后返回列表
    detail_urls = map(lambda url: BASE_DOMAIN+url, detail_urls)

    return detail_urls


def parse_detail_page(url):

    movie = {}

    # 获取网页
    response = requests.get(url,headers=HEADERS)
    text = response.content.decode('gbk')

    # 解析网页
    html = etree.HTML(text)

    # 只有片名是独立的元素
    title = html.xpath('//div[@class="title_all"]//font[@color="#07519a"]/text()')[0]
    movie['片名'] = title

    # 所有的电影信息（虽然ZoomD只有一个，但xpath始终返回列表，所以使用[0]）
    ZoomD = html.xpath('//div[@id="Zoom"]')[0]

    # 储存电影的封面图和截图
    imgs = ZoomD.xpath('.//img/@src')

    cover = imgs[0]
    screenshot = imgs[1]
    movie['封面图'] = cover
    movie['截图'] = screenshot

    # 封装方法：替换指定字符并去掉空格
    def pase_info(info,rule):
        '''

        :param info: 数据
        :param rule: 指定字符
        :return: 过滤后的数据
        '''
        ret = info.replace(rule, "").strip()  # strip去掉两侧空格
        return ret

    # 文本
    infos = ZoomD.xpath('.//text()')
    for index, info in enumerate(infos):
        # 利用下标获取具体的文本
        # print(info)
        # print(index)
        # print('='*30)

        if info.startswith('◎年　　代'):
            # 判断字符串是否以指定字符（字符串）开头
            year = pase_info(info, '◎年　　代')
            movie['年份'] = year

        elif info.startswith('◎类　　别'):
            category = pase_info(info, '◎类　　别')
            movie['类别'] = category

        elif info.startswith('◎上映日期'):
            show_date = pase_info(info, '◎上映日期')
            movie['上映日期'] = show_date

        elif info.startswith('◎片　　长'):
            running_time = pase_info(info, '◎片　　长')
            movie['片长'] = running_time

        elif info.startswith('◎标　　签'):
            label = pase_info(info, '◎标　　签')
            movie['标签'] = label
        elif info.startswith('◎主　　演'):
            '''
            判断为“◎主　　演”开头后，继续遍历余下的数据。
            当遇到“◎简　　介 ”停止遍历，并保存数据
            '''
            info = pase_info(info, '◎主　　演').strip()
            actors = [info,]  # 储存演员信息，并进行拼接([info, actor])

            # index表示 当前数据的下标（当前数据后面的数据）。len(infos)  总索引
            for x in range(index + 1, len(infos)):
                # 使用infos根据下标获取对应的值
                actor = infos[x].strip()

                if actor.startswith('◎'):
                    # 去除其他信息
                    break
                actors.append(actor)
            # 添加到字典
            movie['演员'] = actors

        elif info.startswith('◎简　　介 '):

            synopsis = []

            # 使用下标根据infos获取数据
            for x in range(index + 1, len(infos)):
                synopsi = infos[x].strip()
                if synopsi.startswith('【下载地址】'):
                    # 停止遍历数据
                    break
                synopsis.append(synopsi)
            # 多余的数据过滤
            synopsis = synopsis[0]
            movie['简介'] = synopsis

    # 下载链接
    download_url = html.xpath('//td[@bgcolor="#fdfddf"]/a/text()')[0]
    movie['下载链接'] = download_url

    return movie


def spider():
    '''主函数'''

    movies = []  # 储存所有电影

    for i in range(9,11):
        # 列表 url
        url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{num}.html'.format(num=i)

        # 提示爬取第几页
        print('{0}\n 爬取第{1}页\n {2}'.format('='*30,i,'='*30) )

        # 详情url
        detail_urls = get_detail_urls(url)

        for detail_url in detail_urls:
            movie = parse_detail_page(detail_url)
            movies.append(movie)

            # break
        # # 只遍历一次
        # break
    print(movies)
    return movies


if __name__ == '__main__':
    spider()
