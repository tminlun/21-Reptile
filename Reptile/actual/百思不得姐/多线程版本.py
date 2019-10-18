# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/10/12 0012 23:23'

import threading
import requests
import csv
import os

from lxml import  etree
from queue import Queue

'''
多线程爬取百思不得姐：
    
    1、所有page_url存进page_queue队列
    2、使用生产者解析page_url，获取数据
    3、使用消费者将数据，保存到csv

'''


class Producer(threading.Thread):
    """
    生产者
    """
    def __init__(self,page_queue,jock_queue, *args, **kwargs):
        super(Producer, self).__init__(*args, **kwargs)  # 重写父类init
        self.page_queue = page_queue
        self.jock_queue = jock_queue

        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                          ' (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        }
        self.joint_url = 'http://www.budejie.com'  # 拼接的url

    def run(self):

        # 多个线程爬取，需要循环
        while True:

            if self.page_queue.empty():
                # 网页路由为空，退出线程
                break

            # 解析数据
            url = self.page_queue.get()  # 获取（先进先出原则）最后一个数据
            self.parse_page(url=url)

    def parse_page(self, url):
        # 请求数据
        response = requests.get(url, headers=self.headers)
        '''
        查看编码方式：
            import chardet
            print(chardet.detect(response.content))
        '''
        text = response.text

        # 解析数据
        html = etree.HTML(text)

        descs = html.xpath('//div[@class="j-r-list-c-desc"]')
        for desc in descs:
            # 提取数据
            # 内容
            jocks = desc.xpath('.//text()')
            # 将空白字符与内容分割，再使用strip()去空白字符
            jock = "\n".join(jocks).strip()  # （不join，strip()会抛出异常）

            # 链接
            link = self.joint_url + desc.xpath('./a/@href')[0]

            # 保存到队列（队列类型为list）
            self.jock_queue.put((jock, link))

        print("="*30 + "第%s页下载完成"%url.split('/')[-1]  +  "="*30)


class Consumer(threading.Thread):
    """
    消费者
    """
    def __init__(self, page_queue, jock_queue, lock, writer, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)  # 重写父类init
        self.page_queue = page_queue
        self.jock_queue = jock_queue
        self.writer = writer
        self.lock = lock

    def run(self):
        # 多个线程，需要循环
        while True:
            try:
                if self.jock_queue.empty() and self.page_queue.empty():
                    # 队列为空，退出线程
                    break

                # 获取队列数据
                jock, link = self.jock_queue.get(timeout=40)  # 等待timeout（秒）还不能读取，报empty异常

                # 写入数据让线程排队，防止数据错乱
                self.lock.acquire()  # 上锁
                self.writer.writerow((jock, link))  # 一行一行写入
                self.lock.release()  # 前个线程保存完数据，释放锁
                print("保存一条")
            except Exception:
                break



def main():

    page_queue = Queue(10)  # 长度为10，的网页路由队列
    jock_queue = Queue(500)  # 长度为100，的数据队列
    lock = threading.Lock()  # 全局锁，因为线程不排队，会出现数据错乱

    # 保存数据
    save_page = 'baijie.csv'

    if os.path.exists(save_page):
        # 更新csv
        os.remove(save_page)

    f = open(save_page, 'a', newline="", encoding="utf-8")  # open对象赋值给变量，才能异步操作
    # a 追加
    writer = csv.writer(f)  # 创建csv对象
    writer.writerow(('jock', 'link'))  # 写入标题


    # 创建线程
    for page in range(10):
        url = f'http://www.budejie.com/text/{int(page)}'
        page_queue.put(url)

    # 生产者
    for x in range(2):
        t1 = Producer(page_queue=page_queue, jock_queue=jock_queue)
        t1.start()

    # 消费者
    for x in range(2):
        t2 = Consumer(page_queue=page_queue, jock_queue=jock_queue, writer=writer, lock=lock)
        t2.start()




if __name__ == '__main__':
    main()


    # 测试版本
    """
    def test_versions():
        '''
        测试版本
        :return: 
        '''
        url = 'http://www.budejie.com/text/1'
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                          ' (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        }
        response = requests.get(url, headers=headers)
        text = response.text
    
        html = etree.HTML(text)
    
        descs = html.xpath('//div[@class="j-r-list-c-desc"]')
        jock_list = []
        for desc in descs:
            # 内容
            jocks = desc.xpath('.//text()')
            # 将空白字符与内容分割，再使用strip()去空白字符（不join()，无法strip()）
            jock = "\n".join(jocks).strip()
    
            # 链接
            link = desc.xpath('./a/@href')[0]
    
            jock_dict = (jock, link)
            # 储存到列表
            jock_list.append(jock_dict)
        # print("="*30 + "第%s页下载完成"%url.split('/')[-1] +  "="*30)
    
        save_page = 'baijie.csv'
        # 更新csv
        if os.path.exists(save_page):
            os.remove(save_page)
    
        with open(save_page, 'a', newline="", encoding="utf-8") as f:
            # a 追加
    
            writer = csv.writer(f)  # 创建csv对象
            writer.writerow(('jock', 'link'))  # 写入标题
            writer.writerows(jock_list)  # 写入多行数据
    """
