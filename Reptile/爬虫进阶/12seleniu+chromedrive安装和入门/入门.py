# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/10/17 0017 10:09'

from selenium import webdriver
import time

# 定义webdriver路径
driver_path = 'E:\chromedriver\chromedriver.exe'

# 初始化driver
driver = webdriver.Chrome(executable_path=driver_path)

# 打开浏览器
driver.get('https://www.baidu.com/')
time.sleep(2)

# # 关闭之前的窗口
# driver.close()

# # 关闭全部窗口
# driver.quit()
