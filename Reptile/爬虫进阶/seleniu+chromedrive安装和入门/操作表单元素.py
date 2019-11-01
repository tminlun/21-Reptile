# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/10/17 0017 11:13'

import time
from selenium import webdriver

'''
1、获取元素
2、对元素进行操作
'''

# 初始化driver
driver_path = 'E:\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/?tn=78040160_26_pg&ch=1')
# # 打开浏览器
# driver.get('https://accounts.douban.com/passport/login_popup?login_source=anony')

# # 1、文本框输入数据
# inputTag = driver.find_element_by_id('kw')
# inputTag.send_keys('python')
# 清除输入框内容
# inputTag.clear()


# # 2、选中checkbox按钮
# rememberBtn = driver.find_element_by_name('remember')
# rememberBtn.click()  # 点击一次，选中
# # 点击两次，取消
# time.sleep(2)
# rememberBtn.click()


# # 3、select标签
# from selenium.webdriver.support.ui import Select
# selectBtn = Select(driver.find_element_by_name('jumpMane'))
# selectBtn.deselect_by_index(1)  # 选中第一个
# selectBtn.deselect_by_value("http:95约")  # 选中值为"http:95约"的select
# selectBtn.deselect_by_visible_text("95约")  # 选中文本为95的select
# selectBtn.deselect_all()  # 取消所有的选中


# 4、submit按钮
# 4.1、获取元素，文本框添加值
iptBtn = driver.find_element_by_id('kw')
iptBtn.send_keys('python')
# 4.2、点击submit按钮
submitBtn = driver.find_element_by_id('su')
submitBtn.click()


# 关闭浏览器
time.sleep(5)
driver.close()

