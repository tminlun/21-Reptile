# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/10/18 0018 13:28'

'''
隐式等待：
    获取ajax不确定的的元素前，会先等待n秒。
    如已经有数据，必须等待完n秒，才停止等待（即使指定时间内已获取）
    超过n秒，未有数据，抛出异常
    
显示等待（推荐）：
    某个条件“成立”后，才执行某个获取元素操作
    如已经有数据，停止等待
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  # 显示等待
from selenium.webdriver.support import expected_conditions as EC  # 获取元素
from selenium.webdriver.common.by import By  # 获取属性的方法


# 初始化driver
driver_path = r'E:\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.douban.com/')

# # 隐式等待，3秒内获取不确定元素。超过3秒，再抛出异常
# driver.implicitly_wait(3)
# driver.find_element_by_id('qdwadad')


# 显示等待
# 10秒内有数据，停止等待并返回数据
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'dale_anonymous_homepage_right_top'))
)
print(element)





# 关闭窗口
import time
time.sleep(1)
driver.close()
