# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/10/12 0012 21:02'


# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/10/9 0009 15:58'


import os, requests, re, time
# 生产者和消费者
import threading

from lxml import etree
from urllib import request
# 队列
from queue import Queue


'''
1、把页面url （page_url）放进队列（page_queue）
2、（Producer）使用生产者解析 page_queue
3、解析完将元组（字典），放进队列（img_queue，队列类型为列表）
4、（Consumer）使用消费者（通过队列 img_queue）下载 img_url
5、创建5个线程：分别为生产者和消费者，执行：start()
'''

class Producer(threading.Thread):
    '''
    生产者：将img_url和filename添加到队列
    '''
    def __init__(self, page_queue, img_queue, *args, **kwargs):
        '''
            自定义参数 :param page_queue:   :param img_queue:
            父类的默认参数   :param args:   :param kwargs:
        '''

        # 重写父类的init
        super(Producer, self).__init__( *args, **kwargs)

        self.page_queue = page_queue
        self.img_queue = img_queue
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'Referer': 'http://www.doutula.com/photo/list/?page=1'
        }

    def run(self):
        '''
        获取url：
            使用多线程获取 img_url
         '''
        while True:
            # 不能死循环
            if self.page_queue.empty():
                # 队列无数据，退出线程
                break

            # 需多个线程不断去队列获取url
            url = self.page_queue.get()  # 获取队列（先进先出原则）最后一个url
            print(f"{threading.current_thread()}正在生产")
            self.parse_page(url)

    def parse_page(self, url):
        '''
        生产者：
            解析page_url完成，获取img_url和filename。
            再把(img_url, filename) 添加到队列：img_queue
        '''
        response = request.Request(url, headers=self.headers)
        html = request.urlopen(response)
        text = html.read().decode('utf-8')

        # 解析url
        html = etree.HTML(text)
        imgs = html.xpath('//div[contains(@class, "page-content")]//img[@class!="gif"]')
        for img in imgs:

            # get()  获取元素的属性
            img_url = img.get('data-original')  # 图片url

            # 后缀名 (suffix)
            # 图片名 + 后缀
            img_name = str(img.get('alt'))
            img_name = re.sub(r'[\.。\?？!！,，\*]', '', img_name)  # 替换
            suffix = os.path.splitext(img_url)[-1]

            # 重命名
            filename = img_name + suffix

            # 将字典（元组）添加到队列（队列类型为list）
            self.img_queue.put((img_url, filename))


class Consumer(threading.Thread):
    '''
    消费者
    '''
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Consumer, self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        '''
        下载图片
        '''

        while True:
            print(f"{threading.current_thread()}正在消费")
            # 不能死循环
            if self.page_queue.empty() and self.img_queue.empty():
                # 无page_queue和img_queue队列数据时，退出线程
                break

            #  获取图片URL和图片名
            img_url, filename = self.img_queue.get()  # 解压元组

            # 下载图片
            dir = os.path.abspath('images/')
            work_path = os.path.join(dir, filename)
            try:
                request.urlretrieve(img_url, work_path)  # 文件，文件名（异常：urllib.error.HTTPError: HTTP Error 403: Forbidden）
            except Exception:
                print('-' * 30)
                print(filename)
                print('-' * 30)
                continue


def main():
    # 创建先进先出的队列
    page_queue = Queue(10)  # 10个 页面路由
    img_queue = Queue(100)  # 100个 图片路由

    for page in range(1, 11):
        print(f'爬取斗图王，第{page}页')
        url = f'http://www.doutula.com/photo/list/?page={page}'
        page_queue.put(url)

    # 5个线程，分别为生产者和消费者
    for x in range(2):
        t1 = Producer(name="生产者", page_queue=page_queue,img_queue=img_queue)
        t1.start()

    for x in range(2):
        t2 = Consumer(name="消费者", page_queue=page_queue,img_queue=img_queue)
        t2.start()



if __name__ == '__main__':
    main()


