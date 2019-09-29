# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/9/29 0029 13:15'


import requests, json, os, time, random
import chardet  # 数据的编码
import pandas as pd


'''
    爬取去哪儿网站的旅游景点售票数据，反映出旅游景点的热度！
'''

# 去哪儿景点Excel文件保存路径
PLACE_EXCEL_PATH = 'qunar_place.xlsx'


def get_url(keyword, page):
    url = f'http://piao.qunar.com/ticket/list.json?keyword={keyword}.&page={page}'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Host': 'piao.qunar.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    }
    try:
        response = requests.get(url=url, headers=headers)

        if response.status_code != 200:
            print("请求失败！")
            return False

        text = response.text
        # 数据转换
        json_text = json.loads(text)
        # 返回数据

        print("请求成功！")
        get_place_info(json_text)

    except Exception:
        print("请求失败！")
        return False


def get_place_info(json_text):
    '''
    解析json，获取想要的数据
        :param json_text:  原数据
        :return:
    '''

    # 每页的全部景点
    sightList = json_text['data']['sightList']

    place_list = []
    for sing in sightList:
        # 使用get方法防止触发KeyError
        data = {'景点id': sing['sightId'],  # 景点id
                 '景点名称': sing['sightName'],  # 景点名称
                 '景点星级': sing.get('star', '无'),  # 景点星级
                 '评分': sing.get('score', 0),  # 评分
                 '门票价格': sing.get('qunarPrice', 0),  # 门票价格
                 '销量': sing.get('saleCount', 0),  # 销量
                 '省-市-县': sing['districts'],  # 省 市 县
                 '坐标': sing['point'],  # 坐标
                 '简介': sing.get('intro', ''),  # 简介
                 }
        place_list.append(data)

    # 保存到excel
    save_excel(place_list)


def save_excel(place_list):
    '''
        使用pandas库保存excel文件。
        :place_list:  景点数据
    '''

    # pd 进行追加数据模式，所以只能先读，再把数据保存到变量中
    if os.path.exists(PLACE_EXCEL_PATH):
        # 先读取数据，再把数据保存到变量中
        df = pd.read_excel(PLACE_EXCEL_PATH)
        df = df.append(place_list)
    else:
        # 实例化pd对象，再把数据保存到变量中
        df = pd.DataFrame(place_list)

    # 实例化writer对象
    writer = pd.ExcelWriter(PLACE_EXCEL_PATH)

    # 数据储存到Excel，columns 标题
    df.to_excel(excel_writer=writer,
                columns=['景点id', '景点名称', '景点星级', '评分', '门票价格', '销量', '省-市-县', '坐标', '简介'], index=False,
                encoding='utf-8', sheet_name='去哪儿热门景点')

    # 储存到Excel
    writer.save()
    writer.close()


def main(keyword):
    '''
    主函数
    :param keyword: 搜索关键字

    '''

    # 保存数据之前，先清空数据
    if os.path.exists(PLACE_EXCEL_PATH):
        os.remove(PLACE_EXCEL_PATH)

    # 爬取url
    for page in range(1, 2):
        # ’f’和str.format()格式字符串相似
        print(f"正在爬取{keyword}，第{page}页！")

        # 获取url
        get_url(keyword, page)

        # 睡眠，防止禁用ip
        time.sleep(random.randint(2, 5))

    # 遍历完成，爬取完成
    print("爬取完成！")




if __name__ == '__main__':
    main('国庆旅游景点')
