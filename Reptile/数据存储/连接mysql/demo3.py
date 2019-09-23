# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/9/22 0022 22:36'


'''
删除和修改数据
'''

import pymysql

# 打开数据库连接
db = pymysql.connect(host="127.0.0.1",user="root",password="root",database="pymysql_demo",port=3306)

# 创建游标
cursor = db.cursor()

# sql语句

# 删除数据
del_sql = """
        delete from user where id=4
    """

# 修改数据
update_sql = """
        update user set username='zhuzhu' where id=3
    """

try:
    cursor.execute(update_sql)
    print("成功")
except:
    print("失败")

db.commit()

db.close()


'''
一个整数，当它加上100是一个完全平方。加上268也是一个完全平方
'''
for i in range(100000):
    import math

    # 对每个数进行 + 100，在开平方（取整）
    x = int(math.sqrt(i + 100))
    y = int(math.sqrt(i + 268))

    # [如果平方数相乘===这个数 + 100]（非小数）
    if x * x == (i + 100) and y * y == (i + 268):
        print(i)

