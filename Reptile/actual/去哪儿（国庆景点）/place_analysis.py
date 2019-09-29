# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/9/29 0029 13:58'


'''
    数据分析：
        门票销量排行分析
        
        门票销售额排行分析 ：
                销售额=单价*销量，我们可以将每行的price和sale相乘算出销售额
        
        景点销量热力图分析：
                使用百度地图开放api（免费）做一个热力图。
                申请一个百度地图开放平台的应用（必须浏览器端应用，不然生成不了）
                
        推荐景点：
            高评分、销量少、价格便宜。
            推荐景点 = 评分/(销量价格) * 1000
'''

import re

import numpy as np
import pandas as pd

from pyecharts import options as opts
from pyecharts.charts import Bar


# 去哪儿景点文件保存路径
PLACE_EXCEL_PATH = 'qunar_place.xlsx'

# 百度热力图模板
HOT_MAP_TEMPLATE_PATH = 'hot/hot_map_template.html'

# 生成的热力图
PLACE_HOT_MAP_PATH = 'hot/place_hot_map.html'

# 读取数据
DF = pd.read_excel(PLACE_EXCEL_PATH)


# 1、景点门票销量排行
def analysis_sale():
    '''

    :return:
    '''

    # 引入全局数据
    global DF
    # 拷贝Excel景点文件储存数据
    df = DF.copy()

    # 1、生成表：包括名称和销量
    place_sale = df.pivot_table(index='景点名称', values='销量')

    # 2、根据销量排序
    # inplace=True    排序之后的数据直接替换原来的数据
    # ascending=True  升序排列
    place_sale.sort_values('销量', inplace=True, ascending=True)

    # 3、生成柱状图
    place_sale_bar = (
        Bar()
            # list类型（index 下标）
            .add_xaxis(place_sale.index.tolist()[-20:])

            # int 类型（value 值）
            .add_yaxis("", list(map(int, np.ravel(place_sale.values)))[-20:])

            .reversal_axis()

            # 向右延伸
            .set_series_opts(label_opts=opts.LabelOpts(position="right"))

            .set_global_opts(
            # 标题
            title_opts=opts.TitleOpts(title="国庆旅游热门景点门票销量TOP20"),
            # y轴名称
            yaxis_opts=opts.AxisOpts(name="景点名称"),
            # x轴名称
            xaxis_opts=opts.AxisOpts(name="销量")
        )
    )
    place_sale_bar.render('analysis/place-sale-bar.html')


# 2、销售额：谁的吸金厉害
def analysis_amount():
    '''
    销售额=单价*销量
    :return:
    '''
    df = DF.copy()

    # 1、获取每个景点的销售额
    amount_list = []
    for index, row in df.iterrows():
        try:
            amount = row['门票价格'] * row['销量']
        except:
            amount = 0
        amount_list.append(amount)

    # 将销售额，添加给df
    df['amount'] = amount_list

    # 2、生成图表：名称和销售额
    place_amount = df.pivot_table(index='景点名称', values='amount')

    # 3、将销售额排序
    place_amount.sort_values('amount',inplace=True,ascending=True )

    # 4、生成柱状图
    place_amount_bar = (
            Bar()
                .add_xaxis(place_amount.index.tolist()[-20:])
                .add_yaxis("", list(map(int, np.ravel(place_amount.values)))[-20:])
                .reversal_axis()
                .set_series_opts(label_opts=opts.LabelOpts(position="right"))
                .set_global_opts(
                title_opts=opts.TitleOpts(title="国庆旅游热门景点门票销售额TOP20"),
                yaxis_opts=opts.AxisOpts(name="景点名称"),
                xaxis_opts=opts.AxisOpts(name="销售额")
            )
        )
    place_amount_bar.render('amount/place-amount-bar.html')


# 3、 生成热力图
def analysis_hot_sale():
    global DF
    df = DF.copy()

    # 遍历数据
    point_sale_list = []  # 暂时保存数据
    for index, row in df.iterrows():
        # 构建坐标数据
        lng, lat = row['坐标'].split(',')
        sale = row['销量']

        point_sale = { 'lng':float(lng), 'lat': float(lat), 'sale': sale }
        point_sale_list.append(point_sale)

    # 数据赋值给  var points
    data = f'var points ={str(point_sale_list)};'

    # 替换模板中的坐标数据
    with open(HOT_MAP_TEMPLATE_PATH, 'r', encoding='utf-8') as f1, open(PLACE_HOT_MAP_PATH, 'w', encoding="utf-8") as f2:

        # 读取f1的数据
        st1 = f1.read()

        # 替换数据
        st2 = st1.replace('%data%', data)
        # 将替换的数据，写入f2
        f2.write(st2)

        f1.close()
        f2.close()


# 推荐排行榜：推荐系数=评分/(销量价格) * 1000
def analysis_recommend():
    global DF
    df = DF.copy()

    # 获取Excel数据
    recommend_list = []
    for index, row in df.iterrows():
        try:
            # （评分 / 销量额） * 1000
            recommend = (row['评分'] * 1000) / (row['门票价格'] * row['销量'])
        except Exception:
            recommend = 0

        recommend_list.append(recommend)

    # 赋值给df
    df['recommend'] = recommend_list

    # 生成一个名称和瞎推荐系数的透视表
    place_recommend = df.pivot_table(index='景点名称', values='recommend')
    # 根据瞎推荐系数排序
    place_recommend.sort_values('recommend', inplace=True, ascending=True)

    # 生成柱状图
    place_recommend_bar = (
        Bar()
            .add_xaxis(place_recommend.index.tolist()[-20:])
            .add_yaxis("", list(map(int, np.ravel(place_recommend.values)))[-20:])
            .reversal_axis()
            .set_series_opts(label_opts=opts.LabelOpts(position="right"))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="国庆旅游热门景点瞎推荐TOP20"),
            yaxis_opts=opts.AxisOpts(name="景点名称"),
            xaxis_opts=opts.AxisOpts(name="瞎推荐系数")
        )
    )
    place_recommend_bar.render('recommend/place-recommend-bar.html')


if __name__ == '__main__':
    analysis_sale()  # 销量排序
    analysis_amount()  # 销售额排序
    analysis_hot_sale()  # 生成热力图
    analysis_recommend()  #推荐排行榜
