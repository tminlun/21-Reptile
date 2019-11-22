# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/10/18 0018 12:31'

from selenium import webdriver

'''
webdriver操作cookie：
    driver.get_cookies(): 所有cookie信息
    driver.get_cookie('BAIDUID')  # 获取name为"BAIDUID"的整行信息
    driver.delete_cookie('BAIDUID')  # 删除单行cookie数据
    
'''

# 初始化driver
driver_path = 'E:\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/?tn=78040160_26_pg&ch=1')


for cookie in driver.get_cookies():
    print(cookie)
print("=" * 30)

print(driver.get_cookie('BAIDUID'))  # 获取name为"BAIDUID"的整行信息
print("=" * 30)

# 删除单行cookie
driver.delete_cookie('BAIDUID')
print(driver.get_cookie('BAIDUID'))  # None
print("=" * 30)

# 删除全部cookie数据
driver.delete_all_cookies()

for cookie in driver.get_cookies():
    print(cookie)
