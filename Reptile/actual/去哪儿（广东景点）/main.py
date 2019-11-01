# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/10/23 0023 17:03'


'''
模拟浏览器行为
'''
import time, re, csv

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  # 显示等待
from selenium.webdriver.support import expected_conditions as EC  # 获取元素
from selenium.webdriver.common.by import By  # 获取属性的方法
from lxml import etree


class Ticket(object):
    # 定义webdriver路径
    driver_path = 'E:\chromedriver\chromedriver.exe'

    def __init__(self):
        # 初始化driver
        self.driver = webdriver.Chrome(executable_path=Ticket.driver_path)
        self.url = 'https://piao.qunar.com/ticket/list.htm?keyword=%E5%B9%BF%E4%B8%9C&region=&from=mpl_search_suggest'

        # 写入csv
        fp = open(r'ticket.csv', 'a', newline='', encoding='utf-8')
        headers = ['name', 'mp_ticket_title', 'mp_ticket_price']
        self.writer = csv.DictWriter(fp, headers)
        self.writer.writeheader()


    def main(self):
        self.driver.get(self.url)

        # 模拟点击下一页
        while True:
            # 操作上个列表数据完
            source = self.driver.page_source
            self.parse_list_page(source)

            # 操作完，点击下一页
            time.sleep(2)  # 防封ip

            # 显示等待，数据加载完成再点击下一页
            WebDriverWait(driver=self.driver, timeout=10).until(
                EC.presence_of_element_located((By.XPATH, '//div[@class="pager"]/a[last()]'))
            )
            try:
                next_btn = self.driver.find_element_by_xpath('//div[@class="pager"]/a[last()]')
                if "display: none;" in next_btn.get_attribute("style"):
                    # 尾页
                    break
                else:
                    next_btn.click()

            except Exception:
                print(source)



            break

    def parse_list_page(self, source):
        '''
        通过解析列表，获取详情url
        :param source: 列表数据
        '''
        html = etree.HTML(source)
        links = html.xpath('//div[@class="sight_item_about"]/h3[@class="sight_item_caption"]/a[@class="name"]/@href')
        for link in links:
            detail_url = f'https://piao.qunar.com{link}'
            self.request_detail_url(detail_url)

            time.sleep(2)  # 防封ip

    def request_detail_url(self, detail_url):
        '''
        请求详情：
            1、打开新窗口
            2、切换窗口到详情
            3、获取source，并等待数据加载进来，才爬取详情数据
            4、爬取完毕，关闭当前详情
            5、切换窗口回列表

        :param detail_url: 详情url
        '''

        # 1、打开新窗口
        self.driver.execute_script(r"window.open('%s')" % detail_url)

        # 2、切换窗口到详情
        self.driver.switch_to_window(self.driver.window_handles[1])

        # 3、获取source，并等待数据加载进来，才爬取详情数据
        detail_source = self.driver.page_source
        WebDriverWait(driver=self.driver, timeout=10).until(
            # By.XPATH只能获取元素，不能获取文本
            EC.presence_of_element_located((By.XPATH, '//div[@class="mp-description-view"]/span[@class="mp-description-name"]'))
        )
        self.parse_detail_url(detail_source)

        # 4、爬取完毕，关闭当前详情
        self.driver.close()

        # 5、切换窗口回列表
        self.driver.switch_to_window(self.driver.window_handles[0])

    def parse_detail_url(self, detail_source):
        mp_ticket_list = []

        html = etree.HTML(detail_source)

        # 门票
        mp_tickets = html.xpath('//div[@class="mp-groupbody-container"]/div[@class="mp-ticket"]')
        for mp_ticket in mp_tickets:
            # 景点名称
            name = html.xpath('//div[@class="mp-description-view"]/span[@class="mp-description-name"]/text()')[0].strip()

            # 门票名
            mp_ticket_title = mp_ticket.xpath('./div[@class="mp-ticket-title"]/text()')[0]
            mp_ticket_title = re.sub(r'[\s]', '', mp_ticket_title)

            # 门票价格
            mp_ticket_price = mp_ticket.xpath('./div[@class="mp-group-price"]//em/strong/text()')[0]
            mp_ticket_price = re.sub(r'[\s]', '', mp_ticket_price)

            mp_ticket_dict = {
                'name': name,
                'mp_ticket_title': mp_ticket_title,
                'mp_ticket_price': mp_ticket_price
            }
            self.writer.writerow(mp_ticket_dict)

            mp_ticket_list.append(mp_ticket_dict)

        print(mp_ticket_list)






if __name__ == '__main__':
    ticket = Ticket()
    ticket.main()
