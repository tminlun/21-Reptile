# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/10/22 0022 21:49'

import time

from selenium import webdriver
from lxml import etree

from selenium.webdriver.support.ui import WebDriverWait  # 显示等待
from selenium.webdriver.support import expected_conditions as EC  # 获取元素
from selenium.webdriver.common.by import By  # 获取属性的方法


class Boss(object):

    driver_path = 'E:\chromedriver\chromedriver.exe'

    def __init__(self):
        self.list_url = 'https://www.zhipin.com/c101280100/?query=python&ka=sel-city-101280100'
        self.driver = webdriver.Chrome(executable_path=Boss.driver_path)  # 初始化driver

    def main(self):
        '''
        主入口
        :return:
        '''
        # 获取列表数据（ajax、html）
        self.driver.get(self.list_url)

        while True:
            try:
                source = self.driver.page_source
                self.parse_list_page(source)  # 解析列表

                # 按钮加载进来，再点击下一页
                WebDriverWait(driver=self.driver, timeout=10).until(
                    EC.presence_of_element_located((By.XPATH, '//div[@class="page"]//a[last()]'))
                )

                next_btn = self.driver.find_element_by_xpath('//div[@class="page"]//a[last()]')
                if "disabled" in next_btn.get_attribute("class"):
                    # 尾页，不点击，并退出循环
                    break
                else:
                    # 点击下一页
                    next_btn.click()

            except Exception as e:
                print("异常：\n")
                print(e)


    def parse_list_page(self, source):
        '''获取详情url'''
        html = etree.HTML(source)
        links = html.xpath('//div[@class="job-primary"]/div[@class="info-primary"]/h3/a/@href')
        for link in links:
            time.sleep(1)
            detail_url = f'https://www.zhipin.com/{link}'
            self.request_detail_url(detail_url)

    def request_detail_url(self, url):
        '''
        1、打开详情新窗口，切换窗口
        2、获取数据
        3、解析数据
        4、关闭
        5、切换列表窗口

        :param url:
        :return:
        '''
        # 打开新窗口，切换窗口
        self.driver.execute_script(r"window.open('%s')" % url)
        self.driver.switch_to_window(self.driver.window_handles[1])
        # 获取详情数据
        source = self.driver.page_source
        self.parse_detail_page(source)

        # 获取完详情数据，关闭详情窗口
        self.driver.close()
        # 切换列表窗口
        self.driver.switch_to_window(self.driver.window_handles[0])

    def parse_detail_page(self, source):
        '''
        解析详情数据
        :param source:
        :return:
        '''
        pass



if __name__ == '__main__':
    boss = Boss()
    boss.main()




