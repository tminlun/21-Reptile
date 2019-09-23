# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/9/22 0022 21:41'


'''
查询数据：cursor.fetchone()【单个】、fetchall（）【全部】fetchmany(2)【筛选】
'''

import pymysql

# 打开数据库连接
db = pymysql.connect(host="127.0.0.1",user="root",password="root",database="pymysql_demo",port=3306)

# 创建游标
cursor = db.cursor()

# 执行语句

# 获取单个数据
cursor.execute("""
    select username, age, sex from user
""")


# #  获取单个数据
# while True:
#     ret = cursor.fetchone()
#     if ret:
#         print(ret)
#     else:
#         break

# # 获取全部数据
# rets = cursor.fetchall()
# for ret in rets:
#     print(ret)

# # 获取指定数据
# rets = cursor.fetchmany(2)
# for ret in rets:
#     print(ret)

db.close()

