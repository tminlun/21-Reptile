# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/10/9 0009 15:19'

from queue import Queue
import threading
import time

'''
Queue：线程安全，各个Queue不相干扰

q = Queue(4)  创建一个（长度为4）先进先出的队列。

q.qsize()  队列的长度
q.empty()  队列是否为空
q.full()   队列是否已满
q.get()    获取队列最后一个元素
q.put()    将一个数据，按顺序插入队列中

'''


def set_value(q):
    index = 0
    while True:
        q.put(index)  # 先进先出的队列
        index += 1
        time.sleep(1)


def get_value(q):
    while True:
        print("%s的元素：%d" % (threading.current_thread(), q.get()))

        if q.full():
            print("|队列已满")
            break


def main():
    q = Queue(4)
    t1 = threading.Thread(target=set_value, args=[q])
    t2 = threading.Thread(target=get_value, args=[q], name="获取值")

    t1.start()
    t2.start()


if __name__ == '__main__':
    main()


