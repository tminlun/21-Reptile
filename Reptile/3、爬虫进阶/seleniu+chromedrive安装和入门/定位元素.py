# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/10/17 0017 10:23'

from selenium import webdriver
from selenium.webdriver.common.by import By


'''
1、如果只想要解析网页中的数据，推荐使用lxml
2、如果给元素一些操作，如给文本框一个值
'''


# 定义webdriver路径
driver_path = 'E:\chromedriver\chromedriver.exe'
# 初始化driver
driver = webdriver.Chrome(executable_path=driver_path)
# 打开浏览器
driver.get('https://www.baidu.com/')


# 定位元素
# iptTag = driver.find_element_by_id('kw')  # id
# iptTag = driver.find_element_by_class_name('s_ipt')  # class
# iptTag = driver.find_element_by_name('wd')  # name

# iptTag = driver.find_element_by_xpath('//input[@id="kw"]')
iptTag = driver.find_element(By.XPATH, '//input[@id="kw"]')

# iptTag = driver.find_element_by_css_selector('.s_ipt_wr input')  # css

iptTag.send_keys("python")  # 填充关键字

# # 关闭
# time.sleep(2)
# driver.quit()
