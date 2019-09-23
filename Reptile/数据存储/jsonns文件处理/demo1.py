# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/9/21 0021 15:17'

import json

'''
json的dumps和dump序列化时对中文默认使用的ascii编码，所以会引起中文编码问题
dump  将py基本数据格式，系列化为json（写入  open(filename, 'w')）文件
load  将json数据类型，反系列化（读取 open(filename, 'r')）文件
'''

# 1、将py基本数据类型，转换为json字符串类型
emp_info = {'name': '黎明', 'age': 18}
jsn = json.dumps(emp_info,ensure_ascii=False)

'''
2、skipkeys=False（跳过非py基本数据类型） 如果为True，则跳过，如果为False，将抛出TypeError异常。
    ensure_ascii  转义为中文（unicode）
'''
error_data = {'name': '黎明', b'age': 18}
js_data = json.dumps(error_data,ensure_ascii=False,skipkeys=True)
print(js_data)  # True：{"name": "黎明"}；  False： TypeError: keys must be a string


# 3、将emp_info系列化，并去除ascii编码写入f指针的文件中
with open("emp.json", 'w', encoding='utf-8') as f:
    json.dump(emp_info, f, ensure_ascii=False)

# 4、反序列化读取json文件
with open("emp.json", 'r', encoding='utf-8') as f:
    ret = json.load(f)
    print(ret)
