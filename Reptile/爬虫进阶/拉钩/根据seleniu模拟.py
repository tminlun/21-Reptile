# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/10/22 0022 13:03'

'''
模拟浏览器请求拉勾网：
    1、获取详情url
    2、获取详情信息
    
    page_source：与请求网页不同，他可以获取，页面所看到全部数据（ajax，html）
'''
import time
import re
import csv

from selenium import webdriver
from lxml import etree
from selenium.webdriver.support.ui import WebDriverWait  # 显示等待
from selenium.webdriver.support import expected_conditions as EC  # 获取元素
from selenium.webdriver.common.by import By  # 获取属性的方法


class LagouReptile(object):
    """
    1、根据列表获取详情url
    2、根据详情url，解析详情数据


    """

    driver_path = 'E:\chromedriver\chromedriver.exe'

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=LagouReptile.driver_path)
        self.url = 'https://www.lagou.com/jobs/list_python/p-city_213?px=default#filterBox'  # 列表
        self.positions = []  # 储存详情数据

        # 初始化csv
        fp = open('lagou.csv', 'a', encoding='utf-8', newline='')
        headers = ['name', 'salary', 'city', 'experience', 'degree', 'desc', 'namwork_addr']
        self.writer = csv.DictWriter(fp, headers)
        self.writer.writeheader()  # 手动加入标题

    def main(self):
        '''
        主入口：
            1、打开首页（打开一次即可），获取数据
            2、等元素某个子或本元素加载进来，再获取该元素
            3、循环点击“下一页”
            4、无“下一页”，退出循环
        '''
        self.driver.get(self.url)  # 打开首页

        while True:

            # 获取数据
            source = self.driver.page_source  # 获取ajax和html数据
            self.parse_list_page(source)  # 获取详情url

            # 按钮未加载，点击“下一页”会报错。（等元素某个子或本元素加载进来，再获取该元素）
            WebDriverWait(driver=self.driver, timeout=10).until(
                EC.presence_of_element_located((By.XPATH, '//div[@class="pager_container"]/span[last()]'))
            )

            try:
                # 循环点击“下一页”
                next_btn = self.driver.find_element_by_xpath('//div[@class="pager_container"]/span[last()]')  # 获取"下一页"按钮
                if "pager_next_disabled" in next_btn.get_attribute("class"):
                    # 最后一页，退出循环（不点击）
                    break
                else:
                    # 否，点击下一页
                    next_btn.click()
            except:
                print(source)

            # 防止封ip
            time.sleep(2)






    def parse_list_page(self, source):
        '''
        获取详情url
        :return  保存详情url
        '''
        html = etree.HTML(source)
        links = html.xpath('//a[@class="position_link"]/@href')  # 单页的所有详情url
        for link in links:
            self.request_detail_page(link)
            time.sleep(1)

    def request_detail_page(self, url):
        '''
        提取详情数据：
            1、爬取完1个详情后，马上关闭
            2、切换回列表
            3、再进行爬取下一详情（保证只存在两个窗口）

        '''
        # 获取详情数据 1：self.driver.get(url) ：
        #   在当前窗口打开详情页面，会自动覆盖列表窗口
        #   “详情”覆盖“列表”窗口后，就无“下一页”按钮，即无法点击下一页

        # 1、获取详情数据 2：（推荐）
        #   打开新窗口，不覆盖“列表窗口”
        self.driver.execute_script("window.open('%s')" % url)
        self.driver.switch_to_window(self.driver.window_handles[1])  # 爬取1个详情，关闭窗口。再爬取下一个
        source = self.driver.page_source

        # # 显示等待：等元素的子元素或本元素。等标题加载进来，再获取详情页面数据
        WebDriverWait(driver=self.driver, timeout=10).until(
            # By.XPATH只能获取元素，不能获取文本
            EC.presence_of_element_located((By.XPATH, '//div[@class="job-name"]//h1[@class="name"]'))
        )

        # 2、解析详情页完成
        self.parse_detail_page(source)
        # 3、关闭详情页
        self.driver.close()
        # 4、切换回列表
        self.driver.switch_to_window(self.driver.window_handles[0])


    def parse_detail_page(self, source):
        '''解析详情页面'''

        # 提取数据
        html = etree.HTML(source)

        name = html.xpath('//div[@class="job-name"]//h1[@class="name"]//text()')[0]  # 标题

        # 标签
        #
        span_list = html.xpath('//dd[@class="job_request"]//span')
        # 薪资
        salary = span_list[0].xpath('.//text()')[0].strip()
        # 城市
        city = span_list[1].xpath('.//text()')[0].strip()
        city = re.sub(r'[\s/]', '', city)
        # 经验
        experience = span_list[2].xpath('.//text()')[0].strip()
        experience = re.sub(r'[\s/]', '', experience)
        # 学历
        degree = span_list[3].xpath('.//text()')[0].strip()
        degree = re.sub(r'[\s/]', '', degree)
        # 介绍
        desc = "".join(html.xpath('//dd[@class="job_bt"]//text()')).strip()  # 转为字符串，再去空格
        desc = re.sub(r'[\s]', '', desc)
        # 地址
        work_addr = "".join(html.xpath('//div[@class="work_addr"]//text()')).strip()
        work_addr = re.sub(r'[\s]', '', work_addr)

        # 转为字典，放进列表
        position = {
            'name': name,
            'salary': salary,  # 薪资
            'city': city,
            'experience': experience,  # 经验
            'degree': degree,  # 学历
            'desc': desc,  # 介绍
            'namwork_addr' : work_addr,  # 地址
        }
        self.writer.writerow(position)
        self.positions.append(position)
        print(position)
        print('='*30)



if __name__ == '__main__':
    lagou = LagouReptile()
    lagou.main()

