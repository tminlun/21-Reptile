# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/9/22 0022 20:24'


'''
添加数据
'''

import pymysql

# 打开数据库连接
db = pymysql.connect(host="127.0.0.1",user="root",password="root",database="pymysql_demo",port=3306)

# 创建游标
cursor = db.cursor()


# 执行语句

# 创建表  auto_increment(自增) UNIQUE(唯一)
create_table = """
        create table user(
            id int(11) not null primary key auto_increment UNIQUE,
            username varchar(255) not null ,
            age int ,
            sex char (1)
        );
"""

# 插入数据（使用%s，动态插入数据）
insert_table = """
    insert into user(username,age,sex) values (%s,%s,%s)
"""

# 数据
username = "zhl"
age = 21
sex = '女'

cursor.execute(insert_table,(username,age,sex))

# 提交到数据库
db.commit()


# 关闭数据库连接
cursor.close()

