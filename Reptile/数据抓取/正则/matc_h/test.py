# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/9/12 0012 13:08'

class Cat:
    def __init__(self,new_name):
        self.name = new_name
        print("%s 来了" %self.name)

    def __del__(self):
        print("%s 去了" %self.name)

# tom 是一个全局变量
tom = Cat("TomCat")
# # print(tom.name)
#
# print("-" * 50)
#
# # del 关键字可以删除一个对象
# del tom
#
# print("del tom------------------------")

# lazy_cat = Cat("大懒猫")
# print(lazy_cat.name)
# print("print(lazy_cat.name)--------------------------")