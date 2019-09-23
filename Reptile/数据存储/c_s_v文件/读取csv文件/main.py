# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/9/22 0022 15:06'

'''
读取csv文件：推荐 字典迭代器方式读取
'''

import csv,os

# 获取目录
up_path = os.path.abspath(os.path.dirname(os.getcwd()))  # dirname（去掉当前目录），abspath（返回上一级目录）
csv_path = os.path.join(up_path,'写入csv文件','classroom.csv')  # classroom.csv文件目录


# 1.读取csv，返回列表迭代器
def read_csv_list():
    with open(csv_path, 'r', encoding='utf-8') as f:
        # 创建reader：返回列表
        reader = csv.reader(f)
        next(reader)  # 去除标题（描述）
        for i in reader:
            print({"name":i[0], "age": i[1]})


# 2、读取csv，返回字典迭代器（推荐）
def read_csv_dict():
    with open(csv_path, 'r', encoding='utf-8') as f:
        # 创建reader字典迭代器对象
        # 字典迭代器，不包含标题信息
        reader = csv.DictReader(f)
        for i in reader:
            print({"name":i["username"], "age": i["age"]})


if __name__ == '__main__':
    print("列表：")
    read_csv_list()
    print("字典：")
    read_csv_dict()
