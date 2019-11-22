# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/10/21 0021 13:19'

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebElement

'''
WebElement介绍：
    get_attribute('value')：获取元素的属性值
    save_screenshot('baidu.png')：截图

'''

# 初始化driver
driver_path = 'E:\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/?tn=78040160_26_pg&ch=1')

iptBtn = driver.find_element_by_id('su')


print(iptBtn.get_attribute('value'))
driver.save_screenshot('baidu.png')
