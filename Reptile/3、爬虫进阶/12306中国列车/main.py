# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/10/30 0030 15:49'

'''
步骤：
    1、手动登录，爬虫判断是否登录成功（系统自动转跳到"个人中页面"）。
    （等待）"个人中页面"有则打开查询车票页面，手动输入关键字（出发地、目的地、出发日、返程日）

    2、（等待）关键字有值，让爬虫点击"查询"按钮

    3、查找车次，查看对应的席位是否有余票（“有”、数字）。
        有余票，爬虫点击“预定”按钮。
        没有余票（“有”、数字），让爬虫循环点击"查询"按钮

    4、一旦检测到有余票，爬虫点击“预定”按钮。
    来到预定的界面后，找到需乘坐的乘客的checkbox，让爬虫点击CheckBox。
    再找到"提交订单"按钮，执行点击事件
    
    5、点击"提交订单"按钮后，会弹出一个对话框。找到"确认"按钮，执行点击事件
    
'''

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By  # 获取属性的方法
from selenium.webdriver.common.action_chains import ActionChains  # 多个动作(行为链)


class QiangPiao(object):
    driver_path = 'E:\chromedriver\chromedriver.exe'

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=QiangPiao.driver_path)  # 初始化driver
        self.login_url = "https://kyfw.12306.cn/otn/resources/login.html"  # 登录url
        self.PersonInfo_url = "https://kyfw.12306.cn/otn/view/index.html"  # 个人中心url
        self.search_url = "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc"  # 查询车票url
        self.reserve_url = "https://kyfw.12306.cn/otn/confirmPassenger/initDc"  # 订票页面
        # 2、初始化行为链类
        self.action = ActionChains(self.driver)

    def wait_input(self):
        '''
        定义需手动输入的变量
        :return: 手动输入的值和浏览器的值相验证
        '''

        self.from_station = "虎门"  # input("请输入出发地：")
        self.to_station = "广州南"  # input("请输入目的地：")
        # 格式必须是：YYYY-MM-dd
        self.depart_time = "2019-11-02"  #  input("出发日：")
        self.trains = ["G6222", "G1020"]  # input("请输入车次（如有多个车次，请用英文逗号分开）：").split(",")  # G74,G74  ==>  ["G6072", "G74"]
        self.linkmans = ["田敏伦"]

    def _login(self):
        '''
        登录：
            1、打开登录页面，手动输入参数
            2、如果有个人中心页面，则转跳成功
        :return:
        '''
        # 登录
        self.driver.get(self.login_url)
        # 显示等待（是否有个人中心页面）
        WebDriverWait(self.driver, 1000).until(
            # 当前url，是否为"个人中心"url
            EC.url_to_be(self.PersonInfo_url)
        )
        print("登录成功")


    def _order_ticket(self):
        '''
        订票：
            1、打开查询车票页面
        :return:
        '''

        # 覆盖"个人中心"页面
        self.driver.get(self.search_url)

        # 浏览器输入值
        # 设置值
        fromStationText = self.driver.find_element_by_xpath('//input[@id="fromStationText"]')
        fromStationText.clear()  # 清除input的value
        fromStationText.click()  # 点击才会弹出城市列表
        time.sleep(2)
        fromStationText.send_keys(self.from_station)

        # 点击
        time.sleep(2)
        WebDriverWait(self.driver, 1000).until(
            EC.presence_of_element_located((By.XPATH, '//div[@id="panel_cities"]//span'))
        )
        cityline_btn = self.driver.find_element_by_xpath('//div[@id="panel_cities"]/div[@id="citem_0"]')
        cityline_btn.click()


        # 目的地
        # 设置值
        fromStationText = self.driver.find_element_by_xpath('//input[@id="toStationText"]')
        fromStationText.clear()  # 清除input的value
        fromStationText.click()  # 点击才会弹出城市列表
        time.sleep(2)
        fromStationText.send_keys(self.to_station)

        # 点击
        time.sleep(2)
        WebDriverWait(self.driver, 1000).until(
            EC.presence_of_element_located((By.XPATH, '//div[@id="panel_cities"]//span'))
        )
        cityline_btn = self.driver.find_element_by_xpath('//div[@id="panel_cities"]/div[@id="citem_0"]')
        cityline_btn.click()


        # 等待浏览器输入值，与手动输入值匹配
        # 手动输入的出发地，和浏览器的出发地的值一致
        WebDriverWait(self.driver, 1000).until(
            # fromStationText元素的值与from_station的值匹配
            EC.text_to_be_present_in_element_value((By.ID, "fromStationText"), self.from_station)
        )

        # 目的地是否一致
        WebDriverWait(self.driver, 1000).until(
            EC.text_to_be_present_in_element_value((By.ID, "toStationText"), self.to_station)
        )

        # 出发日是否一致
        WebDriverWait(self.driver, 1000).until(
            EC.text_to_be_present_in_element_value((By.ID, "train_date"), self.depart_time)
        )


        # 点击查询
        # "查询"按钮是否可以点击，不可点击爬虫会抛出异常
        WebDriverWait(self.driver, 1000).until(
            EC.element_to_be_clickable((By.ID, "query_ticket"))
        )
        # 能点击，找到"查询"按钮，执行点击事件
        searchBtn = self.driver.find_element_by_id("query_ticket")
        searchBtn.click()

        # 预定车票
        # 1、不能刚点击"查询"按钮，就马上获取列车信息。（等待列车信息加载进来）
        WebDriverWait(self.driver, 1000).until(
            # 等待tr（非tbody）元素加载进来
            EC.presence_of_element_located((By.XPATH, '//tbody[@id="queryLeftTable"]/tr'))
        )

        # 2、找到没有datatran属性的tr标签（tr[not(@**)]）
        tr_list = self.driver.find_elements_by_xpath('//tbody[@id="queryLeftTable"]/tr[not(@datatran)]')  # 列表

        # 3、遍历所有tr标签
        for tr in tr_list:


            # 所有车次
            train_nums = tr.find_element_by_class_name('number').text  # 非列表
            # 匹配指定的车次（从浏览器车次列表，寻找与输入车次相同）
            if train_nums in self.trains:

                yes_ticket = tr.find_element_by_xpath('.//td[4]').text  # 二等座
                # 有余票
                if yes_ticket == "有" or yes_ticket.isdigit():
                    print(train_nums + "有票")
                    # 让爬虫点击"预定"按钮
                    reserve_btn = tr.find_element_by_class_name('btn72')
                    reserve_btn.click()

                    # 提交订单
                    # 预定成功才能提交订单
                    self.submit_order()




    def submit_order(self):
        '''
        提交订单
        :return:
        '''
        # 判断是否预定成功
        WebDriverWait(self.driver, 1000).until(
            # 当前url是否为订票页面
            EC.url_to_be(self.reserve_url)
        )

        # 打开新窗口，切换窗口
        self.driver.execute_script(r"window.open('%s')" % self.reserve_url)
        self.driver.switch_to_window(self.driver.window_handles[1])
        # WebDriverWait(self.driver, 1000).until(
        #     # 12306联系人是否加载进来
        #     EC.presence_of_element_located((By.XPATH, '//ul[@id="normal_passenger_id"]//label'))
        # )


        # 联系人方法1、
        # 联系人是否一致
        # label_names = self.driver.find_elements_by_xpath('//ul[@id="normal_passenger_id"]//label/text()')
        # if self.linkman in label_names:
        #     print("联系人一致")
        #     print(label_names)
        #
        #     # 选中联系人
        #     check_btns = self.driver.find_elements_by_xpath('//ul[@id="normal_passenger_id"]//input[@class="check"]')
        #     for check_btn in check_btns:
        #         check_btn.click()

        # 联系人方法2、
        normal_lis = self.driver.find_elements_by_xpath('//ul[@id="normal_passenger_id"]//li')  # 所有联系人li

        for li in normal_lis:  # 循环每个联系人，当匹配成功，选中
            li_label_name = li.find_element_by_xpath('./label').text   # 联系人姓名

            if li_label_name in self.linkmans:  # 12306联系人，如在（手动输入）联系人中
                # 选中
                check_btn = li.find_element_by_xpath('./input[@class="check"]')
                check_btn.click()

        # 关闭温馨提示
        # 温馨提示（非成人票）
        warm_prompt = self.driver.find_element_by_xpath('//div[contains(@class, "dhtmlx_wins_no_header)]')
        if warm_prompt:
            # 关闭
            close_warm_btn = self.driver.find_element_by_xpath('//div[contains(@class, "dhtmlx_wins_no_header")]//a[@id="qd_closeDefaultWarningWindowDialog_id"]')
            close_warm_btn.click()

        # 点击"提交订单"按钮后，会弹出一个对话框。找到"确认"按钮，执行点击事件
        submit_btn = self.driver.find_element_by_xpath('//div[@class="lay-btn"]//a[@id="submitOrder_id"]')
        submit_btn.click()
        qr_btn = self.driver.find_element_by_xpath('//div[@id="confirmDiv"]//a[@id="qr_submit_id"]')
        qr_btn.click()


        time.sleep(3)
        # 获取完详情数据，关闭详情窗口
        self.driver.close()
        # 切换列表窗口
        self.driver.switch_to_window(self.driver.window_handles[0])




    def run(self):
        '''
        主函数
        :return:
        '''
        self.wait_input()  # 调用方法，把输入的值保存到变量
        self._login()
        # 登录成功，转跳查询页面
        self._order_ticket()




if __name__ == '__main__':
    qiang_piao = QiangPiao()
    qiang_piao.run()
