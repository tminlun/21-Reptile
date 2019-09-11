# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/9/9 0009 19:59'

'''
爬取中国天气网的全国天气，只爬取当天
'''
import requests
from bs4 import BeautifulSoup
from pyecharts.charts import Bar,Geo


URL = 'http://www.weather.com.cn/textFC/{}.shtml'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                  ' (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'Referer': 'http://www.weather.com.cn/static/html/weather.shtml'
}

# 储存所有数据
ALL_DATA = []


def get_url(url):
    response = requests.get(url=url, headers=HEADERS)
    text = response.content.decode('utf-8')

    return text



def parse_html(html):
    global ALL_DATA
    '''
    获取所有城市的天气信息：
        1、先获取包裹数据的大盒子
        2、获取其子孙table（table才包含数据），进行遍历
        3、过滤table中的前两个tr。获取其他tr的数据
        :param html:  网页
    '''

    # gat的源码不规范。lxml（c解析器）识别不了。所以使用 html5lib（浏览器解析器）
    soup = BeautifulSoup(html, "html5lib")

    conMidtabs = soup.find_all('div', attrs={'class': 'conMidtab'})  # 大盒子：未来几天所有数据
    for conMidtab in conMidtabs:
        # conMidtab 未来几天

        tables = conMidtab.find_all('table')  # 获取所有的table（里面才装着数据,conMidtab2并无）

        for table in tables:
            #  table 装着所有省份信息

            # 城市天气列表
            trs = table.find_all('tr')[2:]

            # 天气数据
            for index, tr in enumerate(trs):
                # tr具体每个城市天气

                weather = {}  # 定义数据，放在遍历最多中

                # # 日期
                # days_trs = table.find_all('tr')[0]
                # day = list(days_trs.find_all('td')[-2].stripped_strings)[0]
                # weather['日期'] = day


                # 最终天气数据：tds是个列表
                tds = tr.find_all('td')

                # 城市
                # 第二个tr开始，的第一个td是城市
                city_td = tds[0]

                # 第一个tr的第一个td装着省份，第二个才是城市
                if index == 0:
                    '''
                    过滤省份
                    如果是第一个tr，（第一个tr的第一个td是省份），第一个tr的第二个td为才是城市
                    '''
                    city_td = tds[1]  # 第一个tr时， 将第二个td转换为城市

                city_name = list(city_td.stripped_strings)[0]  # 获取城市非标签字符串
                city_href = city_td.find('a')['href']
                weather['city'] = city_name
                # weather['城市链接'] = city_href

                # # 天气现象
                # phenomenon_td = tds[-3]
                # phenomenon = list(phenomenon_td.stripped_strings)[0]
                # weather['天气现象'] = phenomenon

                # 最低气温
                temp_td = tds[-2]
                min_temp = list(temp_td.stripped_strings)[0]
                weather['min_temp'] = int(min_temp)

                # 把全部数据存入全局变量
                ALL_DATA.append(weather)

            # # 获取一个省份
        break


def main():
    regions = ['hb', 'db', 'hd', 'hz', 'hn', 'xb', 'xn', 'gat']  # gat 的源码不规范
    for index, region in enumerate(regions):

        # 获取url
        url = URL.format(region)
        html = get_url(url)


        # 规则网页
        parse_html(html)


        # 数据可视化（数据分析）
        # 根据最低气温排序
        ALL_DATA.sort(key=lambda data: data['min_temp'])
        data = ALL_DATA[:10]  # 取前十个

        # 从列表元素（字典），获取值。
        # 方法1、遍历列表，获取列表的字典的值，再把这些值放入新列表；方法2、map
        # 全部城市
        citys = list(map(lambda x:x['city'], data))
        # 全部天气
        min_temps = list(map(lambda x:x['min_temp'], data))

        # pyechars
        bar = Bar()  # 初始化
        bar.add_xaxis(citys)
        bar.add_yaxis("城市", min_temps)
        # render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
        # 也可以传入路径参数，如 bar.render("mycharts.html")
        bar.render("mycharts.html")


if __name__ == '__main__':
    main()