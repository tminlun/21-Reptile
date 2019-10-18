# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/10/18 0018 10:22'

import time
from selenium import webdriver
# 行为链类
from selenium.webdriver.common.action_chains import ActionChains

'''
行为链（ActionBuilder）：
    1、移动鼠标到输入框，输入框添加文本
    2、鼠标又移动到按钮，点击按钮
    3、执行
'''

# 初始化driver
driver_path = 'E:\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/?tn=78040160_26_pg&ch=1')

# 1、获取元素（输入框和按钮）
iptBtn = driver.find_element_by_id('kw')
subBtn = driver.find_element_by_id('su')

# 2、初始化行为链类
action = ActionChains(driver)

# 3、根据行为链，进行多个操作
# 3.1、移动鼠标到输入框
action.move_to_element(iptBtn)
# 3.2、输入框添加文本
action.send_keys_to_element(iptBtn, 'python')
# 3.4、鼠标又移动到按钮
action.move_to_element(subBtn)
# 3.5、点击subBtn按钮
action.click(subBtn)
# 3.6、执行行为链
action.perform()

