# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/10/18 0018 20:26'

'''
execute_script：打开新窗口
switch_to_window：切换窗口
window_handles[n]：窗口的列表-*- n窗口下标
current_url：当前URL
'''
import time
from selenium import webdriver


# 初始化driver
driver_path = r'E:\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get(r'https://www.douban.com/')

# 打开新窗口-切换窗口（默认打开另外一个窗口，但并为当前执行的url）
driver.execute_script(r"window.open('https://space.bilibili.com/339846648/favlist?fid=474494248&ftype=create')")  # 使用JS打开新窗口
# 切换窗口（当前url的下标为0，并不是新窗口的url）
driver.switch_to_window(driver.window_handles[1])

print(driver.window_handles)  # 窗口列表
print(driver.current_url)  # 当前url





time.sleep(3)
driver.quit()
