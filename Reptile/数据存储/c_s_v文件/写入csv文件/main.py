# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/9/22 0022 15:55'

'''
写入csv文件：列表和字典方式写入
'''


import csv


# csv标题
headers = ['username', 'age', 'height']


# 1、列表方式写入
def writer_csv_list():
    # csv数据
    values = [
        ('张三', 18, 180),
        ('李四', 19, 170),
        ('王五', 20, 190)
    ]

    # encoding='' 打开文件时，指定编码格式
    # 去掉空行。newline=''  默认为newline='\n'（每添加一行，添加一个空白字符）
    with open('classroom.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)  # 创建writer对象
        writer.writerow(headers)  # 写入标题
        writer.writerows(values)  # 写入多行数据
        print(type(writer.writerows))


# 2、字典方式写入
def writer_csv_dict():

    values = [
        {'username': "张三", 'age': 18, 'height': 190},
        {'username': "李四", 'age': 19, 'height': 180},
        {'username': "王五", 'age': 20, 'height': 170},
    ]

    with open("classroom_dict.csv", 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, headers)  # 传递两个参数：文件和标题(但标题需手动添加)
        writer.writeheader()  # 手动加入标题
        writer.writerows(values)


if __name__ == '__main__':
    # 爬取数据以 list(set) 格式，推荐使用
    writer_csv_list()
    # 爬取数据以 list(dict) 格式，推荐使用
    writer_csv_dict()