# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/10/18 0018 21:02'

'''
防止爬虫识别：使用代理ip
'''
from selenium import webdriver

# 实例化一个，启动Chrome的参数对象
options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=183.129.244.16:11232")

# 初始化driver对象
driver_path = r'E:\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)

driver.get('http://httpbin.org/ip')

